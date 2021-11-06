'''
定义一个Setting类，将所有设置存放在一个地方
'''
class Setting():
    '''存放本项目所有设置的类'''
    def __init__(self):
        '''初始化游戏设置'''
        #游戏边框大小颜色设置
        self.screen_width=1280
        self.screen_height= 720
        self.bg_color=(35,35,42)  #定义背景颜色，rgb值，分别是红色，绿色，蓝色
        self.ship_speed_factor=1.5     #飞船每次移动像素
        self.ship_limit = 3

        #发射子弹设置
        self.bullet_speed_factor = 3    #子弹速度
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = (19,221,33)
        self.bullets_allowed = 10      #单屏幕子弹最大数量

        #外星人设置
        self.alien_speed_factor = 0.5    #移动速度
        self.fleet_drop_speed = 5      #向下速度
        self.fleet_direction = 1 #1为向右-1为向左

 
