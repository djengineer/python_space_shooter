import pygame
import time
########## Initialize Pygame ##########
pygame.init()
pygame.font.init()
########## Set Initial Values ##########
screenwidth = 600
screenheight = 300
size = (screenwidth,screenheight)
screen = pygame.display.set_mode(size)
bgcolor = (255,255,255)
pygame.display.set_caption("Moving Player Ball")
player_ball_color=(60,20,10)
player_ball_pos=[60,70]
done = False

########## initialize all button states ##########


########## Method Definitions ##########
def listen_key_pressed():
    # when key is pressed, set is_key_pressed to True
    if event.type == pygame.KEYDOWN:
       
    # when key is released,  set is_key_pressed to False
    if event.type == pygame.KEYUP:
        

def ball_movement_controller():
    # pygame's position starts from the TOP LEFT of the screen surface at (0,0)
    # X +1 will move it rightwards. How about X -1?
    # Y +1 will move it downwards. How about Y -1?
    # when up key pressed, y-coordinate -1 for as long as the key is pressed.



    
########## End Method Definitions ##########       
########## Main Game Loop #########
while not done:
    screen.fill(bgcolor)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #start listening to which key being pressed here

    # call the ball position controller here

    pygame.display.flip()
while done:
    pygame.quit()
########## End Main Game Loop ##########
