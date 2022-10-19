import pygame
import time
from datetime import datetime
from random import randint
from threading import Thread

clock = pygame.time.Clock()

pygame.init()
pygame.mixer.music.load("bgmusic.mp3")
pygame.font.init()
screenwidth = 1200
screenheight = 600
size = (screenwidth,screenheight)
screen = pygame.display.set_mode(size)
bgcolor = (255,255,255)
pygame.display.set_caption("2 player space shooter")
ball_colour = (60,20,10)
ball_pos = [300,150]
ball_speed = 30
player_ball_colour = (60,100,200)
player_ball_pos = [60,70]
p_ball_speed = 12
is_key_pressed = {"up" : False,"down" : False,"left" : False,"right" : False,"w":False,"s":False,"a":False,"d":False,"v":False,"rctrl":False}
ball_width = 20       

mainmenu_img = pygame.image.load('game_menu.png')
gamebg_img = pygame.transform.scale(pygame.image.load('gamebg.jpg'),(screenwidth,screenheight))
gameover_img = pygame.transform.scale(pygame.image.load('gameover.jpg'),(screenwidth,screenheight))
player_img = pygame.transform.scale(pygame.image.load('plane.png'),(100,100))
enemy_img = pygame.transform.scale(pygame.image.load('enemy.png'),(100,100))
#### For music ####
shoot_sound = pygame.mixer.Sound("mattix__8bit-laser-shot-04.wav")
bgmusic = False
playing = False
def play_music(bgmusic):
    global playing
    while bgmusic == True and playing == False:
        pygame.mixer.music.play(loops=-1)
        playing = True
        print("playing")
        print(playing,bgmusic)
def stop_music():
    global playing
    pygame.mixer.music.stop()
    playing = False

#insert code to listen to key press
def set_direction():
    move_direction = {"X":randint(-ball_speed,ball_speed),"Y":randint(-ball_speed,ball_speed)}
    while move_direction["X"] == 0 and move_direction["Y"] == 0:
        move_direction = {"X":randint(-ball_speed,ball_speed),"Y":randint(-ball_speed,ball_speed)}
    return move_direction

def listen_key_press():
    global start
    global main_menu
    global gameover
    global is_key_pressed
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            main_menu = not main_menu
            start = not start
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
        if event.key == pygame.K_w:
            is_key_pressed["w"] = True
        if event.key == pygame.K_s:
            is_key_pressed["s"] = True
        if event.key == pygame.K_a:
            is_key_pressed["a"] = True
        if event.key == pygame.K_d:
            is_key_pressed["d"] = True
        if event.key == pygame.K_RCTRL:
            is_key_pressed["rctrl"] = True
        if event.key == pygame.K_v:
            is_key_pressed["v"] = True   

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            is_key_pressed["up"] = False
        if event.key == pygame.K_DOWN:
            is_key_pressed["down"] = False
        if event.key == pygame.K_LEFT:
            is_key_pressed["left"] = False
        if event.key == pygame.K_RIGHT:
            is_key_pressed["right"] = False
        if event.key == pygame.K_w:
            is_key_pressed["w"] = False
        if event.key == pygame.K_s:
            is_key_pressed["s"] = False
        if event.key == pygame.K_a:
            is_key_pressed["a"] = False
        if event.key == pygame.K_d:
            is_key_pressed["d"] = False
        if event.key == pygame.K_RCTRL:
            is_key_pressed["rctrl"] = False
        if event.key == pygame.K_v:
            is_key_pressed["v"] = False 



bullet_list = []    

