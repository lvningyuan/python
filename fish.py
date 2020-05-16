import pygame
import sys
from pygame.locals import *


pygame.init()


size = width, height = 600, 400
white = (255,255,255)
black = (0, 0, 0)
green = (0,255,0)

points = [(200,75), (300,25), (400,75), (450,25), (450,125),(400,75),(300,125)]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('fish')

clock = pygame.time.Clock()

while True:
    for each in pygame.event.get():
        if each.type == QUIT:
            sys.exit()

    screen.fill(white)

    pygame.draw.polygon(screen, green, points,0)

    pygame.display.flip()

    clock.tick(10)
    
