FROM python:3.9.1-buster
#FROM python:3

WORKDIR /usr/src/app

# RUN apt-get update && \
#     apt-get -y install build-essential libdbus-1-dev && \
#     git clone https://github.com/IanHarvey/bluepy.git && \
#     cd bluepy && \
#     git checkout 7d2864686f8b3daad021ea042adc322276e75045 . && \
#     cd bluepy && \
#     make

RUN apt-get update && \
    apt-get -y install python3-pip libglib2.0-dev && \
    pip3 install bluepy

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./ble-reader.py" ]
