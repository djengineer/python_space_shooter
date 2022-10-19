import pygame
#### Initialize pygame ####
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("monospace", 60)
#### Set Screen Width 600, Screen Height 300 ###
screen = pygame.display.set_mode((600,300))
#### Game Loop ####
finished = False
while finished == False:
    screen.fill((255,255,255))
    mytitle = myfont.render("Hello World", 1, (0,0,0))
    screen.blit(mytitle, (100, 100))
    pygame.display.flip()
while finished == True:
    pygame.quit()
#### End of Game Loop ####

#screenwidth = 600
#screenheight = 300
#size = (screenwidth,screenheight)
#screen = pygame.display.set_mode(size)
#bgcolor = (255,255,255)
#pygame.display.set_caption("move and bounce a ball")

