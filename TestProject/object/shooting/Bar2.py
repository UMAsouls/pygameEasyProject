import pygame

from pygameEasy.GameObject import GameObject

class Bar2(GameObject):
    def set_data(self, data):
        super().set_data(data)
        
        size = pygame.display.get_surface().get_size()
        
        self.position = [100, size[1]*8/10]