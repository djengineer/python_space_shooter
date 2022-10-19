import pygame
import time
from random import randint

pygame.init()
pygame.font.init()
screenwidth = 1100
screenheight = 530
size = (screenwidth,screenheight)
screen = pygame.display.set_mode(size)
bgcolor = (255,255,255)
pygame.display.set_caption("move and bounce a ball")

# Initialize variables
finished = False
start = False
is_boundary_hit = False

#initialize functions here
def listen_key_press():
    global start
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            start = not start


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
        
#load classes here
#enemy(name,speed,color,position,width,direction)
enemy_count = 30
max_speed = 1
enemy_obj_list = []
# e1 starts at index 0
for x in range(0,enemy_count):
    width = 20
    color = (randint(0,255),randint(0,255),randint(0,255))
    position = [randint(0,screenwidth),randint(0,screenheight)]
    speed = randint(1,max_speed)
    enemy_obj_list.append(enemy("e"+str(x+1),speed,color,position,width))


##### Game Loop #####
while finished == False:
    screen.fill(bgcolor)
    headerfont = pygame.font.SysFont("monospace", 100)
    title = headerfont.render("In3",1,(255,140,0))
    title2 = headerfont.render("Labs",1,(0,0,0))
    subfont = pygame.font.SysFont("monospace", 50)
    subtitle = subfont.render("Robotics & Tech Education",1,(0,0,0))
    screen.blit(title,(150,200))
    screen.blit(title2,(330,200))
    screen.blit(subtitle,(160,300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        listen_key_press()
    for x in enemy_obj_list:
        x.all_play_functions()
    pygame.display.flip()
while finished == True:
    pygame.quit()
