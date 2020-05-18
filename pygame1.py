import pygame
import sys

#初始化
pygame.init()

size = width,height = 1000, 600#tuple
speed =[-2,1]
bg = (255,255,255)#背景色

#设置指定大小的窗口Surface
screen = pygame.display.set_mode(size)
#设置窗口标题
pygame.display.set_caption('初次见面，多多关照')

#加载图片Surface对象
photo = pygame.image.load('link.jpg')

#获得图像的位置矩形rectangle
position = photo.get_rect()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()#退出游戏  右上角X

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
    
