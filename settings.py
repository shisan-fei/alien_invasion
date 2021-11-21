'''
定义一个Setting类，将所有设置存放在一个地方
'''
# from _typeshed import Self
from pygame.mouse import set_visible


class Setting():
    '''存放本项目所有设置的类'''
    def __init__(self):
        '''初始化游戏静态设置'''
        #游戏边框大小颜色设置
        self.screen_width=1280
        self.screen_height= 720
        self.bg_color=(35,35,42)  #定义背景颜色，rgb值，分别是红色，绿色，蓝色
        self.ship_speed_factor=1.5     #飞船每次移动像素

        #飞船设置
        self.ship_limit = 1

        #发射子弹设置
        self.bullet_speed_factor = 3    #子弹速度
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (19,221,33)
        self.bullets_allowed = 10      #单屏幕子弹最大数量

        #外星人设置
        # self.alien_speed_factor = 1.5    #移动速度
        self.fleet_drop_speed = 10      #向下速度
        # self.fleet_direction = 1 #1为向右-1为向左

        '''以什么样的速度加快游戏速度'''
        self.speedup_scale=1.1    #控制游戏加快速度
        self.initialize_dynamic_settings()   #每提高一个等级，游戏速度翻倍

    def initialize_dynamic_settings(self):
        '''初始化随着游戏变化而变化的值'''
        self.ship_speed_factor = 1.5    #移动速度
        self.bullet_speed_factor  = 3   #子弹速度
        self.alien_speed_factor = 1    #外星人移动速度

        self.fleet_direction = 1

    def increase_speed(self):
        '''提高速度设置'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

 
