import pygame


def get_controllers():
    controllers = []
    for controller in range(pygame.joystick.get_count()):
        controllers.append(pygame.joystick.Joystick(controller))
        controllers[-1].init()
    return controllers


def get_controller_events(controller):
    axes = []
    buttons = []
    for axis in range(controller.get_numaxes()):
        axes.append(controller.get_axis(axis))
    for button in range(controller.get_numbuttons()):
        buttons.append(controller.get_button(button))
    return axes, buttons


###-------------------- SIMPLE CONTROLLER GUIDE --------------------###

#Buttons
#0 	X
#1 	Circle
#2 	Square
#3 	Triangle
#4 	Share
#5 	PS
#6 	Options
#7 	L3
#8 	R3
#9 	L1
#10 	R1
#11 	Down Arrow
#12 	Up Arrow 
#13 	Left Arrow
#14 	Right Arrow
#15 	D-Pad

#Axes
#0	L Right-Left
#1	L Up-Down
#2	R Right-Left
#3	R Up-Down
#4	L2
#5	R2

###-----------------------------------------------------------------###





