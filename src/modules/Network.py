#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket
import threading

import Log as log
from Module import Module

class Network(Module):
    '''Workarounds to establish network connection'''

    def __init__(self, **kwargs):
        Module.__init__(self, **kwargs)

        self._thread_control = threading.Thread(target=self._restartNetworkOnNoConnection)

    def start(self):
        Module.start(self)

    def stop(self):
        Module.stop(self)

    def pingPort(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        try:
            return sock.connect_ex((host, port)) == 0
        finally:
            sock.close()

    def restartNetworkService(self):
        log.warn('Restarting networking service...')
        self.execCommandWait(['sudo', 'service', 'networking', 'stop'])
        self.waitActive(5.0)
        self.execCommandWait(['sudo', 'service', 'networking', 'start'])
        log.info('Networking restarted')

    def restartNetworkOnNoConnection(self):
        if not self._thread_control.is_alive():
            self._thread_control.start()

    def _restartNetworkOnNoConnection(self):
        for r in range(self._cfg.get('restart_retries', 3)):
            for i in range(self._cfg.get('ping_retries', 3)):
                log.debug('Trying network connection (%d-%d)' % (r, i))
                if self.pingPort(self._cfg.get('ping_host', 'google.com'), self._cfg.get('ping_port', 80)):
                    log.debug('Connection is existing - no more retries')
                    return
                self.waitActive(2.0)
            self.restartNetworkService()
