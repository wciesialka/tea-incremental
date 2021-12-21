'''Screen Element ABC'''

from abc import ABC, abstractmethod
import pygame

class ScreenElement(ABC):

    def __init__(self, size, position):
        self.surface = pygame.Surface(size)
        self.position = position

    @abstractmethod
    def draw(self, game):
        pass

    def render(self, game):
        self.draw(game)
        return self.surface