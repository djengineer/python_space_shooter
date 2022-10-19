import pygame
import time
from random import randint

pygame.init()
pygame.font.init()
screenwidth = 1024
screenheight = 500
size = (screenwidth,screenheight)
screen = pygame.display.set_mode(size)
bgcolor = (255,255,255)
pygame.display.set_caption("move and bounce a ball")

# Initialize variables
########## initialize all button states ##########
is_key_pressed = {"up" : False,"down" : False,"left" : False,"right" : False}
finished = False
start = False
main_menu = True
game_over = False

#initialize functions here
def listen_key_press():
    global start
    global main_menu
    global game_over
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            start = not start
            main_menu = not main_menu
            if game_over == True:
                game_over = not game_over
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

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            is_key_pressed["up"] = False
        if event.key == pygame.K_DOWN:
            is_key_pressed["down"] = False
        if event.key == pygame.K_LEFT:
            is_key_pressed["left"] = False
        if event.key == pygame.K_RIGHT:
            is_key_pressed["right"] = False



#initialize class here
class enemy:
    def __init__(self,name,speed,color,position,width):
        self.name = name
        self.speed = speed
        self.color = color
        self.position = position
        self.width = width
        self.direction = self.set_dir()
    def set_dir(self):
        # Copy from your completed program
    def movement_controller(self):
        # Copy from your completed program
    def boundary_controller(self):
        # Copy from your completed program
        
    def draw(self):
        # Copy from your completed program
        
    def collision_detection(self):
        # Copy from your completed program
        
    def all_play_functions(self):
        self.draw()
        self.movement_controller()
        self.boundary_controller()
        self.collision_detection()


class player:
    def __init__(self,name,position,color,width,speed):
        self.name = name
        self.position = position
        self.color = color
        self.width = width
        self.speed = speed
    def draw(self):
        # Copy from your completed program
        
    def ball_movement_controller(self):
        # Copy from your completed program
    
    def all_player_functions(self):
        self.draw()
        self.ball_movement_controller()
        
#load classes here
#player
p1_ball_pos=[60,70]
p1_ball_color=(60,20,10)
p1_ball_width = 20
p1_ball_speed = 3
p1 = player("p1",p1_ball_pos,p1_ball_color,p1_ball_width,p1_ball_speed)
#enemy(name,speed,color,position,width,direction)

enemy_count = 10
max_enemy_speed = 1
enemy_obj_list = []
# e1 starts at index 0
for x in range(0,enemy_count):
    width = 20
    color = (randint(0,255),randint(0,255),randint(0,255))
    position = [randint(0,screenwidth),randint(0,screenheight)]
    speed = randint(1,max_enemy_speed)
    enemy_obj_list.append(enemy("e"+str(x+1),speed,color,position,width))


##### Game Loop #####
while finished == False:
    screen.fill(bgcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        listen_key_press()
    if main_menu == True and start == False:
        headerfont = pygame.font.SysFont("monospace", 30)
        title = headerfont.render("Press Space to Start",1,(0,0,0))
        screen.blit(title,(100,80))
    if start == True and main_menu == False:
        ## Load Enemies in Game Loop
        for enemy in enemy_obj_list:
            enemy.all_play_functions()
        ## Load player 1 in Game Loop
        p1.all_player_functions()
    if game_over == True and start == False:
        headerfont = pygame.font.SysFont("monospace", 30)
        title = headerfont.render("Game Over. Press Space to Main Menu.",1,(0,0,0))
        screen.blit(title,(100,80))
    pygame.display.flip()
while finished == True:
    pygame.quit()
