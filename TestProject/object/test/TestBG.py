import pygame
from pygame import locals
import os

from pygameEasy.GameObject import GameObject
from pygameEasy.Vector import Vector

class TestBG(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        
        self.time = 1
        
    def update(self):
        super().update()
        if(self.time < 0):
            self.moving = False
            
        else:
            self.time -= 1
        #test_sp : GameObject = self._groups.get_single_by_name("test")
        
        #print(test_sp.name)
    