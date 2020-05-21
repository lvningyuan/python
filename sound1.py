import pygame
import sys

from pygame.locals import *

pygame.init()

pygame.mixer.init()

pygame.mixer.music.load('1.ogg')
oygame.mixer.set_volume(0.2)
pygame.mixer.music.play()

a1 = pygame.mixer.Sound('2.wav')
a1.mix.set_volume(0.2)

a2 = pygame.mixer.Sound('3.wav')
a2.mix.set_volume(0.2)

bg_size = width, height = 300,200
screen = pygame.display.set_mode(bg_size)
pygame.display.set_title('Sound ')


pasue = False

while Ture:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
               a1.play()
            elif event.buttom == 3:
                a2.play()

        if event.type == KEYDOWN:
            if event.key ==K_SAPACE:
                pause = not pause

    screen.fill((255, 255, 255))

    if pause:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

    pygame.display.flip()
     
    
