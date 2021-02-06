import time
#import _bleio
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

#https://github.com/adafruit/Adafruit_CircuitPython_BLE

radio = BLERadio()
print("scanning")
found = set()
found_addresses = set()

ble = radio

#mac_addr = "70:80:9E:48:44:32"
#mac_addr = "54:26:81:E2:FC:F0"
mac_addr = "24:0A:C4:32:36:2E" #esp

def scan():
    for entry in radio.start_scan(timeout=5, minimum_rssi=-120):
        addr = entry.address
        if addr not in found_addresses:
            print(entry)        
            print(addr.string)
            found.add(entry)
            found_addresses.add(addr)

    radio.stop_scan()
    print("scan done")

def connect():
    connection = None
    try:
        for device in found:
            
            if device.address.string == mac_addr:
                print ("connecting..")
                #print (device.address.string)
                connection = radio.connect(device)
                if connection.connected:
                    print("------connected")
                    time.sleep(6)
                    connection.disconnect()
                    print("------disonnected")
    except:
        print("exception")
        pass
    #finally:
        #if connection is not None:
        #    connection.disconnect()
    
"""
for adv in ble.start_scan(ProvideServicesAdvertisement, timeout=5):
    print(adv)
    print(adv.address)
    if UARTService in adv.services:
        print("found a UARTService advertisement")
        uart_connection = ble.connect(adv)
        break
    # Stop scanning whether or not we are connected.
    ble.stop_scan()


i=0
scan()
while i < 3:
    i += 1
    time.sleep(6)
    connect()
print("all done")
"""

scan()
connect()
