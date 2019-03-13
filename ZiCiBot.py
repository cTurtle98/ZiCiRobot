'''
Ciaran Farley
Ziah Jyothi

ZiCiRobot Control

Version 0.2

HID game controller input
output to adafruit servo board
controls ziahs and ciarans robot
'''
#library for reading from joystick
import inputs
#library for talking to servo board
from adafruit_servokit import ServoKit
# time for sleeps
from time import sleep
import os
import sys



# initialize the pwm board
pwm = ServoKit(channels=16)


while True:
  #stearing
  print("Stearing Axis", + ds4.get_axis(0))
  stearingAngle = ((ds4.get_axis(0) - -1)/(1 - -1)) * (180 - 0) + 0
  pwm.servo[1].angle = stearingAngle
  #throttle
  if ds4.get_button(6): #left trigger
    pwm.servo[2].angle = ((ds4.get_axis(2) - -1)/(1 - -1)) * (90 - 0) + 0
  elif ds4.get_button(7): #right trigger
    pwm.servo[2].angle = ((ds4.get_axis(5) - -1)/(1 - -1)) * (180 - 90) + 90
  else:
    pwm.servo[2].angle = 90
  
  sleep(.5)
  
  
