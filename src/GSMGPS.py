#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import serial

import Log as log
from Module import Module

class GSMGPS(Module):
    '''GSM & GPS module interface'''

    _SUPPORTED = [
        'SIMCOM_SIM5320A'
    ]

    def __init__(self, **kwargs):
        Module.__init__(self, **kwargs)

        self.setDevice(self._cfg.get('dev', False))
        self.setRate(self._cfg.get('rate', 115200))

        self._c = None

    def start(self):
        Module.start(self)
        self._c = serial.Serial(self.getDevice(), self.getRate(), timeout=1.0)
        # Disabling echo
        self.execAT('ATE0')

        # Check the device before running
        if self.checkVersion() != True:
            log.error('Unable to run GSMGPS module due to device version is unsupported: %s' % self.checkVersion())
            self.stop()

        if self._cfg.get('net', {}).get('enabled', False):
            self.enableNetwork()

        if self._cfg.get('gps', {}).get('enabled', False):
            self.enableGPS()

    def stop(self):
        if self._c:
            self._c.close()

    def powerOn(self):
        log.info('Power on the GSMGPS chip %s' % self.name())
        self.signal('power_on')
        # Waiting for init done
        self.execAT('AT', '+CPIN: READY')

    def powerOff(self):
        log.info('Power off the GSMGPS chip %s' % self.name())
        self.execAT('AT+CPOF', '+STIN:')

    def execAT(self, cmd, return_begins = None, msg_ok = 'OK', msg_err = 'ERROR'):
        '''Will execute command & read output till OK and return_begins filtered
        If there is error - will return False immediately
        If no return filter is set - will return command success'''

        command_done = False

        out = None
        out_num = 0
        if return_begins == None:
            pass
        elif isinstance(return_begins, str):
            # Found values will be stored in list
            out = []
            out_num = 1
        elif isinstance(return_begins, list):
            # Found values will be stored in map
            out = { key:[] for key in return_begins }
            out_num = len(return_begins)
        else:
            log.error('Unsupported return filter for execute AT command: %s' % (return_begins))
            return_begins = None

        self._c.write(cmd+'\r')

        while not command_done or len(out) < out_num:
            data = self._c.readline().rstrip()
            if data == msg_ok:
                command_done = True
            elif data == msg_err:
                return False
            elif isinstance(return_begins, str):
                # Adding data to output only if filter is ok
                if data.startswith(return_begins):
                    out.append(data[len(return_begins):].strip())
                    out_flag = False
            elif isinstance(return_begins, list):
                # Searching across the known keys
                for key in return_begins:
                    if data.startswith(key):
                        out[key].append(data[len(key):].strip())
                        out_flag = False

        return out if out else command_done

    def checkVersion(self):
        '''Checking chip verision to be supported'''
        model = self.callGetInfo().get('Model:')
        if model in self._SUPPORTED:
            return True

        return model

    def enableNetwork(self):
        '''Configuring & enabling networking'''
        # Check current state to process
        self.callSignalQuality()[0] > 0 # it should be better than -113 dBm
        self.callNetworkRegistration()[1] in [1,5] # Registered, home or roaming
        self.callConnectionInfo()[1] == 'Online' # Connection established
        self.callGPRSNetworkRegistration()[1] in [1,5] # GPRS registered, home or roaming

        # Configuring networking
        self.callSetAPN()
        self.callSetAPNAuth()

        # Opening network connection
        self.callNetworkOpen()

    def disableNetwork(self):
        self.callNetworkClose()

    def enableGPS(self):
        # Configure AGPS if existing
        self.callSetAGPS()
        self.callEnableGPS()

    def disableGPS(self):
        self.callDisableGPS()

    def callSetAPN(self):
        '''AT+CGCONT=1,"IP","Broadband"
        OK'''
        return self.execAT('AT+CGCONT=1,"IP","%s"' % self._cfg.get('net', {}).get('apn', ''))

    def callSetSockAPN(self):
        '''AT+CGSOCKCONT=1,"IP","Broadband"
        OK'''
        return self.execAT('AT+CGSOCKCONT=1,"IP","%s"' % self._cfg.get('net', {}).get('apn', ''))

    def callNetworkOpen(self):
        '''AT+NETOPEN
        OK

        +NETOPEN: 0'''
        return self.execAT('AT+NETOPEN', '+NETOPEN:')

    def callSendHTTPSRequest(self, url):

    def callNetworkClose(self):
        '''AT+NETCLOSE
        OK

        +NETCLOSE: 0'''
        return self.execAT('AT+NETCLOSE', '+NETCLOSE:')

    def callGetIP(self):
        '''AT+IPADDR
        +IPADDR: 10.235.141.11

        OK'''
        return self.execAT('AT+IPADDR', '+IPADDR:')

    def callEnableGPS(self):
        '''AT+CGPS=1,2
        OK'''
        mode = 2 if self._cfg.get('gps', {}).get('agps', False) else 1
        return self.execAT('AT+CGPS=1,%d' % mode)

    def callDisableGPS(self):
        '''AT+CGPS=0
        OK'''
        return self.execAT('AT+CGPS=0')

    def callSetAGPS(self):
        '''AT+CGPSURL="supl.google.com:7276"
        OK'''
        url = self._cfg.get('gps', {}).get('agps')
        if url:
            return self.execAT('AT+CGPSURL="%s"' % url)
        return None

    def callGetGPS(self):
        '''AT+CGPSINFO
        +CGPSINFO:3734.035426,N,12158.143130,W,121017,040558.6,-15.3,0.0,0

        AmpI/AmpQ: 1057/1057

        OK'''
        def _convertGPSCoord(coord, direction):
            coord = float(coord)
            out = int(coord/100)
            out += (coord - lat*100)/60
            return out if direction in ['N','E'] else -out

        data = self.execAT('AT+CGPSINFO', '+CGPSINFO:')
        if not data or data[0] == ',,,,,,,,':
            log.error('Unable to get response from GPS')
            return (None. None, None, None, None, None, None)

        data = data[0].split(',')
        lat = _convertGPSCoord(data[0], data[1]) # Decimal degrees
        lon = _convertGPSCoord(data[2], data[3]) # Decimal degrees
        date = data[4] # ddmmyy
        time = data[5] # UTC hhmmss.s
        alt = float(data[6]) # Meters
        speed = float(data[7]) * 0.51444444444 # Meters / second
        course = float(data[8]) # Degrees
        return (lat, lon, date, time, alt, speed, course)

    def callGetInfo(self):
        '''ATI
        Manufacturer: SIMCOM INCORPORATED
        Model: SIMCOM_SIM5320A
        Revision: SIM5320A_V1.5
        IMEI: 014682001954535
        +GCAP: +CGSM,+DS,+ES

        OK'''
        return execAT('ATI', ['Manufacturer:', 'Model:','Revision:', 'IMEI:'])

    def callSignalQuality(self):
        '''AT+CSQ
        +CSQ: 13,99

        OK'''
        data = self.execAT('AT+CSQ', '+CSQ:')
        if not data:
            return (None, None)
        return [ int(d) for d in data.split(',') ]

    def callNetworkRegistration(self):
        '''AT+CREG?
        +CREG: 0,1

        OK'''
        data = self.execAT('AT+CREG?', '+CREG:')
        if not data:
            return (None, None)
        return [ int(d) for d in data.split(',') ]

    def callGetOperator(self):
        '''AT+COPS?
        +COPS: 0,0,"AT&T",2

        OK'''
        data = self.execAT('AT+COPS?', '+COPS:').split(',')
        if not data:
            return (None, None, None, None)
        mode = data[0]

    def callConnectionInfo(self):
        '''AT+CPSI?
        +CPSI: WCDMA,Online,310-410,0xDE8B,3846084,WCDMA 850,355,4385,0,4.5,78,39,37,500

        OK'''

    def callGetNetworkMode(self):
        '''AT*CNTI?
        *CNTI: 0,HSDPA

        OK'''

    def callGetBatteryStatus(self):
        '''AT+CBC
        +CBC: 0,62,3.837V

        OK'''

    def runPPPD(self):
        '''sudo pppd /dev/ttyS0 115200 nodetach crtscts debug persist maxfail 0 noauth persist user '' password '' connect 'echo "ATD*99#\r" > /dev/ttyS0' noccp defaultroute replacedefaultroute'''
