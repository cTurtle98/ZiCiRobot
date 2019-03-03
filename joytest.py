'''
joystick test program

ciaran farley

'''

from pygame import joystick

joystick.init()

joystick_count = pygame.joystick.get_count()

for i in range(joystick_count):
  joystick = pygame.joystick.Joystick(i)
  joystick.init()
  
  name = joystick.get_name()
  print(Joystick name: " + name)
  
  axes = joystick.get_numaxes()
  
  for i in range( axes ):
    axis = joystick.get_axis( i )
    print("Axis ", + i, + " value: ", axis)
  
  buttons = joystick.get_numbuttons()
  
  for i in range( buttons ):
    button = joystick.get_button( i )
    print ("button ", + i, + "value ", + button)
    
  print()
  print()
  
