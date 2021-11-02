import sys
import pygame
from settings import Setting  #导入配置类
from ship import Ship     #导入ship类
from alien import Alien   #导如Alien
import game_functions as gf
from pygame.sprite import Group   #Group类似一个列表
'''程序主文件：创建游戏所需要的对象，主循环'''

def run_game():
    pygame.init()              #pygame初始化
    ai_setting = Setting()     #将配置类进行实例化
    # screen = pygame.display.set_mode((1280,720))   #创建窗口
    screen = pygame.display.set_mode(
        (ai_setting.screen_width,ai_setting.screen_hight)
    )  #调用配置文件中定义的属性
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen,ai_setting)              #创造一个飞船
    bullets = Group()     #创建实例
    alien = Alien(ai_setting, screen)   #创建外星人

    while True:
        gf.check_events(ai_setting,screen,ship,bullets)      #导入事件检查
        ship.update()  # 移动图像
        gf.update_bullets(bullets)
        gf.update_screen(ai_setting,screen,ship,alien,bullets)     #导入屏幕更新图像


run_game()