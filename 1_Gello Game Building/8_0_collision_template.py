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

#insert code to declare ball_width to 20 here


#insert initial ball variables and values here
#ball_pos = [X-coordicates, Y-Coordinates]
ball_color = (60,20,10)
ball_pos = [300,150]
ball_speed = 1

#insert initial player ball variables and values here
#ball_pos = [X-coordicates, Y-Coordinates]
player_ball_color = (255,0,0)
player_ball_pos = [100,150]
player_ball_speed = 1

finished = False
start = False
is_boundary_hit = False

########## initialize all button states ##########
is_key_pressed = {"up" : False,"down" : False,"left" : False,"right" : False}

def listen_key_press():
    global start
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            start = not start
        if event.key == pygame.K_UP:
            is_key_pressed["up"] = True
        if event.key == pygame.K_DOWN:
            is_key_pressed["down"] = True
        if event.key == pygame.K_LEFT:
            is_key_pressed["left"] = True
        if event.key == pygame.K_RIGHT:
            is_key_pressed["right"] = True
    # when key is released, set the relevant is_key_pressed to False
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            is_key_pressed["up"] = False
        if event.key == pygame.K_DOWN:
            is_key_pressed["down"] = False
        if event.key == pygame.K_LEFT:
            is_key_pressed["left"] = False
        if event.key == pygame.K_RIGHT:
            is_key_pressed["right"] = False
def set_dir():
    #instead of lists, we use a dictionary here
    move_direction = {"X":randint(-ball_speed,ball_speed),"Y":randint(-ball_speed,ball_speed)}
    while move_direction["X"] == 0 and move_direction["Y"] == 0:
        move_direction = {"X":randint(-ball_speed,ball_speed),"Y":randint(-ball_speed,ball_speed)}
    return move_direction


def boundary_controller():
    global move_direction
    if ball_pos[0] <= 0: #left screen boundary
        print("Left Bound")
        ball_pos[0] += 5
        ball_pos[1] += 0
        move_direction = set_dir()

    if ball_pos[0] >= screenwidth: #right screen boundary
        print("Right Bound")
        ball_pos[0] -= 5
        ball_pos[1] -= 5
        move_direction = set_dir()
        
    if ball_pos[1] <= 0:    #top screen boundary
        print("Top Bound")
        ball_pos[0] += 0
        ball_pos[1] += 5
        move_direction = set_dir()
        
    if ball_pos[1] >= screenheight: #bottom screen boundary
        print("Bottom Bound")
        ball_pos[0] -= 5
        ball_pos[1] -= 5
        move_direction = set_dir()

def ball_movement_controller():
    global move_direction
    if start == True:
        #Auto ball controls
        if ball_pos[0] < screenwidth and ball_pos[0] > 0 and ball_pos[1] < screenheight and ball_pos[1] > 0:
            ball_pos[0] += move_direction["X"]
            ball_pos[1] += move_direction["Y"]
        boundary_controller()
        #player ball controls
        if is_key_pressed["up"] == True and player_ball_pos[1]>=0:
            player_ball_pos[1] = player_ball_pos[1] - 1
        if is_key_pressed["down"] == True and player_ball_pos[1] <= screenheight:
            player_ball_pos[1] += 1
        if is_key_pressed["left"] == True and player_ball_pos[0]>=0:
            player_ball_pos[0] -= 1
        if is_key_pressed["right"] == True and player_ball_pos[0] <= screenwidth:
            player_ball_pos[0] += 1

########## Insert code here to detect collision ##########

        
#set initial ball move direction
move_direction = set_dir()

##### Game Loop #####
while finished == False:
    screen.fill(bgcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        listen_key_press()
    # change the 20 here to ball_width
    pygame.draw.circle(screen,ball_color,ball_pos, 20, 0)
    pygame.draw.circle(screen,player_ball_color,player_ball_pos, 20, 0)
    ball_movement_controller()
    pygame.display.flip()
while finished == True:
    pygame.quit()
