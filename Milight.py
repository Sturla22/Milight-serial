from led import write
from time import sleep

ALL_ON = chr(66)
ALL_OFF = chr(65)
GRP1_ON = chr(69)
GRP1_OFF = chr(70)
GRP2_ON = chr(71)
GRP2_OFF = chr(72)
GRP3_ON = chr(73)
GRP3_OFF = chr(74)
GRP4_ON = chr(75)
GRP4_OFF = chr(76)
DISCO_ON = chr(77)
DISCO_FASTER = chr(68)
DISCO_SLOWER = chr(67)
WHITE = [chr(194),chr(197),chr(199),chr(201),chr(203)]

class Milight:
    def grp_ctrl(self,grp,state):
        """grp_ctrl(grp,state)
        switches on grp
        grp:
        0 = All
        1 - 4 corresponding groups
        state:
        True for on, False for off
        """
        if grp == 0:
            if state:
                write(ALL_ON)
            else:
                write(ALL_OFF)
        if grp == 1:
            if state:
                write(GRP1_ON)
            else:
                write(GRP1_OFF)
        elif grp == 2:
            if state:
                write(GRP2_ON)
            else:
                write(GRP2_OFF)
        elif grp == 3:
            if state:
                write(GRP3_ON)
            else:
                write(GRP3_OFF)
        elif grp == 4:
            if state:
                write(GRP4_ON)
            else:
                write(GRP4_OFF)
    def white(self,grp):
        """white(grp)
        sets all lights in grp to white
        grp:
        0 = All
        1 - 4 corresponding groups
        """
        self.grp_ctrl(grp,True)
        sleep(0.1)
        write(WHITE[grp])

    def brightness(self,grp,luminosity):
        """brightness(grp,luminosity)
        sets the brightness of grp to luminosity
        grp:
        0 = All
        1 - 4 corresponding groups
        luminosity:
        2<=luminosity<=27
        """
        self.grp_ctrl(grp,True)
        sleep(0.1)
        if luminosity > 1 and luminosity < 28:
            write(chr(78)+chr(luminosity))
        else:
            #shold probably throw an exception
            if luminosity <=1:
                write(chr(78)+chr(2))
            else:
                write(chr(78)+chr(27))
    def color(self,grp,color):
        """color(grp,color)
        sets the color of grp to color
        grp:
        0 = All
        1 - 4 corresponding groups
        color:
        0<=color<=255
        """
        self.grp_ctrl(grp,True)
        sleep(0.1)
        if color > 0 and color < 256:
            write(chr(64)+chr(color))
        else:
            #should probably throw an exception
            if color <=0:
                write(chr(64)+chr(0))
            else:
                write(chr(64)+chr(255))

if __name__ == "__main__":
    m = Milight()
    m.color(2,88)
    sleep(0.7)
    m.color(1,88)
    sleep(1)
    m.white(0)
    sleep(1)
    m.brightness(0,2)
    sleep(0.7)
    m.brightness(0,5)
    sleep(0.7)
    m.brightness(0,14)
    sleep(0.7)
    m.brightness(0,27)
