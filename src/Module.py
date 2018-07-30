#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import subprocess

import Log as log

class Module(object):
    """Module - basic module class"""

    def __init__(self, **kwargs):
        '''Module preparation'''
        self._control = kwargs.get('control')
        self._cfg = kwargs.get('config')
        self._active = False
        log.info('Initializing %s(%s)' % (self.__class__.__name__, self.name()))

    def name(self):
        '''Getting module instance name'''
        return self._cfg.get('name')

    def isActive(self):
        return self._active

    def wait(self):
        '''Waiting for complete initialization'''
        pass

    def deps(self):
        '''Get list of requirements for the module'''
        return []

    def start(self):
        '''Start the module initialization'''
        log.info('Starting %s(%s)' % (self.__class__.__name__, self.name()))
        self._active = True

    def postStart(self):
        '''Actions to do when all the modules was started'''
        log.info('PostStarting %s(%s)' % (self.__class__.__name__, self.name()))

    def stop(self):
        '''Shutdown the module operations'''
        log.info('Stopping %s(%s)' % (self.__class__.__name__, self.name()))
        self._active = False

    def waitActive(self, timeout):
        '''Wait till timeout or active state'''
        till = time.time() + timeout
        while self.isActive() and time.time() < till:
            time.sleep(0.1)

    def execCommand(self, cmd):
        return subprocess.Popen(cmd)

    def execCommandWait(self, cmd):
        ret = self.execCommand(cmd)
        try:
            while self.isActive() and ret.poll() == None:
                self.waitActive(0.5)
            if ret.poll() == None:
                ret.kill()
        except:
            pass
        finally:
            if ret.poll() != 0:
                log.error('Failed to execute command')
                log.debug('STDOUT: %s\n\nSTDERR: %s' % ret.communicate())

    def signal(self, signal, **kwargs):
        '''Send configured signal and execute defined function
        Signal could be a name in module configuration, a map with required socket info or array of such maps
        Will try to search the required instance by module or instance or will use self
        If function contains parameters from the kwargs - it will be added to execution params
        '''
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
                log.error('Wrong module instance: %s (signal: %s)' % (inst, s))
                continue # Wrong instance found

            func_name = s.get('socket')
            if hasattr(inst, func_name) and callable(getattr(inst, func_name)):
                func = getattr(inst, func_name)
                kwargs.update(s.get('parameters', {}))
                if len(kwargs):
                    params = { k:v for k,v in kwargs.iteritems() if k in func.func_code.co_varnames }
                    func(**params)
                else:
                    func()
            else:
                log.error('Unable to find module instance function to execute the signal: %s::%s' % (inst, func_name) )
