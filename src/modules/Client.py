#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time, threading
import urllib2, base64
import ssl
import zlib, json

import Log as log
from Module import Module

class Client(Module):
    '''Module to send logs and data to the remote server'''

    def __init__(self, **kwargs):
        Module.__init__(self, **kwargs)

        self._data = {}
        self._data_lock = threading.Lock()
        self._data_send_timer = None
        self._send_interval = None

    def _timerAlarm(self):
        self.sendData()
        self.resetTimer()

    def start(self):
        Module.start(self)
        self.setInterval()

    def stop(self):
        Module.stop(self)
        if self._data_send_timer:
            self._data_send_timer.cancel()
        self._data_send_timer = None
        self._send_interval = None
        self.sendData()

    def setInterval(self, value = None):
        prev = self._send_interval
        if (isinstance(value, int) or isinstance(value, float)) and value > 0:
            self._send_interval = value
        else:
            self._send_interval = self._cfg.get('interval', 30)

        if self._send_interval != prev:
            self.resetTimer()

    def resetTimer(self):
        if self._data_send_timer:
            self._data_send_timer.cancel()
        self._data_send_timer = threading.Timer(self._send_interval, self._timerAlarm)
        self._data_send_timer.start()

    def logData(self, sender, data):
        t = int(time.time() * 1000)
        with self._data_lock:
            self._data[sender] = self._data.get(sender, {})
            self._data[sender][t] = data

    def sendData(self):
        if not self._data:
            return

        log.debug('Start sending collected client data to the server (%s)' % ({ k:len(v) for k, v in self._data.iteritems() }))

        buf = None
        with self._data_lock:
            buf = self._data
            self._data = {}

        post_req = urllib2.Request(self._cfg.get('url'))

        # Preparing data
        data = json.dumps(buf, separators=(',',':'))

        compress = self._cfg.get('compress', 6)
        if isinstance(compress, int) and compress > 0:
            data = zlib.compress(data, compress)
            post_req.add_header('Content-Encoding', 'gzip')

        # Adding auth
        user = self._cfg.get('auth_user')
        password = self._cfg.get('auth_password')
        if user or password:
            post_req.add_header('Authorization', 'Basic ' + base64.b64encode(user+':'+password))

        post_req.add_data(data)

        # Setting SSL context
        ctx = ssl.create_default_context()
        ctx.check_hostname = self._cfg.get('ssl_check_hostname', True)
        if not self._cfg.get('ssl_verify', True):
            ctx.verify_mode = ssl.CERT_NONE

        response_json = {}
        try:
            response = urllib2.urlopen(post_req, context=ctx, timeout=120)
            response_data = response.read()
            response.close()
            try:
                response_json = json.loads(response_data)
            except Exception as e:
                response_json = {'result': 'local error', 'message': 'Uabled to parse response json: %s, http: %s %s' % (e, response.getcode(), response.info())}
        except Exception as e:
            response_json = {'result': 'local error', 'message': 'Request exception: %s' % e}

        if not response_json or response_json.get('result') != 'ok':
            log.warn('Unable to send data properly, will try next time: %s %s' % (response_json.get('result'), response_json.get('message')))
            with self._data_lock:
                for key in self._data:
                    if key in buf:
                        buf[key].update(self._data[key])
                    else:
                        buf[key] = self._data[key]
                self._data = buf
