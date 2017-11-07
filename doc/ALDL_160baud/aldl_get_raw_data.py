#!/usr/bin/env python

import serial

with serial.Serial('/dev/ttyUSB0', 9600, timeout=5) as ser:
    while True:
        data = ser.read(160)
        out = ''
        for i in data:
            # On 9600 baud we will get that each original bit is converted to a byte, where 1 is '00000000' and 0 is '11111000'
            # Yeah, according to the ALDL documentation actually low is 1 and high is 0
            out += '1' if i == chr(0) else '0'
        print out
