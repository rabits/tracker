#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import RPi.GPIO as gpio

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
                setattr(self, action, lambda self, pin=socket['pin']: gpio.output(pin, not gpio.input(pin)))
            else:
                log.warn("GPIO type %s unsupported for socket %s" % (socket_type, action))

        # Init listen GPIO's
        for name, item in self._cfg.get('listen', {}).iteritems():
            log.info("Attaching GPIO listener %s to pin %d" % (name, item['pin']))
            self._pin_map[item['pin']] = name
            gpio.setup(item['pin'], gpio.IN)
            gpio.add_event_detect(item['pin'], gpio.BOTH, callback=self._listenTrigger)

    def stop(self):
        Module.stop(self)
        gpio.cleanup()
        self._pin_map = {}

    def _listenTrigger(self, pin):
        name = self._pin_map[pin]
        item = self._cfg['listen'][name]
        value = gpio.input(item['pin'])
        log.info("Triggered listener %s with value %s" % (name, value))

        for signal in item['signals']:
            if signal.get('when', True) == value:
                self.signal(signal)
