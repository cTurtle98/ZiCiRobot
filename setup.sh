#
# ZiCi-Robot
# https://github.com/cTurtle98/ZiCiRobot
# 
# setup script for preparing a raspberry pi for being the robot brain
#

sudo apt update

sudo apt install python3-pip python-smbusl i2c-tools -y

sudo pip3 install adafruit-circuitpython-servokit inputs ds4drv

echo '####################'
echo 'please use "sudo crontab -e" to add the following lines to the crontab file'
echo '@reboot python /home/pi/ZiCiRobot/oled.py &'
echo '@reboot python3 /home/pi/ZiCiRobot/ZiCiBot.py &'
echo '####################'
