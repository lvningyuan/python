import pygame
import sys
from random import *
from pygame.locals import *


#sprite 是pygame 提供的 Ball 类 直接继承 pygame.sprite.Sprite类 
class Ball(pygame.sprite.Sprite):
    def __init__(self, image, position, speed, bg_size):
        #继承先初始化基类
        pygame.sprite.Sprite.__init__(self)

        #图片加上convert_alpha 有利于游戏速度
        self.image = pygame.image.load(image).convert_alpha()
        #图片的位置矩形
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position#position 是传入进来的二元组
        self.speed = speed
        self.width,self.height = bg_size[0], bg_size[1]

    def move(self):
        self.rect = self.rect.move(self.speed)#ball的move调用rect的move方法

        if self.rect.right < 0:
            self.rect.left = self.width
            
        elif self.rect.left > self.width:
            self.rect.right = 0
            
        elif self.rect.top > self.height:
            self.rect.bottom = 0
            
        elif self.rect.bottom < 0:
            self.rect.top = self.height

        
def main():
    pygame.init()

    ball_image =  '2.png'
    back_ground = '4.jpg'

    running = True
    #可以游戏成功或者失败就结束，不用用户点击退出

    bg_size = width, height = 1000, 600

    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption('play the ball')
    #载入背景图片
    background = pygame.image.load(back_ground).convert_alpha() 

    balls =[]
    
    for i in range(5):
        #position 是个二元组 -100是减去ball的半径
        position = randint(0,width-100),randint(0, height-100)
        speed = [randint(-10,10), randint(-10,10)]

        #实例化对象
        ball = Ball(ball_image,position, speed, bg_size)
        balls.append(ball)

    clock = pygame.time.Clock() #设置帧率       

#主循环
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.blit(background,(0,0))# image + position 

        for each in balls:
            each.move()
            screen.blit(each.image, each.rect)#image + position

        pygame.display.flip()
        clock.tick(30)


        
if __name__ == '__main__':
    main()

