import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):   #继承Sprite类
    '''对发射的子弹进行管理'''
    def __init__(self,ai_setting,screen,ship):
        '''在飞船所在位置创建一个子弹对象'''
        super(Bullet,self).__init__()    #类似super().__init__() 继承Sprite
        self.screen = screen

        #在（0，0）处创建一个子弹，再设置子弹位置
        self.rect = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx    #子弹从飞船顶部飞出，子弹centerx和top和飞船相同
        self.rect.top = ship.rect.top

        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        '''管理子弹位置，向上移动子弹'''
        self.y -= self.speed_factor    #更新子弹位置最小值
        self.rect.y = self.y      #更新子弹rect位置

    def draw_bullet(self):
        ''' 在屏幕绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)


