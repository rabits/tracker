#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import threading
import time

import Log as log
from Module import Module
from Library import mapValue, mergeDicts, evaluateMath

class DataModule(Module):
    """DataModule - common data sensors functions"""

    def __init__(self, **kwargs):
        Module.__init__(self, **kwargs)

        self._active = False
        self._raw_data = {}
        self._raw_data_lock = threading.Lock()
        self._map_data = {}
        self._map_data_lock = threading.Lock()

        self._thread_control = threading.Thread(target=self._readRawDataThreadWrapper)

    def start(self):
        Module.start(self)
        self._reinitMap()
        self._active = True
        if not self._thread_control.is_alive():
            self._thread_control.start()

    def stop(self):
        Module.stop(self)
        self._active = False

    def _reinitMap(self):
        self._map = self._cfg.get('map', {})

        # Converting list to dict to use the same interface
        if isinstance(self._map, list):
            self._map = { i:v for i,v in enumerate(self._map) }
        elif not isinstance(self._map, dict):
            self._map = {}
            log.error('Wrong map format in %s(%s)' % (self.__class__.__name__, self.name()))

    def _readRawDataThreadWrapper(self):
        '''This wrapper is required to run prepare & cleaning operations for the read thread'''
        try:
            log.debug('%s %s reading thread started' % (self.__class__.__name__, self.name()))
            self._readRawDataThread()
        finally:
            log.debug('%s %s reading thread completed' % (self.__class__.__name__, self.name()))
            self._cleanData()

    def _readRawDataThread(self):
        '''Thread function to get & update values of the collected data'''
        log.error('Issue with %s(%s) DataModule implementation, it should override the _readRawDataThread function' % (self.__class__.__name__, self.name()))

    def _processData(self, data):
        '''Helper to update _raw_data and _map_data and trigger required signals'''
        # Determining changes
        to_update = []
        for i, val in data.iteritems():
            if self._raw_data.get(i, None) != val:
                to_update.append(i)
                if not self._map:
                    log.debug('Raw data value %d changed: %s to %s' % (i, self._raw_data.get(i), val))

        # Atomic update the raw data
        with self._raw_data_lock:
            for i in to_update:
                self._raw_data[i] = data[i]

        # Mapping raw data by provided map
        if self._map:
            mdata = {}
            for i in to_update:
                mdata.update(mapValue(i, data, self._map, self._map_data))

            changes = {}
            with self._map_data_lock:
                changes = mergeDicts(self._map_data, mdata)
            changes = self._processChanged(changes, self._map, self._map_data)
            if changes:
                self.signal('changes', sender=self.name(), data=changes)
        elif to_update:
            self.signal('changes', sender=self.name(), data={k:v for k,v in data.iteritems() if k in to_update})

    def _processChanged(self, changes, data_map, data):
        '''Function will execute required signals based on changes data'''
        out = {}
        for key in changes:
            if not data_map.get(key, {}).get('enabled', True):
                continue

            if isinstance(changes[key], dict):
                log.debug('- %s(%s) changes: %s:' % (self.__class__.__name__, self.name(), key))
                out[key] = self._processChanged(changes[key], data_map.get(key, {}), data.get(key, {}))
                continue

            log.debug('- %s(%s) changes: %s = %s (%s)' % (self.__class__.__name__, self.name(), key, data.get(key), changes.get(key)))
            out[key] = changes[key]

            signals = data_map.get(key, {}).get('signals', [])
            for s in signals:
                if s.has_key('when') and not evaluateMath(s.get('when'), data.get(key), changes.get(name, s.get('default_value', 0))):
                    continue
                self.signal(s)
        return out

    def _cleanData(self):
        '''Will clean all the data when module is inactive'''
        log.debug('Deactivation - cleaning data')
        self._active = False
        with self._raw_data_lock:
            self._raw_data = {}
        with self._map_data_lock:
            self._map_data = {}

    def getRawDataValue(self, index):
        with self._raw_data_lock:
            return self._raw_data.get(index, None)

    def _waitActive(self, timeout):
        till = time.time() + timeout
        while self._active and time.time() < till:
            time.sleep(0.2)
