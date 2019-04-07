#
# ZiCi-Robot
# https://github.com/cTurtle98/ZiCiRobot/blob/master/ZiCiBot.py
# 
# setup script for preparing a raspberry pi for being the robot brain
#

sudo apt update

sudo apt install python3-pip -y

sudo apt-get install python-smbus -y

sudo apt-get install i2c-tools -y

sudo pip3 install adafruit-circuitpython-servokit

sudo pip3 install inputs

sudo pip3 install ds4drv

echo '####################'
echo 'please use "sudo crontab -e" to add the following lines to the crontab file'
echo '@reboot python /home/pi/ZiCiRobot/oled.py &'
echo '@reboot python3 /home/pi/ZiCiRobot/ZiCiBot.py &'
echo '####################'
