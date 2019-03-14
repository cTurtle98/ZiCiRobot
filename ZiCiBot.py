'''
Ciaran Farley
Ziah Jyothi

ZiCiRobot Control

Version 0.2

HID game controller input
output to adafruit servo board
controls ziahs and ciarans robot
'''
DEBUG = True

#library for reading from joystick
import inputs
#library for talking to servo board
from adafruit_servokit import ServoKit
# alloow sleepz
from time import sleep

#function for turning the byte values from input into degrees for the servo library
def map_value (OldValue, OldMin, OldMax, NewMin, NewMax):
    OldRange = (OldMax - OldMin)  
    NewRange = (NewMax - NewMin)
    NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
    return NewValue

# initialize the pwm board
pwm = ServoKit(channels=16)

#stearing trim amount of degrees for adjustment for center
stearingTrim = 0

while True:
    ds4_events = inputs.get_gamepad()
    for ds4 in ds4_events:
        # stearing
        # input from left stick x
        if ds4.code == "ABS_X" :
            stearingAngle = int(map_value(ds4.state, 0, 255, 0, 128))
            pwm.servo[0].angle = stearingAngle + stearingTrim
        if ds4.code == "BTN_START" :
            stearingTrim = stearingAngle - 180
            sleep(1)
        #throttle
        # right trigger forward
        if ds4.code ==  "ABS_RZ" :
            pwm.servo[1].angle = map_value(ds4.state, 0, 255, 90, 128)
        elif ds4.code == "ABS_Z" :
            pwm.servo[1].angle = map_value(ds4.state, 0, 255, 0, 90)
        else :
            pwm.servo[1].angle = 90


 
