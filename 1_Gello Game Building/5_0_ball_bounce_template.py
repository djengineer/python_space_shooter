import pygame
import time
from random import randint

pygame.init()
pygame.font.init()
screenwidth = 600
screenheight = 300
size = (screenwidth,screenheight)
screen = pygame.display.set_mode(size)
bgcolor = (255,255,255)
pygame.display.set_caption("move and bounce a ball")

#insert code for initial ball variables and values here

#insert code to initialize is_boundary_hit here

#insert code to listen for key being pressed

#insert code to set direction

#insert code to control boundary

#insert code to control ball movement


finished = False
start = False

##### Game Loop #####
while finished == False:
    screen.fill(bgcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        #call listen to key press function here
            
    #draw ball here

    #call ball movement function here
    
    pygame.display.flip()
while finished == True:
    pygame.quit()
