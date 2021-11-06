class GameStats():
    '''跟踪游戏统计信息'''
    def __init__(self,ai_setting):
        '''初始化统计信息'''
        self.ai_setting = ai_setting
        self.reset_stats()
        self.game_active = False   #游戏状态

    def reset_stats(self):
        '''初始化游戏期间可能变化的统计信息'''
        self.ship_left = self.ai_setting.ship_limit
