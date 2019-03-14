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
            if DEBUG :
                print ("DEBUG: STEARING ", + ds4.state, + map_value(ds4.state, 0, 255, 0, 128))
            pwm.servo[1].angle = int(map_value(ds4.state, 0, 255, 0, 128))
        #throttle
        # right trigger forward
        if ds4.code ==  "ABS_RZ" :
            pwm.servo[2].angle = map_value(ds4.state, 0, 255, 90, 128) + stearingTrim
        elif ds4.code == "ABS_Z" :
            pwm.servo[2].angle = map_value(ds4.state, 0, 255, 0, 90) + stearingTrim
        else :
            pwm.servo[2].angle = 90 + stearingTrim


 
