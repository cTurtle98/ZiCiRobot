# ZiCiRobot

this is a python program that runs on a raspberry pi for controlling a robot ziah and I are building

INPUT DEVICE: sony dualshock 4

OUTPUT DEVICE: adafruit 16 channel pwm servo driver board

im not sure what else to put here so heres the changelog

## Changelog

#### v0.4 working throttle
- Test Video: https://www.youtube.com/watch?v=iE4JfnMkYAo
- throttle works now
- throttle is the R2 and L2 triggers
- right is forward left is reverse

#### v0.3 working stearing
- stearing is on the left stick x axis
- I got the code from the inputs library and the servokit library working together for stearing
- I realised that ziah mounted the servo wrong and I had to add a 27 degree stearing offset so it would drive straight ish

#### v0.2 switch from pygame to inputs
- I realise that pygame is mainly a graphics library and does not work on headless raspbian lite
- I find a library called "inputs" to use to get values off the dualshock 4

#### v0.1 pygame initial code
- I accomplished adding the servo driver board librarys and base code for publishing to the driver board
- I started getting pygame working for joystick input
