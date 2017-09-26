#!/usr/bin/python

from __future__ import absolute_import, print_function, unicode_literals

import os
import dbus, dbus.service, dbus.mainloop.glib
import gobject as GObject

BUS_NAME = 'org.bluez'
AGENT_INTERFACE = BUS_NAME+'.Agent1'
DEVICE_INTERFACE = BUS_NAME+'.Device1'
MEDIA_INTERFACE = BUS_NAME+'.MediaControl1'

bus = None

def device_property_changed_cb(property_name, value, path, interface, device_path):
    if property_name != MEDIA_INTERFACE:
        return

    print("Getting dbus interface for device: %s interface: %s property_name: %s" % (device_path, interface, property_name))

    device = dbus.Interface(bus.get_object(BUS_NAME, device_path), interface)
    properties = device.GetAll(MEDIA_INTERFACE)
    properties_device = device.GetAll(DEVICE_INTERFACE)

    if properties["Connected"]:
        print("Device: %s has connected %s" % (properties_device['Name'], properties_device['Address']))
        cmd = "bluealsa-aplay '%s'" % properties_device['Address']
        print("Running cmd: %s" % cmd)
        os.system(cmd)
    else:
        print("Device: %s has disconnected %s" % (properties_device['Name'], properties_device['Address']))

def set_trusted(path):
    props = dbus.Interface(bus.get_object(BUS_NAME, path), "org.freedesktop.DBus.Properties")
    props.Set(BUS_NAME+".Device1", "Trusted", True)

class Agent(dbus.service.Object):
    exit_on_release = True

    def set_exit_on_release(self, exit_on_release):
        self.exit_on_release = exit_on_release

    @dbus.service.method(AGENT_INTERFACE, in_signature="", out_signature="")
    def Release(self):
        print("Release")
        if self.exit_on_release:
            mainloop.quit()

    @dbus.service.method(AGENT_INTERFACE, in_signature="", out_signature="")
    def Cancel(self):
        print("Cancel")

    @dbus.service.method(AGENT_INTERFACE, in_signature="o", out_signature="s")
    def RequestPinCode(self, device):
        print("RequestPinCode (%s)" % (device))
        set_trusted(device)
        return "1234a5678"

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    capability = "NoInputNoOutput"

    path = "/test/agent"
    agent = Agent(bus, path)
    obj = bus.get_object(BUS_NAME, "/org/bluez");
    manager = dbus.Interface(obj, BUS_NAME+".AgentManager1")
    manager.RegisterAgent(path, capability)

    print("Agent registered")
    manager.RequestDefaultAgent(path)

    print("Listening for signals on the bus...")
    bus.add_signal_receiver(device_property_changed_cb, bus_name=BUS_NAME, signal_name="PropertiesChanged", path_keyword="device_path", interface_keyword="interface")

    try:
        mainloop = GObject.MainLoop()
        mainloop.run()
    except KeyboardInterrupt:
        pass

    manager.UnregisterAgent(path)
    print("Agent unregistered")
