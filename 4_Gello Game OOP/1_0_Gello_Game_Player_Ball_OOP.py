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

########## initialize all button states ##########
is_key_pressed = {"up" : False,"down" : False,"left" : False,"right" : False}

########## Class Declaration ##########
class player:
    def __init__(self,name,position,color,width):
        self.name = name
        self.position = position
        self.color = color
        self.width = width
    def draw(self):
        pygame.draw.circle(screen,self.color,self.position, self.width, 0)
    def ball_movement_controller(self):
    # pygame's position starts from the TOP LEFT of the screen surface at (0,0)
    # X +1 will move it rightwards. How about X -1?
    # Y +1 will move it downwards. How about Y -1?
    # when up key pressed, y-coordinate -1 for as long as the key is pressed.
        if is_key_pressed["up"] == True and self.position[1]>=0:
            self.position[1] -= 1
        if is_key_pressed["down"] == True and self.position[1] <= screenheight:
            self.position[1] += 1
        if is_key_pressed["left"] == True and self.position[0]>=0:
            self.position[0] -= 1
        if is_key_pressed["right"] == True and self.position[0] <= screenwidth:
            self.position[0] += 1
########## End Class Declarations ##########  
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

########## End Function Declarations ##########
########## Load Classes Here ##########
p1_ball_pos=[60,70]
p1_ball_color=(60,20,10)
p1_ball_width = 20

p1 = player("p1",p1_ball_pos,p1_ball_color,p1_ball_width)
########## End Load Classes ##########           
########## Main Game Loop #########
done = False
while not done:
    screen.fill(bgcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #start listening to which key presses
        listen_key_pressed()
    p1.draw()
    p1.ball_movement_controller()
    pygame.display.flip()
while done:
    pygame.quit()
########## End Main Game Loop ##########
