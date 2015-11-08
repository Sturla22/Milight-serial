import serial
import time

TTL_PORT = "/dev/ttyAMA0"
TTL_SPEED = 9600
ser = serial.Serial(TTL_PORT, TTL_SPEED)


def write(byte):
    if len(byte) > 1:
        ser.write(str(byte)+"\x55")
    else:
        ser.write(str(byte)+"\x00\x55")
