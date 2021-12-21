'''Home screen.'''

import pygame
import pygame.freetype
from tea_incremental.game.tea_game import TeaGame
from tea_incremental.interface.screen_element import ScreenElement

class HomeScreen(ScreenElement):

    FONT_NAME: str = "Arial"

    def __init__(self):
        super().__init__((400, 500), (100, 0))
        pygame.freetype.init()
        self.font = pygame.freetype.SysFont(HomeScreen.FONT_NAME, 12)

    def draw(self, game: TeaGame):
        self.surface.fill((244, 239, 248))
        leaves_surface, _ = self.font.render(f"Leaves: {game.leaves:1.1f}", (0, 0, 0))
        cash_surface, _ = self.font.render(f"Cash: ${game.cash:1.2f}", (0, 0, 0))
        self.surface.blit(leaves_surface, (3, 6))
        self.surface.blit(cash_surface, (3, 18))