class Player:
    def __init__(self,name,colour,pos,speed,width,keys,bullet_size):
        self.name = name
        self.colour = colour
        self.pos = pos
        self.speed = speed
        self.width = width
        self.keys = keys
        self.bullet_size = bullet_size
        self.has_shot = False
        
    def ball_movement_controller(self):
     if start == True:
         if is_key_pressed[self.keys[0]] == True and self.pos[1] >= self.width:
             self.pos[1] -= self.speed
         if is_key_pressed[self.keys[1]] == True and self.pos[1] <= screenheight-self.width:
             self.pos[1] += self.speed
         if is_key_pressed[self.keys[2]] == True and self.pos[0] >= self.width:
             self.pos[0] -= self.speed
         if is_key_pressed[self.keys[3]] == True and self.pos[0] <= screenwidth-self.width:
             self.pos[0] += self.speed
         if is_key_pressed[self.keys[4]] == True:
             #### for shots every 0.5 seconds
             #if(0.5 > time.time() % 2 > 0 and self.has_shot == False):
              #   self.shoot_bullets()
              #   self.has_shot = True

             #if(1 > time.time() % 2 > 0.5 and self.has_shot == True):
             #    self.has_shot = False

            # if(1.5 > time.time() % 2 > 1 and self.has_shot == False):
              #   self.shoot_bullets()
             #    self.has_shot = True

            # if(2 > time.time() % 2 > 1.5 and self.has_shot == True):
            #     self.has_shot = False
            ##### for shot every 0.25 seconds
             if(0.25 > time.time() % 2 > 0 and self.has_shot == False):
                 self.shoot_bullets()
                 self.has_shot = True

             if(0.5 > time.time() % 2 > 0.25 and self.has_shot == True):
                 self.has_shot = False

             if(0.75 > time.time() % 2 > 0.5 and self.has_shot == False):
                 self.shoot_bullets()
                 self.has_shot = True

             if(1 > time.time() % 2 > 0.75 and self.has_shot == True):
                 self.has_shot = False
             if(1.25 > time.time() % 2 > 1 and self.has_shot == False):
                 self.shoot_bullets()
                 self.has_shot = True

             if(1.5 > time.time() % 2 > 1.25 and self.has_shot == True):
                 self.has_shot = False

             if(1.75 > time.time() % 2 > 1.5 and self.has_shot == False):
                 self.shoot_bullets()
                 self.has_shot = True

             if(2 > time.time() % 2 > 1.75 and self.has_shot == True):
                 self.has_shot = False
    def draw(self):
        #pygame.draw.circle(screen,self.colour,self.pos,self.width,0)
        #headerfont = pygame.font.SysFont("monospace", 30,True)
        #header = headerfont.render(self.name,1, (0,0,0))
        #screen.blit(header, (self.pos[0]-13,self.pos[1]-self.width/2))
        screen.blit(player_img,(self.pos[0]-13,self.pos[1]-self.width/2))
    def shoot_bullets(self):
        global bullet_list
        global is_key_pressed
        print('shoot bullet')
        shoot_sound.play()
        bullet_list.append([int(self.pos[0]+30),int(self.pos[1]+40),self.name])


def bullet_movement(color,speed,width):
    global bullet_list
    for i, bullet in enumerate(bullet_list):
        bullet_list[i][0] += speed
        pygame.draw.circle(screen,color,(bullet_list[i][0],bullet_list[i][1]),width,0)
        if(bullet_list[i][0] > screenwidth):
            bullet_list.pop(i)
        



bullet_speed = 30
bullet_width = 10
bullet_color = (175, 206, 255)        
p1 = Player("P1",(60,100,200),[260,70],12,20,["up","down","left","right","rctrl"],5)
p2 = Player("P2",(89,244,66),[60,70],12,20,["w","s","a","d","v"],5)


winner = None

class Enemy:
    def __init__(self,colour,pos,speed,width):
        self.colour = colour
        self.pos = pos
        self.speed = speed
        self.width = width
        self.direction = self.set_direction()
        self.status = True
        
    def set_direction(self):
        move_direction = {"X":randint(-self.speed,self.speed),"Y":randint(-self.speed,self.speed)}
        while move_direction["X"] == 0 and move_direction["Y"] == 0:
            move_direction = {"X":randint(-self.speed,self.speed),"Y":randint(-self.speed,self.speed)}
        return move_direction
    
    def movement_controller(self):
        if self.pos[0] < screenwidth and self.pos[1] < screenheight:
            self.pos[0] += self.direction["X"]
            self.pos[1] += self.direction["Y"]
        self.boundary_controller()
        
    def boundary_controller(self):
        if self.pos[0] <= 0:
            #print("Left bound")
            self.pos[0] += 5
            self.pos[1] += 0
            self.direction = self.set_direction()
        
        if self.pos[0] >= screenwidth:
            #print("Right bound")
            self.pos[0] -= 5
            self.pos[1] -= 0
            self.direction = self.set_direction()

        if self.pos[1] <= 0:
            #print("Top bound")
            self.pos[0] += 0
            self.pos[1] += 5
            self.direction = self.set_direction()

        if self.pos[1] >= screenheight:
            #print("Bottom bound")
            self.pos[0] -= 5
            self.pos[1] -= 5
            self.direction = self.set_direction()
        
    def draw(self):
        #pygame.draw.circle(screen,self.colour,self.pos,self.width,0)
        screen.blit(enemy_img,(self.pos[0]-50,self.pos[1]-50))
        
    def collision_detection(self):
        global start
        global gameover
        global winner
        if abs(p1.pos[0] - self.pos[0]) < self.width > 0 and abs(p1.pos[1] - self.pos[1]) < self.width > 0:
            print("collision")
            gameover = True
            start = False
            winner = "p2"
            
        if abs(p2.pos[0] - self.pos[0]) < self.width > 0 and abs(p2.pos[1] - self.pos[1]) < self.width > 0:
            print("collision")
            gameover = True
            start = False
            winner = "p1"
    def bullet_collision(self):
        global bullet_list
        for i, bullet in enumerate(bullet_list):
            try:
                if abs(self.pos[1] - bullet[1]) < self.width >0 and abs(self.pos[0] - bullet[0]) < self.width > 0:
                    print('del called')
                    self.__del__()
            except Exception as err:
                pass
    def __del__(self):
        self.status = False
        self.pos = [-100,-100]
    def all_play_functions(self):
        if self.status == True:
            self.draw()
            self.movement_controller()
            self.boundary_controller()
            self.collision_detection()
            self.bullet_collision()

