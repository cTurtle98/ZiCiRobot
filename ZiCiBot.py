'''
Ciaran Farley
Ziah Jyothi

ZiCiRobot Control

Version 0.4

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
  return (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
  
def stearing (position) :
  pwm.servo[0].angle = int(map_value(position, 0, 255, 0, 128)) + stearingTrim
  
#def throttle (position) :
  

# tell servokit that I am using the 16 channel version of their i2c board
# also instanciate a servokit object to name "pwm"
pwm = ServoKit(channels=16)

# ziah put the stearing servo onto the stearing rack wrong
# I dont feel like fixing it so instead I hard coded an offset into the control software
# lets pretend that the servo is properly centered
stearingTrim = 27

#center the throttle
throttleAngle = 90

def main():
  # main while loop to keep the program running till I kill it
  while True:
    # instanciate an object of the event manager from the inputs library
    ds4_events = inputs.get_gamepad()
    # for loop to let me handle each event individually
    for ds4 in ds4_events:

      #speed up hopefuly by ignoring event types I dont need
      if (ds4.ev_type == "Sync") or (ds4.ev_type == "Misc") :
        continue
            
      # STEARING
      # if my event has a code of ABS_X (left stick x axis) run next code
      if ds4.code == "ABS_X" :
        stearing(ds4.state)
        continue
            
      #THROTTLE
      if (ds4.code == "ABS_Z") or (ds4.code == "ABS_RZ") :
        # if the event has a code of ABS_RZ (R2 Axis)
        # right trigger is forward (90 to 128 degrees) on the speed controller
        if ds4.code ==  "ABS_RZ" :
          # map the value from L2 into the forward range for the speed controller for throttle
          throttleAngle = int(map_value(ds4.state, 0, 255, 90, 128))
        # else if the event has a code of ABS_Z (L2 axis)
        # left trigger is reverse (90 to 0 degrees) on the speed controller
        elif ds4.code == "ABS_Z" :
          # map the value from the L2 trigger to 90 through 0 degrees on the speed controller
          throttleAngle = int(map_value(ds4.state, 0, 255, 90,  0))
        #publish value to servo
        pwm.servo[1].angle = throttleAngle
        continue

if __name__ == "__main__":
    main()
                
                
