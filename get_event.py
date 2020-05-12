import pygame
import sys

pygame.init()

size = width, height = 600,400
bf = (255,255,255)

pygame.display.set_mode(size)
pygame.display.set_caption('捕获事件')

f = open('record.txt','w')

while True:
    for each in pygame.event.get():
        f.write(str(each) +'\n')
        
        if each.type == pygame.QUIT:
            f.close()
            sys.exit()
