#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import subprocess
from gi.repository import GObject
import dbus, dbus.service

import Log as log
from Module import Module

BUS_NAME = 'org.bluez'
AGENT_INTERFACE = BUS_NAME+'.Agent1'
DEVICE_INTERFACE = BUS_NAME+'.Device1'
MEDIA_INTERFACE = BUS_NAME+'.MediaControl1'

class Agent(dbus.service.Object):
    _pin = None

    def setPin(self, pin):
        self._pin = pin
        if not (isinstance(self._pin, str) or isinstance(self._pin, int)):
            import string, os
            chars = string.ascii_letters + string.digits + '+-'
            self._pin = ''.join([chars[ord(os.urandom(1)) % len(chars)] for i in xrange(8)])
            log.warn('Generated bluetooth password: "%s"' % self._pin)

    @dbus.service.method(AGENT_INTERFACE, in_signature="", out_signature="")
    def Release(self):
        log.debug("Release")

    @dbus.service.method(AGENT_INTERFACE, in_signature="", out_signature="")
    def Cancel(self):
        log.debug("Cancel")

    @dbus.service.method(AGENT_INTERFACE, in_signature="o", out_signature="s")
    def RequestPinCode(self, device):
        log.debug("RequestPinCode %s" % device)
        self.setTrusted(device)
        return self._pin

    def setTrusted(self, path):
        props = dbus.Interface(self._connection.get_object(BUS_NAME, path), "org.freedesktop.DBus.Properties")
        props.Set(BUS_NAME+".Device1", "Trusted", True)
        log.debug("Set trusted %s" % path)

class Bluetooth(Module):
    """Bluetooth device controller - manage bluetooth device"""

    def __init__(self, **kwargs):
        Module.__init__(self, **kwargs)

        self.setState(self._cfg.get('enabled', False))
        self.setDeviceClass("0x6c041c")
        self.setDeviceName(self._cfg.get('name', 'tracker-1'))
        self.setSSP(False) # Secure Simple Pairing - if enabled will disable pin pairing (not supported) (not secure)
        self.setAFH(self._cfg.get('afh', True))
        self.setEncryption(self._cfg.get('encrypt', True))
        self.setVisibility(self._cfg.get('visible', False))
        self.setAuth(self._cfg.get('auth', False))

        self._bus = dbus.SystemBus()

        self._agent = Agent(self._bus, "/tracker/agent")
        self._agent.setPin(self._cfg.get('pin', None))

        manager = dbus.Interface(self._bus.get_object(BUS_NAME, "/org/bluez"), BUS_NAME+".AgentManager1")
        manager.RegisterAgent("/tracker/agent", "NoInputNoOutput")
        manager.RequestDefaultAgent("/tracker/agent")

        self._connected_devices = {}

        self._bus.add_signal_receiver(self._devicePropertyChanged,
                                      bus_name=BUS_NAME, signal_name='PropertiesChanged',
                                      path_keyword='device_path', interface_keyword='interface')

    def stop(self):
        Module.stop(self)
        for name in self._connected_devices.keys():
            dev = self._connected_devices.pop(name)
            dev.kill()
            dev.poll()
        manager = dbus.Interface(self._bus.get_object(BUS_NAME, "/org/bluez"), BUS_NAME+".AgentManager1")
        manager.UnregisterAgent("/tracker/agent")

    def _exec(self, cmd):
        return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def setState(self, val):
        log.info("Set device state to '%s'" % ('up' if val else 'down'))
        self._exec(['sudo', 'hciconfig', self._cfg.get('dev'), 'up' if val else 'down'])

    def setDeviceClass(self, btclass):
        log.info("Set device class to '%s'" % btclass)
        self._exec(['sudo', 'hciconfig', self._cfg.get('dev'), 'class', btclass])

    def setDeviceName(self, name):
        log.info("Set device name to '%s'" % name)
        self._exec(['sudo', 'hciconfig', self._cfg.get('dev'), 'name', name])

    def setEncryption(self, val):
        log.info("Set device encryption to '%s'" % ('encrypt' if val else 'noencrypt'))
        self._exec(['sudo', 'hciconfig', self._cfg.get('dev'), 'encrypt' if val else 'noencrypt'])

    def setVisibility(self, visible):
        log.info("Set device visibility to '%s'" % ('visible' if visible else 'invisible'))
        self._exec(['sudo', 'hciconfig', self._cfg.get('dev'), 'piscan' if visible else 'pscan'])

    def setAuth(self, val):
        log.info("Set device authentication to '%s'" % ('enable' if val else 'disable'))
        self._exec(['sudo', 'hciconfig', self._cfg.get('dev'), 'auth' if val else 'noauth'])

    def setAFH(self, val):
        log.info("Set device AFH mode to '%s'" % ('enable' if val else 'disable'))
        self._exec(['sudo', 'hciconfig', self._cfg.get('dev'), 'afhmode', '1' if val else '0'])

    def setSSP(self, val):
        log.info("Set device SSP mode to '%s'" % ('enable' if val else 'disable'))
        self._exec(['sudo', 'hciconfig', self._cfg.get('dev'), 'sspmode', '1' if val else '0'])

    def _devicePropertyChanged(self, property_name, value, path, interface, device_path):
        if property_name != MEDIA_INTERFACE:
            return
 
        device = dbus.Interface(self._bus.get_object(BUS_NAME, device_path), interface)
        properties = device.GetAll(MEDIA_INTERFACE)
        properties_device = device.GetAll(DEVICE_INTERFACE)
 
        if properties['Connected']:
            if self._connected_devices.has_key(properties_device['Address']):
                return # Already connected
            log.info("Device: %s has connected: %s" % (properties_device['Name'], properties_device['Address']))

            log.info('Connecting device audio routing')
            self._connected_devices[properties_device['Address']] = self._exec(['bluealsa-aplay', properties_device['Address']])

            if len(self._connected_devices) == 1:
                log.info('Connecting GPIO sound output')
                self.signal('audio_switch')
        else:
            log.info("Device: %s has disconnected: %s" % (properties_device['Name'], properties_device['Address']))

            dev = self._connected_devices.pop(properties_device['Address'])
            dev.kill()
            if dev.poll() != None:
                log.debug('Audio routing application exited with code %d' % dev.poll())
            else:
                log.warn('Unable to kill the audio routing application pid: %d' % dev.pid)

            if len(self._connected_devices) < 1:
                log.info('Disconnecting GPIO sound output')
                self.signal('audio_switch')
