#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import subprocess
from gi.repository import GObject
import dbus, dbus.service

import Log as log
from Module import Module

BUS_NAME = 'org.bluez'
PROPERTIES_INTERFACE = 'org.freedesktop.DBus.Properties'
ADAPTER_INTERFACE = BUS_NAME+'.Adapter1'
AGENT_INTERFACE = BUS_NAME+'.Agent1'
AGENT_MANAGER_INTERFACE = BUS_NAME+'.AgentManager1'
DEVICE_INTERFACE = BUS_NAME+'.Device1'
MEDIA_INTERFACE = BUS_NAME+'.MediaControl1'
PLAYER_INTERFACE = BUS_NAME+'.MediaPlayer1'

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
        props = dbus.Interface(self._connection.get_object(BUS_NAME, path), PROPERTIES_INTERFACE)
        props.Set(BUS_NAME+".Device1", "Trusted", True)
        log.debug("Set trusted %s" % path)

class Bluetooth(Module):
    """Bluetooth device controller - manage bluetooth device"""

    def __init__(self, **kwargs):
        Module.__init__(self, **kwargs)

        self._bus = dbus.SystemBus()
        self._agent = Agent(self._bus, "/tracker/agent")

        self._last_device = None
        self._resume_playing = None
        self._connected_devices = {}

    def start(self):
        Module.start(self)

        self._agent.setPin(self._cfg.get('pin', None))

        self.setState(self._cfg.get('enabled', True))
        self.setDeviceClass('0x200420')
        self.setDeviceName(self._cfg.get('name', 'tracker-1'))
        self.setSSP(False) # Secure Simple Pairing - if enabled will disable pin pairing (not supported) (not secure)
        self.setAFH(self._cfg.get('afh', True))
        self.setEncryption(self._cfg.get('encrypt', True))
        self.setVisibility(self._cfg.get('visible', False))
        self.setAuth(self._cfg.get('auth', False))

        manager = dbus.Interface(self._bus.get_object(BUS_NAME, '/org/bluez'), AGENT_MANAGER_INTERFACE)
        manager.RegisterAgent('/tracker/agent', 'NoInputNoOutput')
        manager.RequestDefaultAgent('/tracker/agent')

        self._listener = self._bus.add_signal_receiver(self._devicePropertyChanged,
                                                       bus_name=BUS_NAME, signal_name='PropertiesChanged',
                                                       path_keyword='device_path', interface_keyword='interface')

        self.restoreLastConnection()

    def postStart(self):
        Module.postStart(self)
        # TODO: enable already connected devices

    def stop(self):
        Module.stop(self)
        self._bus.remove_signal_receiver(self._listener)
        for name in self._connected_devices.keys():
            dev = self._connected_devices.pop(name)
            dev.kill()
            dev.poll()
        manager = dbus.Interface(self._bus.get_object(BUS_NAME, '/org/bluez'), AGENT_MANAGER_INTERFACE)
        manager.UnregisterAgent('/tracker/agent')

    def disableBluetooth(self):
        log.debug('Disabling Bluetooth adapter %s' % self.name())
        self.setVisibility(False)
        self.disconnectDevices()

    def enableBluetooth(self):
        log.debug('Enabling Bluetooth adapter %s' % self.name())
        self.setVisibility(self._cfg.get('visible', False))
        self.restoreLastConnection()

    def disconnectDevices(self):
        log.debug('Disconnecting all the connected devices')
        om = dbus.Interface(self._bus.get_object(BUS_NAME, '/'), 'org.freedesktop.DBus.ObjectManager')
        for path, interfaces in om.GetManagedObjects().iteritems():
            if ('/org/bluez/%s' % self._cfg.get('dev')) not in path or DEVICE_INTERFACE not in interfaces:
                continue
            props = interfaces[DEVICE_INTERFACE]
            if props['Connected']:
                log.debug(' - disconnecting device %s %s' %(props['Name'], props['Address']))
                device = dbus.Interface(self._bus.get_object(BUS_NAME, path), DEVICE_INTERFACE)
                device.Disconnect()

    def restoreLastConnection(self):
        if self._last_device != None:
            log.info('Connecting last device: %s' % self._last_device)
            self.signal('audio_switch', value = True)
            device = dbus.Interface(self._bus.get_object(BUS_NAME, self._last_device), DEVICE_INTERFACE)
            try:
                device.Connect()
            except dbus.exceptions.DBusException as e:
                log.warn('Unable to reconnect to the last connected device: %s' % e)
                self.signal('audio_switch', value = False)

    def _exec(self, cmd):
        return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def _exec_wait(self, cmd):
        ret = self._exec(cmd)
        if ret.wait() != 0:
            log.error('Failed to execute command')
            log.debug('STDOUT: %s\n\nSTDERR: %s' % ret.communicate())

    def setState(self, val):
        log.info("Set device state to '%s'" % ('up' if val else 'down'))
        # TODO: Replace with Adapter1 Set "Power" property
        self._exec_wait(['sudo', 'hciconfig', self._cfg.get('dev'), 'up' if val else 'down'])

    def setDeviceClass(self, btclass):
        log.info("Set device class to '%s'" % btclass)
        self._exec_wait(['sudo', 'hciconfig', self._cfg.get('dev'), 'class', btclass])

    def setDeviceName(self, name):
        log.info("Set device name to '%s'" % name)
        self._exec_wait(['sudo', 'hciconfig', self._cfg.get('dev'), 'name', name])

    def setEncryption(self, val):
        log.info("Set device encryption to '%s'" % ('encrypt' if val else 'noencrypt'))
        self._exec_wait(['sudo', 'hciconfig', self._cfg.get('dev'), 'encrypt' if val else 'noencrypt'])

    def setVisibility(self, visible):
        log.info("Set device visibility to '%s'" % ('visible' if visible else 'invisible'))
        self._exec_wait(['sudo', 'hciconfig', self._cfg.get('dev'), 'piscan' if visible else 'noscan'])

    def setAuth(self, val):
        log.info("Set device authentication to '%s'" % ('enable' if val else 'disable'))
        self._exec_wait(['sudo', 'hciconfig', self._cfg.get('dev'), 'auth' if val else 'noauth'])

    def setAFH(self, val):
        log.info("Set device AFH mode to '%s'" % ('enable' if val else 'disable'))
        self._exec_wait(['sudo', 'hciconfig', self._cfg.get('dev'), 'afhmode', '1' if val else '0'])

    def setSSP(self, val):
        log.info("Set device SSP mode to '%s'" % ('enable' if val else 'disable'))
        self._exec_wait(['sudo', 'hciconfig', self._cfg.get('dev'), 'sspmode', '1' if val else '0'])

    def _devicePropertyChanged(self, property_name, value, path, interface, device_path):
        if property_name == PLAYER_INTERFACE:
            if value.has_key('Status'):
                if self._resume_playing and value['Status'] == 'stopped':
                    log.debug('Resuming playing state')
                    player = dbus.Interface(self._bus.get_object(BUS_NAME, device_path), PLAYER_INTERFACE)
                    player.Play()
                if self._resume_playing and value['Status'] == 'playing':
                    self._resume_playing = False

            if value.has_key('Track'):
                log.debug('Current track is: %s' % value['Track'])

        if property_name == MEDIA_INTERFACE:
            if value.has_key('Connected'):
                device = dbus.Interface(self._bus.get_object(BUS_NAME, device_path), interface)
                properties = device.GetAll(DEVICE_INTERFACE)

                if value['Connected']:
                    if self._connected_devices.has_key(properties['Address']):
                        return # Already connected
                    log.info('Device: %s has connected: %s' % (properties['Name'], properties['Address']))

                    self._last_device = device_path

                    log.debug('Connecting device audio routing')
                    self._connected_devices[properties['Address']] = self._exec(['bluealsa-aplay', '--verbose', '-i', self._cfg.get('dev'), '--profile-a2dp', properties['Address']])

                    if len(self._connected_devices) == 1:
                        log.info('Connecting GPIO sound output')
                        self.signal('audio_switch', value = True)

                    self._resume_playing = self._cfg.get('media', {}).get('play_on_connected', True)
                else:
                    if not self._connected_devices.has_key(properties['Address']):
                        return # Not connected at all

                    log.info('Device: %s has disconnected: %s' % (properties['Name'], properties['Address']))

                    dev = self._connected_devices.pop(properties['Address'])
                    if dev.poll() is None:
                        dev.kill()
                        if dev.poll() is None:
                            log.warn('Unable to kill the audio routing application pid: %d' % dev.pid)

                    log.debug('Audio routing application ended with code %d' % dev.poll())
                    if dev.poll() != None and dev.poll() != 0:
                        log.warn('STDOUT: %s\n\nSTDERR: %s' % dev.communicate())

                    if len(self._connected_devices) < 1:
                        log.info('Disconnecting GPIO sound output')
                        self.signal('audio_switch', value = False)
