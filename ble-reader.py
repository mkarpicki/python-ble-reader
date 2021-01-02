import binascii
import struct
import time
from bluepy.btle import UUID, Peripheral


#mac_address = "24:0A:C4:32:36:2E"
#characteristic_uuid = "a869a793-4b6e-4334-b1e3-eb0b74526c14"

def read_ble_server(mac_address, characteristic_uuid):
    '''
    Connecting to BLE server and reads characteristic by UUID

    Keyword arguments:
    mac_address -- MAC Address of BLE server
    characteristic_uuid -- UUID of characteristic to read value from

    Returns: string
    '''
    
    print("connecting...")
    characteristic_uuid = UUID(characteristic_uuid)
    p = Peripheral(mac_address, "public")
    try:
        val = read_characterictic(p, characteristic_uuid)        
    finally:
        p.disconnect()
        print("disconnected")
        return val

def read_characterictic(peripheral, characteristic_uuid):
    '''
    read_characterictic readme
    '''
    try:
        print("reading...")
        val = None
        ch = peripheral.getCharacteristics(uuid=characteristic_uuid)[0]
        
        if (ch.supportsRead()):            
            val = binascii.b2a_hex(ch.read())
            val = binascii.unhexlify(val)
            val = struct.unpack('f', val)[0]
    finally:
        return val


if __name__ == '__main__':
    while 1:
        val = read_ble_server("24:0A:C4:32:36:2E", "a869a793-4b6e-4334-b1e3-eb0b74526c14")
        print("val: " + str(val))
        time.sleep(2)
