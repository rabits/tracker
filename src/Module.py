#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import Log as log

class Module(object):
    """Module - basic module class"""

    def __init__(self, **kwargs):
        '''Module preparation'''
        self._control = kwargs.get('control')
        self._cfg = kwargs.get('config')
        log.info('Initializing %s instance %s' % (self.__class__.__name__, self.name()))

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
        log.info('Starting %s instance %s' % (self.__class__.__name__, self.name()))

    def postStart(self):
        '''Actions to do when all the modules was started'''
        log.info('PostStarting %s instance %s' % (self.__class__.__name__, self.name()))

    def stop(self):
        '''Shutdown the module operations'''
        log.info('Stopping %s instance %s' % (self.__class__.__name__, self.name()))

    def signal(self, signal, **kwargs):
        '''Send configured signal and execute defined function
        Signal could be a name in module configuration, a map with required socket info or array of such maps
        Will try to search the required instance by module or instance or will use self
        If fynction contains parameters from the kwargs - it will be added to execution params'''
        if isinstance(signal, str):
            signal = self._cfg.get('signals', {}).get(signal)
        if not signal:
            return # Skipping if no signal configuration is defined

        if not isinstance(signal, list):
            signal = [signal]

        for s in signal:
            inst = self
            req = { 'module': s.get('module'), 'instance': s.get('instance') }
            if isinstance(req['module'], str) or isinstance(req['instance'], str):
                inst = self._control.getModuleInstance(**req)

            if not isinstance(inst, Module):
                log.error('Found module instance is not a module: %s (signal: %s)' % (inst, s))
                return # Wrong instance found

            func_name = s.get('socket')
            if hasattr(inst, func_name) and callable(getattr(inst, func_name)):
                func = getattr(inst, func_name)
                kwargs.update(s.get('parameters', {}))
                if len(kwargs):
                    params = { k:v for k,v in kwargs.iteritems() if k in func.func_code.co_varnames }
                    return func(**params)
                return func()
            else:
                log.error('Unable to find module instance function to execute the signal: %s::%s' % (inst, func_name) )
