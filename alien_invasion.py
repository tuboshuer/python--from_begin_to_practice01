import sys
import pygame
from settings import Settings

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #设置背景色
        self.bg_color = (230,230,230)

    def run_game(self):
        """start game"""
        while True:
            #监听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #每次循环时都重新绘制屏幕
            self.screen.fill(self.settings.bg_color)
            #让最近绘制的屏幕可见
            pygame.display.flip()
            #确保这个循环每秒运行60次，tick参数为帧率
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
        