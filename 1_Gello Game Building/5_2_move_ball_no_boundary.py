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
#ball_pos = [X-coordicates, Y-Coordinates]
ball_color = (60,20,10)
ball_pos = [300,150]
ball_speed = 35

finished = False
start = False
def listen_key_press():
    global start
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            start = not start

def ball_movement_controller():
    global move_direction
    if start == True:
        ball_pos[0] += 1
        ball_pos[1] += 1
        
##### Game Loop #####
while finished == False:
    screen.fill(bgcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        listen_key_press()
    pygame.draw.circle(screen,ball_color,ball_pos, 20, 0)
    ball_movement_controller()
    pygame.display.flip()
while finished == True:
    pygame.quit()
