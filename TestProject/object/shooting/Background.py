import pygame

from pygameEasy import *

class Background(GameObject):
    def start(self):
        
        size = pygame.display.get_surface().get_size()
        
        self.music = Music.get_instance()
        self.key = Key.get_instance()
        self.scene_loader = SceneLoader.get_instance()
        
        self.bgm = self.music.get_sound("bgm.ogg")
        
        self.size = size
        self.music.play_bgm(self.bgm)
        
    def update(self):
        super().update()
        
        if self.key.get_key_down("back"):
            self.scene_loader.scene_load("title.json")
        
        