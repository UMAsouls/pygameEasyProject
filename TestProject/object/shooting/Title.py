import pygame
from pygame.locals import *


from pygameEasy import *


class Title(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        self.size = pygame.display.get_surface().get_size()
        
        self.music = Music.get_instance()
        
        self.bgm = self.music.get_sound("title.ogg")
        self.music.play_bgm(self.bgm)
        
    def update(self):
        super().update()