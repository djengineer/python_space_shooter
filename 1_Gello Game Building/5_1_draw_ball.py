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

#insert initial ball variables and values here
ball_color = (60,20,10)
ball_pos = [300,150]
ball_speed = 1

finished = False
start = False

##### Game Loop #####
while finished == False:
    screen.fill(bgcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pygame.draw.circle(screen,ball_color,ball_pos, 20, 0)
    pygame.display.flip()
while finished == True:
    pygame.quit()
