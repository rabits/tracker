#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import Log as log
from DataModule import DataModule

class FileSimpleSensor(DataModule):
    '''Simple float data from file'''

    def getPath(self):
        return self._cfg.get('paths', [])

    def _readRawDataThread(self):
        while self.isActive():
            # Reading values from files
            out = {}
            for i, path in enumerate(self.getPath()):
                with open(path, 'r') as f:
                    out[i] = float(f.read())

            self._processData(out)

            self.waitActive(self._cfg.get('update_delay', 1))