e1 = Enemy(ball_colour,[600,300],ball_speed,ball_width)        
finished = False
start = False
gameover = False
main_menu = True
move_direction = set_direction()
init_enemy_count = 1
enemy_count = init_enemy_count
max_enemy_speed = 15
enemy_obj_list = []

for x in range(0,enemy_count):
    width = 20
    colour = (randint(0,255),randint(0,255),randint(0,255))
    position = [screenwidth,screenheight]
    speed = randint(1,max_enemy_speed)
    enemy_obj_list.append(Enemy(colour,position,speed,width))
def gen_enemies(enemy_count):
    global enemy_obj_list
    enemy_obj_list = []
    while(len(enemy_obj_list) < enemy_count):
        for x in range(0,enemy_count):
            width = 20
            colour = (randint(0,255),randint(0,255),randint(0,255))
            position = [screenwidth,screenheight]
            speed = randint(1,max_enemy_speed)
            enemy_obj_list.append(Enemy(colour,position,speed,width))    
##### Game Loop #####

while finished == False:
    clock.tick(60)
    screen.fill(bgcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        listen_key_press()
        
    if start == False and main_menu == True:
        screen.blit(mainmenu_img,(0,0))
        headerfont = pygame.font.SysFont("monospace", 70)
        header = headerfont.render("Main Menu",1, (255,255,255))
        screen.blit(header, (screenwidth/2-200,screenheight/2-50))
    elif start == True and main_menu == False:
        play_music(True)     
        screen.blit(gamebg_img,(0,0))
        p1.draw()
        p1.ball_movement_controller()
        #p1.shoot_bullets()
        p2.draw()
        p2.ball_movement_controller()
        #p2.shoot_bullets()
        active_enemy = []
        for enemy in enemy_obj_list:
            enemy.all_play_functions()
            if enemy.status == True:
                active_enemy.append(1)
        if len(active_enemy) ==0:
            #gameover = True
            #start = False
            enemy_count += 5
            gen_enemies(enemy_count)
        bullet_movement(bullet_color,bullet_speed,bullet_width)
        
    elif gameover == True and start == False:
        stop_music()
        screen.blit(mainmenu_img,(0,0))
        p1.pos = [260,70]
        p2.pos = [60,70]
        if winner == "p1":
            headerfont = pygame.font.SysFont("monospace", 60)
            header = headerfont.render("P1 wins. 'Space' to Start",1, (255,255,255))
            screen.blit(header, (screenheight/2-150,screenheight/2-50))
        if winner == "p2":
            headerfont = pygame.font.SysFont("monospace", 60)
            header = headerfont.render("P2 wins. 'Space' to Start",1, (255,255,255))
            screen.blit(header, (screenheight/2-150,screenheight/2-50))
        player_ball_pos = [10,10]
        ball_pos = [300,150]
        listen_key_press()
        enemy_count = init_enemy_count
        gen_enemies(init_enemy_count)
        for enemy in enemy_obj_list:
            enemy.pos = [screenwidth,screenheight]
        
    pygame.display.flip()
while finished == True:
    pygame.quit()
