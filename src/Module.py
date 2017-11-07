#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import Log as log

class Module(object):
    """Module - basic module class"""

    def __init__(self, **kwargs):
        '''Module preparation'''
        log.info("Initializing %s instance" % self.__class__.__name__)
        self._control = kwargs.get('control')
        self._cfg = kwargs.get('config')

    def name(self):
        '''Getting module instance name'''
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

    def signal(self, signal):
        '''Send configured signal and execute defined function
        Signal could be a name in the configuration or a map with required socket info
        Will try to search the required instance by module or instance or will use self'''
        if isinstance(signal, str):
            signal = self._cfg.get('signals', {}).get(signal)
        if not signal:
            return # Skipping if no signal configuration is defined

        inst = self
        req = { 'module': signal.get('module'), 'instance': signal.get('instance') }
        if isinstance(req['module'], str) or isinstance(req['instance'], str):
            inst = self._control.getModuleInstance(**req)

        if not isinstance(inst, Module):
            log.error("Found module instance is not a module: %s (signal: %s)" % (inst, signal))
            return # Wrong instance found

        func = signal.get('socket')
        if hasattr(inst, func) and callable(getattr(inst, func)):
            return getattr(inst, func)(inst)
        else:
            log.error("Unable to find module instance function to execute signal: %s::%s" % (inst, func) )
