import pygame
from pygame.locals import *
import os
import copy

from pygameEasy.GameObject import TextObject
from pygameEasy.Vector import Vector

class TestText(TextObject):
    def set_data(self, data) -> None:
        super().set_data(data)
        self.pos_x = 0
        self.pos_y = 0
        
    def update(self):
        super().update()
        self.text = f"This is test {self.pos_x} {self.pos_y}"