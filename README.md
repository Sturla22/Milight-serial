# Milight-serial
This is an implementation of the [limitless led API](http://www.limitlessled.com/dev/) in Python
through a serial connection to the Milight bridge.

By following [this](https://servernetworktech.com/2014/09/limitlessled-wifi-bridge-4-0-conversion-raspberry-pi/) tutorial 
you can get a serial connection to your milight bridge.

*note:* you can stop your raspberry pi from writing stuff to the serial on startup by disabling 
the terminal over serial. To do this you run: 
>sudo raspi-config

select: 8. Advanced Options, A8 Serial, and choose No


Instead of using the program given in the tutorial you can use this to
control your lights directly from your raspberry pi (or from any serial capable computer really)

Just clone this repository and run 
>sudo python2 Milight.py

for a quick test (assuming you have some lights paired to group 1 and/or 2)
(if you are a member of the group tty you can omit the sudo)
