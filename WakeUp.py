# to be run by a cronjob
from Milight import Milight
from time import sleep
m = Milight()
m.grp_ctrl(1,True)
m.brightness(1,2)
m.color(1,144)
for i in range(25):
	m.brightness(1,i+2)
	m.color(1,160-i)
	sleep(1)
m.white(1)
m.brightness(1,16)
for i in range(10):
	m.brightness(1,i+17)
	sleep(1)