import pygame
import sys
from pygame.locals import *


pygame.init()


size = width, height = 600, 400
white = (255,255,255)
black = (0, 0, 0)
green = (0,255,0)
red  =(255,0,0)
blue = (0,0,255)

points = [(200,75), (300,25), (400,75), (450,25), (450,125),(400,75),(300,125)]



screen = pygame.display.set_mode(size)
pygame.display.set_caption('fish')

position = size[0]//2, size[1]//2
moving = False

clock = pygame.time.Clock()

while True:
    for each in pygame.event.get():
        if each.type == QUIT:
            sys.exit()

        if each.type == MOUSEBUTTONDOWN:#�������
            if each.button ==1:  #���
                moving = True
                
        if each.type == MOUSEBUTTONUP:#����ɿ�  ע�⣬���������ж�button���кô��� �������
            if each.button ==1:
                moving = False

    if moving :#��ʱ��������Ƿ��ƶ�
        position = pygame.mouse.get_pos()

    screen.fill(white)

    pygame.draw.circle(screen, red, position,25,1),#�뾶�� ����
    pygame.draw.circle(screen, green, position,75,1),
    pygame.draw.circle(screen, blue, position,125,1),
    pygame.display.flip()

    clock.tick(10)
    

    
