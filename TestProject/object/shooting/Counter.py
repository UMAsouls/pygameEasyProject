import pygame

from pygameEasy import *

class Counter(TextObject):
    def set_data(self, data) -> None:
        super().set_data(data)
        
        
        self.clock = pygame.time.Clock()
        
        self.count = data["count"]
        
    def update(self) -> None:
        self.clock.tick()
        self.text = f"{self.count}"[:5]
        
        self.count -= self.clock.get_rawtime() / 1000