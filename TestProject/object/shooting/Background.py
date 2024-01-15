import pygame

from pygameEasy.GameObject import GameObject

class Background(GameObject):
    def set_data(self, data):
        super().set_data(data)
        
        size = pygame.display.get_surface().get_size()
        
        self.bgm = self._music.get_sound("bgm.ogg")
        
        self.size = size
        self._music.play_bgm(self.bgm)
        
    def update(self):
        super().update()
        
        if self._key.get_key_down("back"):
            self._scene_loader.scene_load("title.json")
        
        