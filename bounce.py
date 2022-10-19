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
pygame.display.set_caption("move and bounce a ball")
ball_color=(60,20,10)
ball_pos=[60,120]
wall_color = (255,255,255)
wall_pos = (0,0,5,100)

done = False

########## initialize ball states ##########
start = False
#def listen_ball_key():
#    if event.key == pygame.K_SPACE:
#        start = not start
########## Method Definitions ##########

#def ball_movement_controller():
    # pygame's position starts from the TOP LEFT of the screen surface at (0,0)
    # X +1 will move it rightwards. How about X -1?
    # Y +1 will move it downwards. How about Y -1?
    # when SPACE key pressed, move right to wall.
    
########## End Method Definitions ##########       
########## Main Game Loop #########
while not done:
    screen.fill(bgcolor)
    pygame.draw.rect(screen, wall_color, wall_pos,5 )  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.key == pygame.K_SPACE:
            print("start pressed")
    # call the ball position controller
    #ball_movement_controller()
    pygame.display.flip()
while done:
    pygame.quit()
########## End Main Game Loop ##########
