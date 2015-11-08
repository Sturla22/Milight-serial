# to be run by a cronjob
from Milight import Milight
from time import sleep
m = Milight()
m.grp_ctrl(1,True)
m.brightness(1,2)
m.color(1,144)
for i in range(25):
	m.brightness(1,i)
	m.color(1,144-i)
	sleep(1)