'''Screen controller.'''

import pygame
from tea_incremental.game.tea_game import TeaGame

class Screen:

    '''Tea Incremental screen.'''

    WIDTH: int = 500
    HEIGHT: int = 500

    def __init__(self, game: TeaGame):
        pygame.init()
        self.display: pygame.Surface = pygame.display.set_mode((500, 500))
        self.game: TeaGame = game

    def dispose(self):
        '''Do anything we need to do before quitting.'''
        pygame.quit()

    def __del__(self):
        self.dispose()

    def draw(self):
        '''Draw the contents of the screen to the display.'''
        self.display.fill((255, 255, 255))

        pygame.display.flip()