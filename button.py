import pygame.font

class Button():
    def __init__(self,ai_setting,screen,msg):
        '''初始化按钮属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #按钮尺寸和属性
        self.width , self.heigth = 200,50      #按钮尺寸
        self.button_color = (10,70,115)    #按钮颜色
        self.text_color = (146,18,34)    #按钮上字颜色
        self.font = pygame.font.SysFont(None,48)    #指定字体

        #创建按钮rect属性，使其居中
        self.rect = pygame.Rect(0,0,self.width,self.heigth)
        self.rect.center = self.screen_rect.center

        #按钮的标签只需要创建一次
        self.prep_msg(msg)

    def prep_msg(self,msg):
        '''将msg渲染为图像，并在按钮中居中'''
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)   #font.render将msg中图像转换为文本。ture是否开启反锯齿功能
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''绘制一个用颜色填充的按钮，再绘制文本'''
        self.screen.fill(self.button_color,self.rect)     #绘制按钮
        self.screen.blit(self.msg_image,self.msg_image_rect)   #绘制文本，给按钮传递一个图像