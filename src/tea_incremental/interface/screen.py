'''Screen controller.'''

import pygame
import pygame.freetype
from tea_incremental.game.tea_game import TeaGame
from tea_incremental.interface.home import HomeScreen 
class Screen:

    '''Tea Incremental screen.'''

    WIDTH: int = 500
    HEIGHT: int = 500

    def __init__(self, game: TeaGame):
        pygame.init()
        self.display: pygame.Surface = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
        self.game: TeaGame = game
        self.children = [HomeScreen()]

    def dispose(self):
        '''Do anything we need to do before quitting.'''
        pygame.quit()

    def __del__(self):
        self.dispose()

    def draw(self):
        '''Draw the contents of the screen to the display.'''
        self.display.fill((255, 255, 255))

        for child in self.children:
            surf = child.render(self.game)
            self.display.blit(surf, child.position)

        pygame.display.flip()