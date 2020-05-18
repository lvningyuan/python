import pygame
import sys
from pygame.locals import *


#初始化
pygame.init()

size = width,height = 1000, 600#tuple
speed =[-2,1]
bg = (255,255,255)#背景色

fullscreen = False

#设置指定大小的窗口Surface , 第二个参数为用户可修改窗口大小
screen = pygame.display.set_mode(size,RESIZABLE)
#设置窗口标题
pygame.display.set_caption('初次见面，多多关照')

#加载图片Surface对象
photo = pygame.image.load('link.jpg')

#获得图像的位置矩形rectangle
position = photo.get_rect()

photo = photo = pygame.transform.flip(photo, True, False)

r_head = photo
l_head =  photo = pygame.transform.flip(photo, True, False)

#获取用户的分辨率
resolution = pygame.display.list_modes()[15]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()#退出游戏  右上角X
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                speed = [-1,0]
                photo = l_head
            if event.key == K_RIGHT:
                speed = [1,0]
                photo = r_head
            if event.key == K_UP:
                speed = [0,-1]
            if event.key == K_DOWN:
                speed = [0,1]
            
            #全屏模式，：注意分辨率
            if event.key == K_k:
                fullscreen = not fullscreen
                if fullscreen == True:
                    screen = pygame.display.set_mode(resolution, FULLSCREEN | HWSURFACE)
                else:
                    screen = pygame.display.set_mode(size)

        #用户调整窗口大小video resize 事件
        if event.type ==  VIDEORESIZE:
            size == event.size
            width , height = size
            print(size)
            screen = pygame.display.set_mode(size,RESIZABLE)

    #移动图像
    position = position.move(speed)

    #碰撞检测:水平方向
    if position.left < 0 or position.right > width:
        #翻转图像   翻转谁， 水平翻转吗？ 垂直翻转吗？
        photo = pygame.transform.flip(photo, True, False)
        # 水平翻转 ：反方向移动  
        speed[0] = -speed[0]

    #碰撞检测:垂直方向
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    #背景填充
    screen.fill(bg)
    #更新背景
    screen.blit(photo,position)
    #更新界面
    pygame.display.flip()
    #设置延迟
    pygame.time.delay(1)
    
