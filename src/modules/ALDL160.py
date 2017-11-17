#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import threading
import serial

import Log as log
from Module import Module

class ALDL160(Module):
    '''ALDL 160 baud car debug interface module'''
    def __init__(self, **kwargs):
        Module.__init__(self, **kwargs)

        self._active = False
        self._data = []
        self._data_lock = threading.Lock()

        # 160 baud on 9600 each bit will be a byte. '00000000' is '1', anything else - '0'
        self._ONE = chr(0x0)

        self._thread = threading.Thread(target=self.thread)

    def getDevice(self):
        return self._cfg.get('dev', None)

    def getRate(self):
        return self._cfg.get('rate', 9600)

    def getDataByte(self, byten):
        with self._data_lock:
            if len(self._data) > byten:
                return self._data[byten]
        return None

    def getDataBit(self, byten, bitn):
        mask = 2**bitn
        return (self.getDataByte(byten) & mask) == mask

    def thread(self):
        log.info('Connecting to the ALDL device %s with rate %s' % (self.getDevice(), self.getRate()))
        with serial.Serial(self.getDevice(), self.getRate(), timeout=5.0) as c:
            data = '010101010010101010'
            in_sync = False
            out = [] # Prepared byte data for current frame

            while self._active:
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
                        out.append(int(data[10:], 2))
                    elif data[9:] == '111111111': # New frame started
                        log.debug('Received frame, updating data')
                        # Processing output to compare with current data
                        if len(out) > len(self._data): # Safe reading
                            with self._data_lock:
                                self._data += [None] * (len(out) - len(self._data))
                        for i, byte in enumerate(out):
                            if self._data[i] != byte: # Safe reading
                                prev_byte = self._data[i] if self._data[i] is None else '0b'+format(self._data[i], '08b')
                                log.debug('Data byte 0x%s changed: %s to 0b%s' % (format(i, '02x'), prev_byte, format(byte, '08b')))
                                with self._data_lock:
                                    self._data[i] = byte
                        out = []
                    else: # Sync failed
                        in_sync = False
                        log.warn('Found wrong sync bit while parsing last 9 bits of data: %s, processed out: %s' % (data, out))
                        out = []

            log.info('Deactivation - cleaning data')
            with self._data_lock:
                self._data = []

            log.info('ALDL reading thread completed')

    def start(self):
        Module.start(self)
        self._active = True
        self._thread.start()

    def stop(self):
        Module.stop(self)
        self._active = False
