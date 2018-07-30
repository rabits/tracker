#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import threading
import serial

import Log as log
from DataModule import DataModule

class ALDL160(DataModule):
    '''ALDL 160 baud car debug interface module'''

    # 160 baud on 9600 each bit will be a byte. '00000000' is '1', anything else - '0'
    _ONE = chr(0x0)

    def getDevice(self):
        return self._cfg.get('dev', None)

    def getRate(self):
        return self._cfg.get('rate', 9600)

    def _readRawDataThread(self):
        log.info('Connecting to the ALDL device %s with rate %s' % (self.getDevice(), self.getRate()))
        with serial.Serial(self.getDevice(), self.getRate(), timeout=5.0) as c:
            data = '010101010010101010'
            in_sync = False
            out = {} # Prepared byte data for current frame

            while self.isActive():
                raw = c.read(9)
                data = data[len(raw):] + ''.join([ '1' if b == self._ONE else '0' for b in raw ])
                if len(raw) != 9:
                    if in_sync:
                        log.warn('Lost sync while reading last %d bits of data: %s' % (len(raw), data))
                    in_sync = False

                if not in_sync:
                    # Searching for a sync sequence "111111111" - beginning of the frame
                    pos = data.find('111111111')
                    if pos < 0: # Sync not found in the data
                        continue

                    if pos > 0: # Sync is found and we need to complete to read the next 9-byte sequence
                        raw = c.read(pos)
                        data = data[len(raw):] + ''.join([ '1' if b == self._ONE else '0' for b in raw ])
                        if len(raw) != pos: # No luck - let's try next time
                            continue
                        in_sync = True

                if in_sync:
                    if data[9] == '0': # Data byte
                        out[len(out)] = int(data[10:], 2)
                    elif data[9:] == '111111111': # New frame started
                        log.debug('Received frame, updating data')
                        to_update = []

                        self._processData(out)

                        out = {}
                    else: # Sync failed
                        in_sync = False
                        log.warn('Found wrong sync bit while parsing last 9 bits of data: %s, processed out: %s' % (data, out))
                        out = {}
