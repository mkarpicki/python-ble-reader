from ble_scanner import scan
from ble_reader import read_ble_server

def start():
    devices = scan()

    for dev in devices:
        read_ble_server(dev.addr, "a869a793-4b6e-4334-b1e3-eb0b74526c14", "i")
    

if __name__ == '__main__':
    start()
