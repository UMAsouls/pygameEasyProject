import pygame
from pygame.locals import *
import os

from pygameEasy import *

class TitleText2(TextObject):
    def set_data(self, data) -> None:
        super().set_data(data)
        
        size = pygame.display.get_surface().get_size()
        
        self.change_pivot("center")
        self.position = Vector(size[0]//2, self.position.y)
        
        select = self.EventBinder("select")
        select.set_func(self.color_change_red)
        change = self.EventBinder("change")
        change.set_func(self.color_change_white)
        
        self.set_event_binder("select", select)
        self.set_event_binder("change", change)
        
    
    def color_change_red(self) -> None:
        self.color = (255,0,0,0)
        
    def color_change_white(self) -> None:
        self.color = (255,255,255,0)
        
    def update(self):
        super().update()