import pygame
from pygame.locals import *
import os

from pygameEasy.GameObject import TextObject
from pygameEasy.Vector import Vector

class TitleText2(TextObject):
    def set_data(self, data) -> None:
        super().set_data(data)
        
        size = pygame.display.get_surface().get_size()
        
        self.change_pivot("center")
        self.position = Vector(size[0]//2, self.position.y)
        
        
        
    def update(self):
        super().update()