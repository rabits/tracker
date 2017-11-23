#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time

import Log as log
from DataModule import DataModule

import Adafruit_ADS1x15

class ADS1115(DataModule):
    '''4xADC 16bit i2c module'''

    def getBusNumber(self):
        return self._cfg.get('i2c_bus', 1)

    def getAddress(self):
        return self._cfg.get('address', 0x48)

    def _readRawDataThread(self):
        log.info('Connecting to I2C bus %d device address 0x%02x' % (self.getBusNumber(), self.getAddress()))
        import smbus
        with Adafruit_ADS1x15.ADS1115(self.getAddress(), smbus.SMBus(self.getBusNumber())) as adc:

            # Warming up the sensor
            for j in range(5):
                { i:adc.read_adc(i, gain=self._map.get(i, {}).get('gain', 1)) for i in range(4) }
                time.sleep(0.2)

            # Actual loop to get the data
            while self._active:
                # Reading values from the sensor
                out = { i:adc.read_adc(i, gain=self._map.get(i, {}).get('gain', 1)) for i in range(4) }

                self._processData(out)

                time.sleep(self._cfg.get('update_timeout', 1))
