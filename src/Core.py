#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''Tracker v0.5.2-alpha

Author:      Rabit <home@rabits.org>
License:     GPL v3
Description: Car tracker, bluetooth player & camera manager
'''

import yaml, string
import sys, os
from importlib import import_module
try:
    from gi.repository import GObject
except ImportError:
    import gobject as GObject
import dbus.mainloop.glib

import Log as log

class Core(object):
    """Main control application"""
    def __init__(self, config_path):
        self._mainloop = GObject.MainLoop()
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        self._modules = {}
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
        if 'verbose' in self._cfg.get('Core', {}).get('log', {}):
            log.logSetVerbose(self._cfg.get('Core')['log']['verbose'])
            log.info("Set verbose mode to %s" % self._cfg.get('Core')['log']['verbose'])

    def saveConfig(self):
        pass

    def _startModules(self, name):
        self._modules[name] = []
        for cfg in self._cfg.get(name, {}):
            if cfg.get('enabled', True):
                log.debug('Starting module %s(%s)' % (name, cfg.get('name')))
                module = import_module('modules.%s' % name)
                self._modules[name].append(getattr(module, name)(control = self, config = cfg))
            else:
                log.info('Skipping starting disabled module %s(%s)' % (name, cfg.get('name')))

        for module in self._modules[name]:
            module.start()

        log.info("Waiting till %s will be started..." % name)
        for module in self._modules[name]:
            module.wait()

        log.info("%s was started" % name)

    def _postStartModules(self):
        for name in self._modules:
            for module in self._modules[name]:
                module.postStart()

    def _init(self):
        log.info('Initializing...')

        # Processing uppercase configurations as modules
        # TODO: dependent module starting
        for module in [ name for name in self._cfg.keys() if name != 'Core' and name[0] in string.ascii_uppercase ]:
            self._startModules(module)

        self._postStartModules()

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
        except Exception as e:
            log.error('Something went wrong: %s' % e)
            self._stop()
            raise

        self._run()

    def _stopModules(self, name):
        if name in self._modules:
            for module in self._modules[name]:
                module.stop()
            for i in range(len(self._modules[name])):
                del self._modules[name][-1]

            del self._modules[name]

    def stop(self):
        log.info("Stopping modules...")
        self._mainloop.quit()

    def _stop(self):
        # Stopping last modules
        # TODO: dependent module stopping
        for name in self._modules.keys():
            self._stopModules(name)

    def version(self):
        return __doc__.split()[1][1:]

    def getModuleInstance(self, module = None, instance = None):
        """Find required module instance and return it
        If there is just instance - will search all the modules
        If there is just module - will return first one"""
        out = []
        modules = self._modules.keys()

        if isinstance(module, str):
            if module in modules:
                modules = [module]
            else:
                log.error("Not found required module: %s" % module)
                return None

        for mod in modules:
            if isinstance(instance, str):
                out += [ (inst, mod, inst.name()) for inst in self._modules[mod] if inst.name() == instance ]
            else:
                out += [ (self._modules[mod][0], mod, self._modules[mod][0].name()) ]

        if len(out) != 1:
            log.error('Not found just one module instances: %s' % out)
            return None

        return out.pop()[0]


if __name__ == '__main__':
    if os.geteuid() == 0:
        log.error('Script is running by the root user - it is really dangerous! Please use unprivileged user')
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: tracker <config.yaml>")
        log.error("No config file argument found")
        sys.exit(1)
    onebutton = Core(sys.argv[1])

    onebutton.run()

    log.info("Exiting...")
    sys.exit(0)
