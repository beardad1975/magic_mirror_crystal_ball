import serial
import struct
import time

ser = serial.Serial('com5', 115200, timeout=0)
ser.reset_input_buffer()
while True:
    data =ser.read(8)
    if data and len(data) == 8:
        my_list = struct.unpack('hhhh', data)
        print(my_list)
    time.sleep(0.05)