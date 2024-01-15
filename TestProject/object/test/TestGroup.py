import pygame


from .TestText import TestText

from pygameEasy.ObjectGroup import ObjectGroup

class TestGroup(ObjectGroup):
    def set_data(self, data):
        super().set_data(data)
        
        self.objects = self.sprites()
        
    def update(self):
        super().update()
        
        machine = self.get_obj_by_id("obj")
        bat = self.get_obj_by_id("bat")
        text: TestText = self.get_obj_by_id("text")
        
        pos = machine.position.change2list()
        
        text.pos_x = pos[0]
        text.pos_y = pos[1]
        
        
        
        