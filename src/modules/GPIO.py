#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import RPi.GPIO as gpio
import time

import Log as log
from Module import Module

class GPIO(Module):
    """GPIO - general purpose input/output interactor"""

    def __init__(self, **kwargs):
        Module.__init__(self, **kwargs)

        self._pin_map = {}
        gpio.setmode(gpio.BOARD)

    def start(self):
        Module.start(self)

        # Init socket GPIO's
        for action in self._cfg.get('sockets', []).keys():
            if hasattr(self, action):
                log.error("Unable to redefine existing function by socket %s" % action)
                continue

            socket = self._cfg['sockets'][action]
            log.info("Registering socket action %s for pin %d..." % (action, socket['pin']))
            gpio.setup(socket['pin'], gpio.OUT, initial=socket.get('default', False))

            socket_type = socket.get('type', 'switch')
            if socket_type == 'switch':
                setattr(self, action, lambda self=self, pin=socket['pin'], value=None: self.sendChange(pin, value))
            elif socket_type == 'pulse':
                setattr(self, action, lambda self=self, pin=socket['pin'], duration=socket.get('duration', None): self.sendPulse(pin, duration))
            else:
                log.warn("GPIO type %s unsupported for socket %s" % (socket_type, action))

    def postStart(self):
        '''Checking the current state of the listening GPIO's and do the configured actions'''
        Module.postStart(self)

        # Init listen GPIO's in poststart
        # We need to be sure that listen isn't triggered until all the modules was started
        for name, item in self._cfg.get('listen', {}).iteritems():
            log.info("Attaching GPIO listener %s to pin %d" % (name, item['pin']))
            self._pin_map[item['pin']] = name
            gpio.setup(item['pin'], gpio.IN)
            while self.isActive():
                # Sometimes event detection is can't be set up - so need retries
                try:
                    gpio.add_event_detect(item['pin'], gpio.BOTH, callback=self._listenTrigger)
                except RuntimeError:
                    log.error('Detected unable to set event detection for GPIO %s, retrying...' % item['pin'])
                    self.waitActive(1.0)
                    continue
                break

        for pin in self._pin_map:
            self._listenTrigger(pin)

    def stop(self):
        Module.stop(self)
        gpio.cleanup()
        self._pin_map = {}

    def _listenTrigger(self, pin):
        name = self._pin_map[pin]
        item = self._cfg['listen'][name]
        value = bool(gpio.input(item['pin']))
        log.debug('Triggered listener %s with value %s' % (name, value))

        for signal in item.get('signals', []):
            if signal.get('when') in (None, value):
                self.signal(signal, value = value)

    def sendChange(self, pin, value = None):
        '''Send change GPIO pin state to the required value or opposite value if value = None'''
        gpio.output(pin, not gpio.input(pin) if value is None else value)
        return bool(gpio.input(pin))

    def sendPulse(self, pin, duration = None):
        '''Send pulse to GPIO pin with required duration (sec)'''
        val = gpio.input(pin)
        gpio.output(pin, not val)
        if duration != None:
            time.sleep(duration)
        gpio.output(pin, val)
