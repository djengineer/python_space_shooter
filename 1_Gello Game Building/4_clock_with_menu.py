import pygame
import datetime

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("monospace", 60)
size = (600,300)
screen = pygame.display.set_mode(size)
bgcolor = (255,255,255)
pygame.display.set_caption("clock")
done = False

is_main_menu = True
show_clock = False

def RunMainMenu():
    titlefont = pygame.font.SysFont("monospace", 30)
    mytitle = titlefont.render("Press Space for Clock",1,(0,0,0))
    screen.blit(mytitle,(100,100))

def RunClock():
    # Format current system time into a readable format Hour, Minute, Seconds
    # put formated time into a variable called timenow
    timenow = datetime.datetime.now().time().strftime("%H:%M:%S")
    # timenow is in timeformat, in order to print it, we must change it to string format
    timenow = str(timenow)
    label = myfont.render(timenow, 1,(0,0,0))
    screen.blit(label,(100, 100))

while done == False:
    screen.fill(bgcolor)
    # Listens for pygame events such as mouseclicks and keyboard press
    for event in pygame.event.get():
        #quit button is pressed
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                is_main_menu = not is_main_menu
                show_clock = not show_clock
    if is_main_menu == True and show_clock == False:
        RunMainMenu()
    if is_main_menu == False and show_clock == True:
        RunClock()
    pygame.display.flip()

while done == True:
    pygame.quit()
    quit()
