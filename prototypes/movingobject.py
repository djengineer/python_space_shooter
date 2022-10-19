import pygame
import time

pygame.init()
pygame.font.init()
screenwidth = 600
screenheight = 300
size = (screenwidth,screenheight)
screen = pygame.display.set_mode(size)
bgcolor = (255,255,255)
pygame.display.set_caption("moving an object")
circlecolor=(60,20,10)
circlepos=[60,120]
done = False

#initialize all button states
up_key_pressed = False
down_key_pressed = False
left_key_pressed = False
right_key_pressed = False

while not done:
    screen.fill(bgcolor)
    pygame.draw.circle(screen,circlecolor,circlepos, 50, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_key_pressed = True
            if event.key == pygame.K_DOWN:
                down_key_pressed = True
            if event.key == pygame.K_LEFT:
                left_key_pressed = True
            if event.key == pygame.K_RIGHT:
                right_key_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_key_pressed = False
            if event.key == pygame.K_DOWN:
                down_key_pressed = False
            if event.key == pygame.K_LEFT:
                left_key_pressed = False
            if event.key == pygame.K_RIGHT:
                right_key_pressed = False

    if up_key_pressed == True and circlepos[1]>=0:
        circlepos[1] = circlepos[1] - 1
    if down_key_pressed == True and circlepos[1] <= screenheight:
        circlepos[1] += 1
    if left_key_pressed == True and circlepos[0]>=0:
        circlepos[0] -= 1
    if right_key_pressed == True and circlepos[0] <= screenwidth:
        circlepos[0] += 1
    pygame.display.flip()
while done:
    pygame.quit()
