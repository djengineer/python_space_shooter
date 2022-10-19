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
is_key_pressed = {"up" : False,"down" : False,"left" : False,"right" : False}

########## Method Definitions ##########

########## insert code for listen key press here #########
def listen_key_pressed():
    # when key is pressed, set the relevant is_key_pressed to True
    if event.type == pygame.KEYDOWN:
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

########## insert code for ball movement controller here ##########
def ball_movement_controller():
    # pygame's position starts from the TOP LEFT of the screen surface at (0,0)
    # X +1 will move it rightwards. How about X -1?
    # Y +1 will move it downwards. How about Y -1?
    # when up key pressed, y-coordinate -1 for as long as the key is pressed.
    if is_key_pressed["up"] == True and player_ball_pos[1]>=0:
        player_ball_pos[1] = player_ball_pos[1] - 1
    if is_key_pressed["down"] == True and player_ball_pos[1] <= screenheight:
        player_ball_pos[1] += 1
    if is_key_pressed["left"] == True and player_ball_pos[0]>=0:
        player_ball_pos[0] -= 1
    if is_key_pressed["right"] == True and player_ball_pos[0] <= screenwidth:
        player_ball_pos[0] += 1
########## End Method Definitions ##########       
########## Main Game Loop #########
while not done:
    screen.fill(bgcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #start listening to which key presses
        listen_key_pressed()
    # call the ball movement controller
    ball_movement_controller()
    pygame.draw.circle(screen,player_ball_color,player_ball_pos, 20, 0)
    pygame.display.flip()
while done:
    pygame.quit()
########## End Main Game Loop ##########
