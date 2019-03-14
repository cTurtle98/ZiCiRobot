'''
Ciaran Farley
Ziah Jyothi

ZiCiRobot Control

Version 0.3

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


def map_value (OldValue, OldMin, OldMax, NewMin, NewMax):
    '''function to convert one range of numbers to another range
    this is pretty much the map() function from c
    I need this because the HID library gives me a 0 to 255 range for the axis inputs
    the servo driver board wants a 0 to 180 range'''
    OldRange = (OldMax - OldMin)  
    NewRange = (NewMax - NewMin)
    NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
    return NewValue

# tell servokit that I am using the 16 channel version of their i2c board
# also instanciate a servokit object to name "pwm"
pwm = ServoKit(channels=16)

# ziah put the stearing servo onto the stearing rack wrong
# I dont feel like fixing it so instead I hard coded an offset into the control software
# lets pretend that the servo is properly centered
stearingTrim = 27

# main while loop to keep the program running till I kill it
while True:
    # instanciate an object of the event manager from the inputs library
    ds4_events = inputs.get_gamepad()
    # for loop to let me handle each event individually
    for ds4 in ds4_events:
        # if my event has a code of ABS_X (left stick x axis) run next code
        if ds4.code == "ABS_X" :
            # set the stearing angle to be the state (value) of the event mapped from a byte size to a degree then add the trim (see comments above)
            stearingAngle = int(map_value(ds4.state, 0, 255, 0, 128)) + stearingTrim
            # publish stearing angle to the pwm driver board
            # stearing servo is on channel 0
            pwm.servo[0].angle = stearingAngle
        # if the event has a code of ABS_RZ (R2 Axis)
        # right trigger is forward (90 to 128 degrees) on the speed controller
        if ds4.code ==  "ABS_RZ" :
            # set the pwm output on channel 1 for the motor speed controller to a mapped value from L2
            pwm.servo[1].angle = map_value(ds4.state, 0, 255, 90, 128)
        # else if the event has a code of ABS_Z (L2 axis)
        # left trigger is reverse (0 to 90 degrees) on the speed controller
        elif ds4.code == "ABS_Z" :
            # set the pwm output on channel 1 for the motor speed controller to a mapped value from L2
            pwm.servo[1].angle = map_value(ds4.state, 0, 255, 0, 90)
        # else if im not pressing either trigger
        else :
            # set the speed controller to 90 degrees aka center aka off
            pwm.servo[1].angle = 90
