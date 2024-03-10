import pygame

from pygameEasy import *

class Counter(TextObject):
    def start(self) -> None:
        self.clock = pygame.time.Clock()
        
        self.count = self.get_data("count")
        
    def update(self) -> None:
        self.clock.tick()
        self.text = f"{self.count}"[:5]
        
        self.count -= self.clock.get_rawtime() / 1000