import pygame
import datetime

pygame.init()
pygame.font.init()
size = (600,300)
screen = pygame.display.set_mode(size)
bgcolor = (255,255,255)
pygame.display.set_caption("gello")

done = False
btn_init = True
just_start = True

def render_clock():
    # render clock text
    print("render function is called")
    done = False
    while not done:
        print("inside while loop")
        label = myfont.render(timenow, 1, (0,0,0))
        screen.blit(label,(100, 100))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            done = True
    while done:
        print("out of render clock while loop")
        return


while not done:
    screen.fill(bgcolor)
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    myfont = pygame.font.SysFont("monospace", 60)
    # set time
    timenow = datetime.datetime.now().time().strftime("%H:%M:%S")
    timenow = str(timenow)
    if just_start:
        if btn_init:
            # initialize clock button
            clock_button_color = (0,255,255)
            clock_button_pos = (150,200,100,50)
            clock_button = pygame.draw.rect(screen,clock_button_color,clock_button_pos);
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
       
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            print("clock_button is pressed")
            #print(timenow)
            btn_init = not btn_init
            # remove button from screen (white)
            clock_button_color = (255,255,255)
            clock_button = pygame.draw.rect(screen,clock_button_color,clock_button_pos)
            render_clock()
                          
    pygame.display.flip()

while done:
    pygame.quit()
    quit()

