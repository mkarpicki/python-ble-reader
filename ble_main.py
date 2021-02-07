import time
from ble_scanner import scan
from ble_reader import read_from_ble_server, watch_ble_server

def start():
    devices = scan()
    time.sleep(1)

    for dev in devices:
        #watch_ble_server(dev.addr, "a869a793-4b6e-4334-b1e3-eb0b74526c14", "i")
        read_from_ble_server(dev.addr, "a869a793-4b6e-4334-b1e3-eb0b74526c14", "i")
    

if __name__ == '__main__':
    start()
