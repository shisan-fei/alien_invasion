import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''单个入侵者的类'''

    def __init__(self,ai_setting,screen):
        '''初始化外星人和设置位置'''
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        #加载外星人图像，设置rect值
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人都从左上角出现
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人准确位置
        self.x = float(self.rect.x)

    def blitem(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image,self.rect)