import pygame
import game_functions as gf

class Ship():
    def __init__(self,screen,ai_setting):
        '''初始化飞机并设置初始位置'''
        self.screen = screen
        self.ai_setting = ai_setting
        #加载飞机图像并获取外界矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将飞机放到屏幕底部中间
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船属性center中存储最小数值
        self.center = float(self.rect.centerx)    #float 将值转换为最小数，存入center
        #移动标志
        self.moving_right= False
        self.moving_left = False
        self.moving_spac = False

    def blitem(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''根据标志调整飞船位置'''
        if self.moving_right:
            # self.rect.centerx +=1    #向右移动一位
            if self.moving_right and self.rect.right < self.screen_rect.right:  #rect.right飞船外接矩形x轴最大值。保证飞船不出边框
                self.center += self.ai_setting.ship_speed_factor    #更新飞船center值，不直接该rect
        if self.moving_left:
            # self.rect.centerx -=1
            if self.moving_left and self.rect.left > 0:         #左边不出边框
                self.center -= self.ai_setting.ship_speed_factor
        # if self.moving_spac:
        #     gf.fire_bullet(self.ai_setting,self.screen,ship,bullets)
        self.rect.centerx = self.center   #根据center更改rect