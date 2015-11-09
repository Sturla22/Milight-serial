import serial
import time

TTL_PORT = "/dev/ttyAMA0"
TTL_SPEED = 9600
ser = serial.Serial(TTL_PORT, TTL_SPEED)


def write(byte):
	# ensure the channel is available by waiting 100ms
	time.sleep(0.1)
	#write two bytes to channel
    if len(byte) > 1:
        ser.write(str(byte)+"\x55")
    #write a single byte to channel
    else:
        ser.write(str(byte)+"\x00\x55")
