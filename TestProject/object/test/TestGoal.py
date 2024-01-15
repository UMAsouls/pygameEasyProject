import pygame
from pygame.locals import *
import os

from .TestObject import TestObject

from pygameEasy.GameObject import GameObject
from pygameEasy.Vector import Vector

class TestGoal(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        
    def on_collide(self, obj: GameObject):
        if isinstance(obj, TestObject):
            self._scene_loader.scene_load("test3.json")
        
    def update(self):
        super().update()
        
        