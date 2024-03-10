import pygame

from pygameEasy import *

class Bar2(GameObject):
    def start(self):
        
        size = pygame.display.get_surface().get_size()
        
        self.position = [100, size[1]*8/10]