#!/usr/env/python2
import sys
from Milight import Milight
m = Milight()
# ./wrapper.py GRP ON/OFF [-c CLR] [-b BRT]
# GRP; 0:All 1-4:1-4
# CLR; 0-254
# BRT; 0-25
if len(sys.argv)<3:
	sys.exit("ERROR: too few args\n usage: ./wrapper.py GRP ON/OFF [-c CLR] [-b BRT]")
group = sys.argv[2]
if sys.argv[3]=="ON":
	if len(sys.argv)<4:
		m.grp_ctrl(group,True)
	elif len(sys.argv)<5:
		if sys.argv[4][:2]=="-c":
			m.color(group,sys.argv[4][2:])
		elif sys.argv[4][:2]=="-b":
			m.brightness(group,sys.argv[4][2:])
		else:
			sys.exit("usage: ./wrapper.py GRP ON/OFF [-c CLR] [-b BRT]")
	else:
		sys.exit("ERROR: too many args\n usage: ./wrapper.py GRP ON/OFF [-c CLR] [-b BRT]")
else:
	m.grp_ctrl(group,False)



