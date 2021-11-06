import sys
import pygame
from settings import Setting  #导入配置类
from ship import Ship     #导入ship类
# from alien import Alien   #导如Alien
import game_functions as gf
from pygame.sprite import Group   #Group类似一个列表
from game_stats import GameStats

'''程序主文件：创建游戏所需要的对象，主循环'''

def run_game():
    pygame.init()              #pygame初始化
    ai_setting = Setting()     #将配置 类进行实例化
    # screen = pygame.display.set_mode((1280,720))   #创建窗口
    screen = pygame.display.set_mode(
        (ai_setting.screen_width,ai_setting.screen_height)
    )  #调用配置文件中定义的属性
    pygame.display.set_caption('Alien Invasion')

    #创建一个存储统计游戏信息的实例
    stats = GameStats(ai_setting)
    #创建一艘飞船，一个子弹编组，一个外星人编组
    ship = Ship(screen,ai_setting)              #创造一个飞船
    bullets = Group()     #创建实例,定义子弹编组
    aliens = Group()   #创建外星人编组
    gf.create_fleet(ai_setting,screen,ship,aliens)
    # alien = Alien(ai_setting, screen)   #创建外星人

    while True:
        gf.check_events(ai_setting,screen,ship,bullets)      #导入事件检查
        if stats.game_active:
            ship.update()  # 移动图像
            gf.update_bullets(ai_setting,screen,ship,aliens,bullets)
            gf.update_aliens(ai_setting,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_setting,screen,ship,aliens,bullets)     #导入屏幕更新图像


run_game()