#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time

import Log as log
from DataModule import DataModule

import subfact_pi_ina219

class FileSimpleSensor(DataModule):
    '''Simple float data from file'''

    def getPath(self):
        return self._cfg.get('paths', [])

    def _readRawDataThread(self):
        while self._active:
            # Reading values from files
            out = {}
            for i, path in enumerate(self.getPath()):
                with open(path, 'r') as f:
                    out[i] = float(f.read())

            self._processData(out)

            time.sleep(self._cfg.get('update_delay', 1))
