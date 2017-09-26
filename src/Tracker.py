#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''Tracker v0.1-alpha

Author:      Rabit <home@rabits.org>
License:     GPL v3
Description: Car tracker, bluetooth player & camera manager
Required:    python2.7, python-bluez, python-yaml, python-dbus
'''

import yaml
import sys, os
try:
    from gi.repository import GObject
except ImportError:
    import gobject as GObject
import dbus.mainloop.glib

import Log as log
from Bluetooth import Bluetooth

class Tracker(object):
    """Main application"""
    def __init__(self, config_path):
        self._mainloop = GObject.MainLoop()
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        self._processes = {}
        self._cfg_path = config_path
        self._loadConfig()
        self._checkConfig()

    def _loadConfig(self):
        self._cfg = None
        try:
            with open(os.path.abspath(os.path.expanduser(self._cfg_path)), 'rb') as f:
                self._cfg = yaml.load(f.read())
                log.info("Using configuration from '%s'" % f.name)
        except IOError:
            log.warn("Unable to read config file '%s'" % self._cfg_path)

        if self._cfg == None:
            raise Exception("Unable to read configuration")

    def _checkConfig(self):
        self._dir = {}
        for key in self._cfg.get('global', {}).get('dir', {}):
            self._dir[key] = os.path.abspath(os.path.expanduser(self._cfg.get('global')['dir'][key]))
            if not os.path.isdir(self._dir[key]):
                log.info("Make directory '%s'" % self._dir[key])
                os.makedirs(self._dir[key])
        if 'verbose' in self._cfg.get('global', {}).get('log', {}):
            log.logSetVerbose(self._cfg.get('global')['log']['verbose'])
            log.info("Set verbose mode to %s" % self._cfg.get('global')['log']['verbose'])

    def saveConfig(self):
        pass

    def _runProcesses(self, Class):
        name = Class.__name__
        self._processes[name] = []
        for i, cfg in enumerate(self._cfg.get(name, {})):
            self._processes[name].append(Class(control = self, config = cfg))

        log.info("Waiting till %s will be started..." % name)
        for proc in self._processes[name]:
            proc.wait()
        log.info("%s was started" % name)

    def _init(self):
        log.info('Initializing...')

        self._runProcesses(Bluetooth)

        log.info('Initialization done')

    def _setup(self):
        log.info('Startup setup...')

        log.info('Startup setup done')

    def _run(self):
        log.info('Running...')
        try:
            self._mainloop.run()
        except (KeyboardInterrupt, SystemExit):
            log.info('Received stop signal')
        except:
            log.error('Abnormal stop...')
            self.stop()
            raise
        finally:
            self._stop()

    def run(self):
        try:
            self._init()
            self._setup()
        except:
            log.error('Something went wrong...')
            self._stop()
            raise

        self._run()

    def _stopProcesses(self, Class):
        if type(Class) == str:
            name = Class
        else:
            name = Class.__name__

        if name in self._processes:
            for proc in self._processes[name]:
                proc.stop()
            for i in range(len(self._processes[name])):
                del self._processes[name][-1]

            del self._processes[name]

    def stop(self):
        log.info("Stopping processes...")
        self._mainloop.quit()

    def _stop(self):
        self._stopProcesses(Bluetooth)

        # Stopping last processes
        for name in self._processes.keys():
            self._stopProcesses(name)

    def version(self):
        return __doc__.split()[1][1:]

if __name__ == '__main__':
    if os.geteuid() == 0:
        log.error('Script is running by the root user - it is really dangerous! Please use unprivileged user')
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: tracker <config.yaml>")
        log.error("No config file argument found")
        sys.exit(1)
    onebutton = Tracker(sys.argv[1])

    onebutton.run()

    log.info("Exiting...")
    sys.exit(0)
