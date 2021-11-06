import sys
import pygame
from bullet import Bullet
from alien import Alien
from settings import Setting  #导入配置类
from time import sleep

'''将程序主要函数存放，减轻alien_invasion中run_game代码量'''

def check_keydown_events(ship,event,ai_setting,bullets,screen):
    '''响应按下按键'''
    if event.key == pygame.K_RIGHT:  # 如果是向右的话
        # 飞船右移
        # ship.rect.centerx +=1
        ship.moving_right = True  # 将moving_right这个成员属性置为Ture，x轴自动加一
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #创建一个子弹，放入编组bullets
        fire_bullet(ai_setting,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(ship,event):
    '''响应松开按键'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_setting,screen,ship,bullets):
    '''相应键盘和鼠标事件，控制飞机左右移动'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #检测到退出就退出游戏
            sys.exit()
        elif event.type == pygame.KEYDOWN:    #检测键盘键入属性,KEYDOWN按下键盘
            check_keydown_events(ship, event,ai_setting,bullets,screen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)

def update_screen(ai_setting,screen,stats,ship,aliens,bullets,play_button):
    '''
    更新屏幕图像
    :param ai_setting: 配置参数的实例化对象
    :param screen: 窗口
    :param ship: 飞船
    '''
    screen.fill(ai_setting.bg_color)
    #在飞船后重新绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitem()  # 绘制飞船
    aliens.draw(screen)    #对编组调用draw，pygame自动绘制编组图像

    #游戏处于非活动状态时绘制play按钮
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(ai_setting,screen,ship,aliens,bullets):
    '''更新子弹位置，删除一消失的子弹'''
    bullets.update()  #移动子弹
        #删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    '''检查是否有子弹集中外星人，之后删除子弹和外星人'''
    check_bullet_alien_collisions(ai_setting,screen,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_setting,screen,ship,aliens,bullets):
    '''响应子弹和外星人碰撞 删除碰撞后的子弹和外星人'''
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) == 0:
        #删除现有的子弹并创建一群外星人
        bullets.empty()
        create_fleet(ai_setting,screen,ship,aliens)

def fire_bullet(ai_setting,screen,ship,bullets):
    '''玩家发射子弹'''
    '''发射子弹前判断是否达到限制'''
    if len(bullets) < ai_setting.bullets_allowed:   #判断当前子弹编组数量是否小于设置的最大子弹数量
            new_bullet = Bullet(ai_setting,screen,ship)
            bullets.add(new_bullet)


def get_number_aliens_x(ai_setting,alien_width):
    '''计算一行容纳外星人数量'''
    available_space_x = ai_setting.screen_width - 2 * alien_width   #容纳外星人的宽度
    number_aliens_x = int(available_space_x / (2 * alien_width))     #容纳外星人数量
    return number_aliens_x

def create_alien(ai_setting,screen,aliens,alien_number,row_number):
    '''创建一个外星人放在当前行'''
    alien = Alien(ai_setting,screen)
    alien_width = alien.rect.width   #外星人宽度
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.add(aliens)

def get_number_rows(ai_setting,ship_height,alien_heigth):
    '''计算屏幕可容纳外星人数量'''
    available_space_y = (ai_setting.screen_height - (3 * alien_heigth) - ship_height)
    number_rows = int(available_space_y / (2 * alien_heigth))
    return number_rows

def create_fleet(ai_setting,screen,ship,aliens):
    '''创建外星人群组'''
    alien = Alien(ai_setting,screen)
    number_aliens_x = get_number_aliens_x(ai_setting,alien.rect.width)
    number_rows = get_number_rows(ai_setting,ship.rect.height,alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_setting,screen,aliens,alien_number,row_number)

def update_aliens(ai_setting,stats,screen,ship,aliens,bullets):
    '''检查外星人是否在边缘，更新位置'''
    check_fleet_edges(ai_setting,aliens)
    aliens.update()
    #检查飞船和外星人碰撞
    if pygame.sprite.spritecollideany(ship,aliens):   #spritecollideany接受精灵和编组，检查是否相互碰撞，找到碰撞的编组成员，停止遍历
        print('ship hit!!!')
        ship_hit(ai_setting,stats,screen,ship,aliens,bullets)
    #检查外星人碰到底部时
    check_aliens_bottom(ai_setting,stats,screen,ship,aliens,bullets)

def check_fleet_edges(ai_setting,aliens):
    '''外星人到边缘时措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting,aliens)
            break

def change_fleet_direction(ai_setting,aliens):
    '''将整群外星人下移，改变方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1

def ship_hit(ai_setting,stats,screen,ship,aliens,bullets):
    '''响应外星人撞到飞船'''
    if stats.ship_left > 0:
        stats.ship_left -= 1

         #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新外星人
        create_fleet(ai_setting,screen,ship,aliens)
        ship.center_ship()

        #暂停
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(ai_setting,stats,screen,ship,aliens,bullets):
    '''检查是否有外星人到达底端'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #执行飞船被撞一样的处理
            ship_hit(ai_setting,stats,screen,ship,aliens,bullets)
            break



