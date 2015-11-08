# to be run by a cronjob
from Milight import Milight
from time import sleep
m = Milight()

GROUP = 1
INTERVAL = 10

m.grp_ctrl(GROUP, True)  # Lights on for group 1
m.brightness(GROUP, 2)  # Lower brightness just in case
m.color(GROUP, 144)  # Set desired starting color

# sunrise effect
for i in range(25):
    # this offset should really be implented in the m object...
    m.brightness(GROUP, i+2)
    m.color(GROUP, 160-i)
    sleep(INTERVAL)

m.white(GROUP)
m.brightness(GROUP, 6)

for i in range(21):
    m.brightness(GROUP, i+7)
    sleep(INTERVAL)
