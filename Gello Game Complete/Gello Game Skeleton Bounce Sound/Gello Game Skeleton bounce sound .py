## copyright 2018 djengineer, Wong Ding Jie ##
## in use at in3labs, Singapore ##
## Game sounds used with creative commons licences from www.freesound.org ##
## Sound credits to plasterbrain, josepharaoh99  ##

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

ball_width = 20
player_ball_color = (255,0,0)
player_ball_pos = [10,10]
ball_color = (60,20,10)
ball_1_pos = [300,150]
ball_speed = 20
player_ball_speed = 10

########## initialize all button states ##########
is_key_pressed = {"up" : False,"down" : False,"left" : False,"right" : False,
    }
########## initialize all game states ##########
finished = False
gameover = False
main_menu = True
start = False
gameover = False



########## Preload sound files ##########
sound_bounce = pygame.mixer.Sound("sounds/bounce.wav")
sound_button_press = pygame.mixer.Sound("sounds/game_start.ogg")
########## Initialize sound list and directory ##########
soundlist = {"bounce":sound_bounce,"button_press":sound_button_press,}

########## Start of Function Definitions ##########
def play_sounds(sound_to_play):
    # set sound using parsed arguments
    # available parameters see soundlist variable
    # sound_to_play must be in string e.g. "bounce"
    #soundlist[sound_to_play].play plays the preloaded in soundlist
    soundlist[sound_to_play].play()
    


def listen_key_press():
    # when key is pressed, set is_key_pressed to True
    global start
    global main_menu
    global gameover
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            main_menu = not main_menu
            start = not start
            play_sounds("button_press")
            if gameover == True:
                gameover = not gameover
                main_menu = True
                start = False
        if event.key == pygame.K_UP:
            is_key_pressed["up"] = True
        if event.key == pygame.K_DOWN:
            is_key_pressed["down"] = True
        if event.key == pygame.K_LEFT:
            is_key_pressed["left"] = True
        if event.key == pygame.K_RIGHT:
            is_key_pressed["right"] = True
    # when key is released,  set is_key_pressed to False
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
    move_direction = {"X":randint(-ball_speed,ball_speed),"Y":randint(-ball_speed,ball_speed)}
    while move_direction["X"] == 0 and move_direction["Y"] == 0:
        move_direction = {"X":randint(-ball_speed,ball_speed),"Y":randint(-ball_speed,ball_speed)}    
    return move_direction
move_direction = set_dir()
def boundary_controller():
    global move_direction
    if ball_1_pos[0] <= 0: #left screen boundary
        print("Left Bound")
        ball_1_pos[0] += 5
        move_direction = set_dir()
        play_sounds("bounce")

    if ball_1_pos[0] >= screenwidth: #right screen boundary
        print("Right Bound")
        ball_1_pos[0] -= 5
        ball_1_pos[1] -= 5
        move_direction = set_dir()
        play_sounds("bounce")
        
    if ball_1_pos[1] <= 0:    #top screen boundary
        print("Top Bound")
        ball_1_pos[0] += 0
        ball_1_pos[1] += 5
        move_direction = set_dir()
        play_sounds("bounce")
        
    if ball_1_pos[1] >= screenheight: #bottom screen boundary
        print("Bottom Bound")
        ball_1_pos[0] -= 5
        ball_1_pos[1] -= 5
        move_direction = set_dir()
        play_sounds("bounce")
        
def ball_movement_controller():
    #global screenwidth
    global move_direction
    if start == True:
        if ball_1_pos[0] < screenwidth and ball_1_pos[0] > 0 and ball_1_pos[1] < screenheight and ball_1_pos[1] > 0:
            ball_1_pos[0] += move_direction["X"]
            ball_1_pos[1] += move_direction["Y"]
        boundary_controller()
        #print(move_direction)
def player_ball_movement_controller():
    # pygame's position starts from the TOP LEFT of the screen surface at (0,0)
    # X +1 will move it rightwards. How about X -1?
    # Y +1 will move it downwards. How about Y -1?
    # when up key pressed, y-coordinate -1 for as long as the key is pressed.
    if is_key_pressed["up"] == True and player_ball_pos[1]>=0:
        player_ball_pos[1] = player_ball_pos[1] - player_ball_speed
    if is_key_pressed["down"] == True and player_ball_pos[1] <= screenheight:
        player_ball_pos[1] += player_ball_speed
    if is_key_pressed["left"] == True and player_ball_pos[0]>=0:
        player_ball_pos[0] -= player_ball_speed
    if is_key_pressed["right"] == True and player_ball_pos[0] <= screenwidth:
        player_ball_pos[0] += player_ball_speed

def collision_detection():
    global start
    global gameover
    if abs(player_ball_pos[0] - ball_1_pos[0]) < ball_width > 0 and abs(player_ball_pos[1] - ball_1_pos[1]) < ball_width > 0:
        print("collision")
        start = False
        gameover = True
        
def printdetails():
    print(str(ball_1_pos[0])+" "+str(ball_1_pos[1]))

##### Game Loop #####
while finished == False:
    screen.fill(bgcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        listen_key_press()
    if main_menu == True and start == False:
        headerfont = pygame.font.SysFont("monospace", 30)
        header = headerfont.render("Press Space to Start",1,(0,0,0))
        screen.blit(header,(100,80))
    elif main_menu == False and start == True:
        pygame.draw.circle(screen,ball_color,ball_1_pos, ball_width, 0)
        pygame.draw.circle(screen,player_ball_color,player_ball_pos, ball_width, 0)
        player_ball_movement_controller()
        ball_movement_controller()
        collision_detection()
        printdetails()
    elif gameover == True and start == False:
        headerfont = pygame.font.SysFont("monospace", 30)
        header = headerfont.render("Game Over. 'Space' to Start",1,(0,0,0))
        screen.blit(header,(100,80))
        ball_1_pos = [300,150]
        player_ball_pos = [10,10]
        listen_key_press()
    else:
        headerfont = pygame.font.SysFont("monospace", 30)
        header = headerfont.render("State Erroe",1,(0,0,0))
        screen.blit(header,(100,80))
    pygame.display.flip()
while finished == True:
    pygame.quit()
