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
is_boundary_hit = False

#initialize functions here
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
        #instead of lists, we use a dictionary here
        move_direction = {"X":randint(-self.speed,self.speed),"Y":randint(-self.speed,self.speed)}
        while move_direction["X"] == 0 and move_direction["Y"] == 0:
            move_direction = {"X":randint(-self.speed,self.speed),"Y":randint(-self.speed,self.speed)}
        return move_direction
    def movement_controller(self):
        if self.position[0] < screenwidth and self.position[0] > 0 and self.position[1] < screenheight and self.position[1] > 0:
            self.position[0] += self.direction["X"]
            self.position[1] += self.direction["Y"]
        self.boundary_controller()
    def boundary_controller(self):
        if self.position[0] <= 0: #left screen boundary
            #print("Left Bound")
            self.position[0] += 5
            self.position[1] += 0
            self.direction = self.set_dir()
        if self.position[0] >= screenwidth: #right screen boundary
            #print("Right Bound")
            self.position[0] -= 5
            self.position[1] -= 5
            self.direction = self.set_dir()
        if self.position[1] <= 0:    #top screen boundary
            #print("Top Bound")
            self.position[0] += 0
            self.position[1] += 5
            self.direction = self.set_dir()
        if self.position[1] >= screenheight: #bottom screen boundary
            #print("Bottom Bound")
            self.position[0] -= 5
            self.position[1] -= 5
            self.direction = self.set_dir()
    def draw(self):
        pygame.draw.circle(screen,self.color,self.position, self.width, 0)
    def all_play_functions(self):
        self.draw()
        self.movement_controller()
        self.boundary_controller()


class player:
    def __init__(self,name,position,color,width,speed):
        self.name = name
        self.position = position
        self.color = color
        self.width = width
        self.speed = speed
    def draw(self):
        pygame.draw.circle(screen,self.color,self.position, self.width, 0)
    def ball_movement_controller(self):
    # pygame's position starts from the TOP LEFT of the screen surface at (0,0)
    # X +1 will move it rightwards. How about X -1?
    # Y +1 will move it downwards. How about Y -1?
    # when up key pressed, y-coordinate -1 for as long as the key is pressed.
        if is_key_pressed["up"] == True and self.position[1]>=0:
            self.position[1] -= self.speed
        if is_key_pressed["down"] == True and self.position[1] <= screenheight:
            self.position[1] += self.speed
        if is_key_pressed["left"] == True and self.position[0]>=0:
            self.position[0] -= self.speed
        if is_key_pressed["right"] == True and self.position[0] <= screenwidth:
            self.position[0] += self.speed
    def all_player_functions(self):
        self.draw()
        self.ball_movement_controller()
        
#load classes here
#player
p1_ball_pos=[60,70]
p1_ball_color=(60,20,10)
p1_ball_width = 20
p1_ball_speed = 10
p1 = player("p1",p1_ball_pos,p1_ball_color,p1_ball_width,p1_ball_speed)
#enemy(name,speed,color,position,width,direction)
enemy_count = 100
max_enemy_speed = 5
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
    ## Load Enemies in Game Loop
    for x in enemy_obj_list:
        x.all_play_functions()
    ## Load player 1 in Game Loop
    p1.all_player_functions()
    pygame.display.flip()
while finished == True:
    pygame.quit()
