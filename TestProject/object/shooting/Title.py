import pygame
from pygame.locals import *


from pygameEasy.GameObject import GameObject
from pygameEasy.Vector import Vector


class Title(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        self.size = pygame.display.get_surface().get_size()
        
        self.bgm = self._music.get_sound("title.ogg")
        self._music.play_bgm(self.bgm)
        
    def update(self):
        super().update()