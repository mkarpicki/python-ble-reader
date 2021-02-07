import binascii
import struct
import time
from bluepy.btle import UUID, Peripheral, DefaultDelegate


#mac_address = "24:0A:C4:32:36:2E"
#characteristic_uuid = "a869a793-4b6e-4334-b1e3-eb0b74526c14"

class MyDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
        # ... initialise here

    def handleNotification(self, cHandle, data):
    	data = bytearray(data)
    	print ("handleNotification %s" % data)

def watch_ble_server(mac_address, characteristic_uuid, struct_unpack_type = None):

    print(mac_address)
    print("+connecting...")
    characteristic_uuid = UUID(characteristic_uuid)
    val = None

    time.sleep(1)
    try:
        peripheral = Peripheral(mac_address, "public")
        peripheral.setDelegate( MyDelegate() )


        while True:
            if peripheral.waitForNotifications(1.0):
                # handleNotification() was called
                continue
            print ("Waiting...")

        time.sleep(1)
        peripheral.disconnect()
    finally:
        print("+done")


def read_from_ble_server(mac_address, characteristic_uuid, struct_unpack_type = None):
    '''
    Connecting to BLE server and reads characteristic by UUID

    Keyword arguments:
    mac_address -- MAC Address of BLE server
    characteristic_uuid -- UUID of characteristic to read value from
    struct_unpack_type -- char ( https://docs.python.org/3.7/library/struct.html#format-characters )

    Returns: string
    '''

    print(mac_address)
    print("+connecting...")
    characteristic_uuid = UUID(characteristic_uuid)
    val = None

    try:
        time.sleep(1)
        peripheral = Peripheral(mac_address, "public")
        time.sleep(1)
        val = read_characterictic(peripheral, characteristic_uuid, struct_unpack_type)
        time.sleep(1)
        peripheral.disconnect()
        
        print("+val: " + str(val))
    finally:
        return val


def read_characterictic(peripheral, characteristic_uuid, struct_unpack_type = None):
    '''
    read_characterictic readme
    '''
    try:
        print("+reading...")
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
    #val = read_from_ble_server("24:0A:C4:31:46:B2", "a869a793-4b6e-4334-b1e3-eb0b74526c14", "i")
    #val = read_from_ble_server("24:0A:C4:32:36:2E", "a869a793-4b6e-4334-b1e3-eb0b74526c14", "i")
    watch_ble_server("24:0A:C4:31:36:76", "a869a793-4b6e-4334-b1e3-eb0b74526c14", "i")

