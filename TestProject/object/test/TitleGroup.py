import pygame
import sys

from .TestText import TestText

from pygameEasy.ObjectGroup import ObjectGroup

class TitleGroup(ObjectGroup):
    def set_data(self, data):
        super().set_data(data)

        self.object_count = 0
        
    def update(self):
        super().update()

        if self._key.get_key_down("up"):
            if self.object_count == 1:
                self.object.color = (255,255,255,0)
                self.object = self.get_obj_by_id("text1")
                self.object.color = (255,0,0,0)
            else:
                self.object = self.get_obj_by_id("text1")
                self.object.color = (255,0,0,0)
                self.object_count = 1
        
        if self._key.get_key_down("down"):
            if self.object_count == 1:
                self.object.color = (255,255,255,0)
                self.object = self.get_obj_by_id("text2")
                self.object.color = (255,0,0,0)
            else:
                self.object = self.get_obj_by_id("text2")
                self.object.color = (255,0,0,0)
                self.object_count = 1
        
        if self._key.get_key_down("enter"):
            if self.object.name == "text1":
                self._scene_loader.scene_load("test5.json")
            elif self.object.name == "text2":
                pygame.quit()
                sys.exit()