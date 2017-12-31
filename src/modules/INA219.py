#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time

import Log as log
from DataModule import DataModule

import subfact_pi_ina219

class INA219(DataModule):
    '''Current, Voltage & Power sensor i2c module'''

    def getBusNumber(self):
        return self._cfg.get('i2c_bus', 1)

    def getAddress(self):
        return self._cfg.get('address', 0x40)

    def _readRawDataThread(self):
        log.info('Connecting to I2C bus %d device address 0x%02x' % (self.getBusNumber(), self.getAddress()))
        import smbus
        with subfact_pi_ina219.INA219(self.getAddress(), smbus.SMBus(self.getBusNumber())) as ina:
            while self._active:
                # Reading values from the sensor
                out = {
                    0: ina.getBusVoltageV(),
                    1: ina.getCurrentA(),
                    2: ina.getPowerW(),
                    3: ina.getShuntVoltageV()
                }

                self._processData(out)

                time.sleep(self._cfg.get('update_timeout', 1))
