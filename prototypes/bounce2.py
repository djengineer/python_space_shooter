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

ball_color = (60,20,10)
ball_pos = [300,150]
ball_speed = 1
wall_color = (0,255,255)
#draw rect position (X,Y,Width,Height)
wall_1_pos = (0,0,0,300)
wall_2_pos = (screenwidth,0,0,300)

finished = False
start = False
is_boundary_hit = False
def listen_key_press():
    global start
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            start = not start
def set_dir():
    move_direction = {"X":randint(-30,30),"Y":randint(-30,30)}
    return move_direction
move_direction = set_dir()
def boundary_controller():
    if ball_pos[0] <= 0: #left screen boundary
        print("Left Bound")
        ball_pos[0] += 5
        #ball_pos[1] += 5
    if ball_pos[0] >= screenwidth: #right screen boundary
        print("Right Bound")
        ball_pos[0] -= 5
        ball_pos[1] -= 5
    if ball_pos[1] <= 0:    #top screen boundary
        print("Top Bound")
        ball_pos[0] += 0
        ball_pos[1] += 5
    if ball_pos[1] >= screenheight: #bottom screen boundary
        print("Bottom Bound")
        ball_pos[0] -= 5
        ball_pos[1] -= 5
def ball_movement_controller():
    #global screenwidth
    global move_direction
    if start == True:
        if ball_pos[0] < screenwidth and ball_pos[0] > 0 and ball_pos[1] < screenheight and ball_pos[1] > 0:
            ball_pos[0] += move_direction["X"]
            ball_pos[1] += move_direction["Y"]
        boundary_controller()
        
def printdetails():
    print(str(ball_pos[0])+" "+str(ball_pos[1]))
while finished == False:
    screen.fill(bgcolor)
    wall_1 = pygame.draw.rect(screen, wall_color, wall_1_pos,20)
    wall_2 = pygame.draw.rect(screen, wall_color, wall_2_pos,20) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        listen_key_press()
    pygame.draw.circle(screen,ball_color,ball_pos, 50, 0)
    ball_movement_controller()
    printdetails()
    pygame.display.flip()
while finished == True:
    pygame.quit()