#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import threading

import Log as log
from Module import Module

class Power(Module):
    '''Actions for power events'''

    def __init__(self, **kwargs):
        Module.__init__(self, **kwargs)

        self._ignition = None
        self._ignition_lock = threading.Lock()
        self._ignition_off_timer = None

        self._power_outage = None
        self._critical_battery_voltage = None
        self._low_battery_voltage = None

    def start(self):
        Module.start(self)

    def stop(self):
        Module.stop(self)

    def getIgnitionOffTimeout(self):
        return self._cfg.get('ignition_off_timeout', 30)

    def ignition(self, value = None):
        if value == None: # Acting like switch
            value = not self._ignition

        if self._ignition_off_timer != None:
            self._ignition_off_timer.cancel()

        if self._ignition == value:
            return

        if value:
            log.info('Ignition started')
            with self._ignition_lock:
                self._ignition = True
            self.signal('ignition_on')
        else:
            log.debug('Ignition stop timer started')
            self._ignition_off_timer = threading.Timer(self.getIgnitionOffTimeout(), self._ignition_off)
            self._ignition_off_timer.start()

    def _ignition_off(self):
        log.info('Ignition stopped for %s seconds' % self.getIgnitionOffTimeout())
        with self._ignition_lock:
            self._ignition = False
        self.signal('ignition_off')

    def powerOutage(self, value = None):
        if value == None: # Acting like switch
            value = not self._power_outage
        elif self._power_outage == value:
            return

        self._power_outage = value
        if value:
            log.warn('Power outage detected')
            self.signal('power_outage_raise')
        else:
            log.warn('Power returned after the outage')
            self.signal('power_outage_drop')

    def criticalBatteryVoltage(self, value = None):
        if value == None: # Acting like switch
            value = not self._critical_battery_voltage
        elif self._critical_battery_voltage == value:
            return

        self._critical_battery_voltage = value
        if value:
            log.warn('Battery voltage riched critical voltage')
            self.signal('critical_voltage_raise')
        else:
            log.info('Battery voltage is not critical now')
            self.signal('critical_voltage_drop')

    def lowBatteryVoltage(self, value = None):
        if value == None: # Acting like switch
            value = not self._low_battery_voltage
        elif self._low_battery_voltage != value:
            return

        self._low_battery_voltage = value
        if value:
            log.warn('Battery voltage riched low voltage')
            self.signal('low_voltage_raise')
        else:
            log.info('Battery restored normal voltage')
            self.signal('low_voltage_drop')
