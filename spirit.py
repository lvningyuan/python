import pygame
import sys
import math
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


#a ball   VS balls  
def collide_check(item, target):

    col_balls =[]#碰撞列表
    for each in target:
        distance = math.sqrt(\
            math.pow((item.rect.center[0] - each.rect.center[0]),2) +\
            math.pow((item.rect.center[1] - each.rect.center[1]),2))
        #碰撞
        
        if distance <= (item.rect.width + each.rect.width)/2:
            col_balls.append(each)

    return col_balls
          
def main():
    pygame.init()

    ball_image =  '2.png'
    back_ground = '4.jpg'

    #可以游戏成功或者失败就结束，不用用户点击退出

    bg_size = width, height = 600, 400
    running = True
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption('play the ball')
    #载入背景图片
    background = pygame.image.load(back_ground).convert_alpha() 

    group = pygame.sprite.Group()
    
    balls =[]
    
    for i in range(5):
        #position 是个二元组 -100是减去ball的半径
        position = randint(0,width-100),randint(0, height-100)
        speed = [randint(-10,10), randint(-10,10)]
        #实例化对象
        ball = Ball(ball_image,position, speed, bg_size)

        while pygame.sprite.spritecollide(ball, group, False ):
            ball.rect.left, ball.rect.top = randint(0,width-100),randint(0,height-100)

        balls.append(ball)
        group.add(ball)#未碰撞/碰撞已解决 加入group中

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

        for i in range(5):
            if pygame.sprite.spritecollide(i, group, False):
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]                

            group.add(i)

        pygame.display.flip()
        clock.tick(30)
        


        
if __name__ == '__main__':
    main()
