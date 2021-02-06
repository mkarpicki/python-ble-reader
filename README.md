# python-ble-reader
Simple Raspberry PI BLE reader for future use as BLE client

> docker build -t ble-reader-app .
> docker run -v ${PWD}:/usr/src/app  --rm ble-reader-app
> docker run --rm -it --entrypoint /bin/bash ble-reader-app

## Install BLE lib
https://github.com/IanHarvey/bluepy

> sudo apt-get install python3-pip libglib2.0-dev
> sudo pip3 install bluepy

##Give permissions to access BLE device
### https://github.com/IanHarvey/bluepy/issues/218

cd PATH_WITH_BLUEPY (~/.local/lib/python3.5/site-packages/bluepy)
sudo setcap 'cap_net_raw,cap_net_admin+eip' bluepy-helper
sudo ./bluepy-helper 0