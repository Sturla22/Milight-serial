import sys
from Milight import Milight
m = Milight()
# ./wrapper.py GRP ON/OFF [-c CLR] [-b BRT]
# GRP; 0:All 1-4:1-4
# CLR; 0-254
# BRT; 0-25
if len(sys.argv)<3:
	sys.exit("ERROR: too few args\n usage: ./wrapper.py GRP ON/OFF [-c CLR] [-b BRT]")
group = int(sys.argv[1])
if sys.argv[2]=="ON":
	if len(sys.argv)<4:
		print "ON"
		m.grp_ctrl(group,True)
	elif len(sys.argv)<6:
		if sys.argv[3]=="-c":
			print "COL"
			m.color(group,int(sys.argv[4]))
		elif sys.argv[3]=="-b":
			print "BRT"
			m.brightness(group,int(sys.argv[4]))
		else:
			sys.exit("usage: ./wrapper.py GRP ON/OFF [-c CLR] [-b BRT]")
	else:
		sys.exit("ERROR: too many args\n usage: ./wrapper.py GRP ON/OFF [-c CLR] [-b BRT]")
else:
	print "OFF",group
	m.grp_ctrl(group,False)



