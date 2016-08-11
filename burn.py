#!/usr/bin/env python2.7
from sys import argv
script, serial_data = argv


def Burn(serial_data):
    if serial_data == "0xa1":
        print "fpga"
        if True:
            return '0x51'
        else:
            return '0x50'
    if serial_data == "0xa2":
        print "flash"
        if True:
            return '0x51'
        else:
            return '0x50'
    else:
        print "No argvment."
result = Burn(serial_data)
print result
