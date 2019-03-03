'''
Ciaran Farley
Ziah Jyothi

ZiCiRobot Control

Version 0.1

This program takes input from HID joysticks and maps it to https://www.adafruit.com/product/815 for controlling a robot

We are using:
https://www.pygame.org/docs/ref/joystick.html
https://github.com/adafruit/Adafruit_CircuitPython_ServoKit
'''
#library for reading from joystick
import pygame
#library for talking to servo board
from adafruit_servokit import ServoKit

# initialize the joystick
pygame.joystick.init()
ds4 = pygame.joystick.Joystick(0)

# initialize the pwm board
pwm = ServoKit(channels=16)

'''
Dualshock 4 Refrence

Axis 0: left stick x
Axis 1: left stick y
Axis 2: L2 Trigger
Axis 3: right stick x
Axis 4: right stick y
Axis 5: R2 Trigger

Btn 0: x
Btn 1: circle
Btn 2: triangle
Btn 3: square

Btn 6: left trigger (L2)
Btn 7: right trigger (R2)

'''

while True:
  #stearing
  kit.servo[1].angle = map(ds4.get_axis(0), 1, -1, 0, 180)
  #throttle
  if ds4.get_button(6): #left trigger
    kit.servo[2].angle = map(ds4.get_axis(2), 1, -1, 0, 90) #map to reverse
  elif ds4.get_button(7): #right trigger
    kit.servo[2].angle = map(ds4.get_axis(5), 1, -1, 90, 180) #map to forward
  else:
    kit.servo[2].angle = 90
  
  
  
  
