import pygame
import datetime

pygame.init()
pygame.font.init()
size = (600,300)
screen = pygame.display.set_mode(size)
bgcolor = (255,255,255)
pygame.display.set_caption("gello")
header_pos=(100,50)

done = False
#app state: init, clock, stopwatch, alarm
app_state = ["init","clock","stopwatch","alarm"]
#initialize appstate
current_app_state = app_state[0]
#menu_pos[0] = (100,100)
#menu_pos[1] = (100,100)
#menu_pos[2] = (100,100)
#menu_pos[3] = (100,100)
menu_pos = [(100,100),(300,100),(100,150),(300,150)]


def renderclock():
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    headerfont = pygame.font.SysFont("monospace", 40)
    header = headerfont.render("clock",1,(0,0,0))
    screen.blit(header,(header_pos))
    myfont = pygame.font.SysFont("monospace", 60)
    # set time
    timenow = datetime.datetime.now().time().strftime("%H:%M:%S")
    timenow = str(timenow)
    label = myfont.render(timenow, 1, (0,0,0))
    screen.blit(label,(100, 100))
    menufont = pygame.font.SysFont("monospace", 14)
    back_btn = menufont.render("Press ESC for Main Menu",1,(0,0,0))
    screen.blit(back_btn,(300,200))

#def renderstopwatch():
    

while not done:
    screen.fill(bgcolor)
    #check for state change
    if current_app_state == "init":
        headerfont = pygame.font.SysFont("monospace", 40)
        header = headerfont.render("Welcome to my app",1,(0,0,0))
        screen.blit(header,(header_pos))
        menufont = pygame.font.SysFont("monospace", 14)
        clock_btn = menufont.render("Press A for Clock", 1, (0,0,0))
        screen.blit(clock_btn,menu_pos[0])
        stopwatch_btn = menufont.render("Press B for Stopwatach",1,(0,0,0))
        screen.blit(stopwatch_btn,menu_pos[1])
        alarm_btn = menufont.render("Press C for Alarm", 1, (0,0,0))
        screen.blit(alarm_btn,menu_pos[2])
        back_btn = menufont.render("Press ESC for Main Menu",1,(0,0,0))
        screen.blit(back_btn,menu_pos[3])
    elif current_app_state == "clock":
        renderclock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:    
            current_app_state=app_state[1]
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:    
            current_app_state=app_state[0]
    pygame.display.flip()
while done:
    pygame.quit()
    #quit()
