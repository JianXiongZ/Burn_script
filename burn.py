#!/usr/bin/env python2.7
import serial
import os
ser = serial.Serial("/dev/ttyUSB1", 9600, timeout=0.5)


def burn(serial_data):
    if serial_data == "0xa1":
        result = os.system('./burnmm.sh')
        if result is True:
            return '0x51'
        else:
            return '0x50'
    if serial_data == "0xa2":
        result = os.system('./burnmcu.sh')
        if result is True:
            return '0x51'
        else:
            return '0x50'
    else:
        pass


def writeserial(result):
    if result == "0x50":
        ser.write("0x50")
    if result == "0x51":
        ser.write("0x51")
    else:
        pass


def readserial():
    serial_data = ser.read(4)
    if len(serial_data) == 4:
        return serial_data
    else:
        pass
while(1):
    serial_data = readserial()
    result = burn(serial_data)
    writeserial(result)
