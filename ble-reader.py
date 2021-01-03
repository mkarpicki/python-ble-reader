import binascii
import struct
import time
from bluepy.btle import UUID, Peripheral


#mac_address = "24:0A:C4:32:36:2E"
#characteristic_uuid = "a869a793-4b6e-4334-b1e3-eb0b74526c14"

def read_ble_server(mac_address, characteristic_uuid, struct_unpack_type = None):
    '''
    Connecting to BLE server and reads characteristic by UUID

    Keyword arguments:
    mac_address -- MAC Address of BLE server
    characteristic_uuid -- UUID of characteristic to read value from
    struct_unpack_type -- char ( https://docs.python.org/3.7/library/struct.html#format-characters )

    Returns: string
    '''
    
    print("connecting...")
    characteristic_uuid = UUID(characteristic_uuid)
    p = Peripheral(mac_address, "public")
    i = 0
    val = None
    try:
        #val = read_characterictic(p, characteristic_uuid, struct_unpack_type)
        while i < 10:
            val = read_characterictic(p, characteristic_uuid, struct_unpack_type)
            print("val: " + str(val))
            i += 1
            time.sleep(1)
    finally:
        p.disconnect()
        print("disconnected")
        return val

def read_characterictic(peripheral, characteristic_uuid, struct_unpack_type = None):
    '''
    read_characterictic readme
    '''
    try:
        print("reading...")
        val = None
        ch = peripheral.getCharacteristics(uuid=characteristic_uuid)[0]
        
        if (ch.supportsRead()):
            val = ch.read()
            if struct_unpack_type != None:            
                val = binascii.b2a_hex(val)
                val = binascii.unhexlify(val)
                val = struct.unpack(struct_unpack_type, val)[0]
    finally:
        return val


if __name__ == '__main__':
    #val = read_ble_server("24:0A:C4:32:36:2E", "a869a793-4b6e-4334-b1e3-eb0b74526c14", "i")
    val = read_ble_server("24:0A:C4:31:46:B2", "a869a793-4b6e-4334-b1e3-eb0b74526c14", "i")
    #while 1:
    #    val = read_ble_server("24:0A:C4:32:36:2E", "a869a793-4b6e-4334-b1e3-eb0b74526c14", "i")
    #    #val = read_ble_server("24:0A:C4:31:46:B2", "a869a793-4b6e-4334-b1e3-eb0b74526c14", "i")
    #    print("val: " + str(val))
    #    time.sleep(10)
