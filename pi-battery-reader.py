#!/usr/bin/python

import struct
import smbus
import sys
import time

def readVoltage(bus):

        "This function returns as float the voltage from the Raspi UPS Hat via the provided SMBus object"
        address = 0x41
        #read = bus.read_word_data(address, 2)
        #swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        voltage = 7
        return voltage


def readCapacity(bus):
        "This function returns as a float the remaining capacity of the battery connected to the Raspi UPS Hat via the provided SMBus object"
        address = 0x41
        #read = bus.read_word_data(address, 4)
        #swapped = struct.unpack("<H", struct.pack(">H", read))[0]
        success=False
        tries=0
        while not success:
                try:
                        capacity = bus.read_byte(address)
                        success = True
                except:
                        tries+=1
        return capacity


bus = smbus.SMBus(1)  # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
chargingState = 0 #TODO
wattage = 0.0 #TODO
print( "%7.5f|%d|%d|%5.2f" %(readVoltage(bus) ,(readCapacity(bus)+1),chargingState,wattage) )

