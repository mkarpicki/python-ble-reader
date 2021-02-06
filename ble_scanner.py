from bluepy.btle import Scanner, DefaultDelegate

BLE_NAME_FIELD = "Complete Local Name"
BLE_NAME_PATTERN = "ESP32_"


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)

def scan():
    found = set()
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(10.0)


    for dev in devices:
        #print ("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        for (adtype, desc, value) in dev.getScanData():
            #print ("  %s = %s" % (desc, value))
            if desc == BLE_NAME_FIELD and (BLE_NAME_PATTERN in value) :
                print ("Found: %s" % value)
                found.add(dev)

    return found            


if __name__ == '__main__':
    #found = set()
    found = scan()
    for dev in found:
        print ("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        
