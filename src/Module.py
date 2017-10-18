#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import Log as log

class Module(object):
    """Module - basic module class"""

    def __init__(self, **kwargs):
        self._control = kwargs.get('control')
        self._cfg = kwargs.get('config')

    def name(self):
        return self._cfg.get('name')

    def wait(self):
        '''Waiting for complete initialization'''
        pass

    def deps(self):
        '''Get list of requirements for the module'''
        return []

    def start(self):
        '''Start the module initialization'''
        log.info("Starting %s instance" % self.__class__.__name__)

    def stop(self):
        '''Shutdown the module operations'''
        log.info("Stopping %s instance" % self.__class__.__name__)

    def signal(self, name):
        '''Send configured signal and execute defined function
        Will try to search the required instance by module or instance or will use self'''
        sig = self._cfg.get('signals', {}).get(name)
        if not sig:
            return # Skipping if no signal defined in the configuration

        inst = self
        req = { 'module': sig.get('module'), 'instance': sig.get('instance') }
        if isinstance(req['module'], str) or isinstance(req['instance'], str):
            inst = self._control.getModuleInstance(**req)

        if not isinstance(inst, Module):
            log.error("Found module instance is not a module: %s (signal: %s)" % (inst, name))
            return # Wrong instance found

        func = sig.get('socket', name)
        if hasattr(inst, func) and callable(getattr(inst, func)):
            return getattr(inst, func)(inst)
        else:
            log.error("Unable to find module instance function to execute signal: %s::%s" % (inst, func) )
