import pygame
from pygame.locals import *


from pygameEasy.GameObject import GameObject
from pygameEasy.Vector import Vector


class TestTitle(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        self.size = pygame.display.get_surface().get_size()
        
    def update(self):
        super().update()