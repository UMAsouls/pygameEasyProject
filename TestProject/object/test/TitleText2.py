import pygame
from pygame.locals import *
import os

from pygameEasy.GameObject import TextObject
from pygameEasy.Vector import Vector

class TitleText2(TextObject):
    def set_data(self, data) -> None:
        super().set_data(data)
        
    def update(self):
        super().update()