import pygame
from pygame.locals import *
import os
import copy

from pygameEasy.GameObject import GameObject
from pygameEasy.Vector import Vector
from .Bullet import Bullet

class Defense(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        
        self.vel = Vector(0,0)
        self.speed = data["speed"]
        
        self.change_pivot("center")
        
        size = pygame.display.get_surface().get_size()
        self.disp_size = size
        
        self.position = [size[0]/2, size[1]*7//10]
        
        self.pos_lim = [0, size[1] *5 / 9, size[0], size[1]]
        
        self._stop:bool = False
    
    @property
    def stop(self) -> bool:
        return self._stop
    
    @stop.setter
    def stop(self, v:bool) -> None:
        self._stop = v
        
    
        
    def update(self):
        super().update()
        self.vel = Vector(0,0)
        
        if self._stop:
            return
        
        if(self._key.get_key_repeat("j")) and self.rect.left >= self.pos_lim[0]:
            self.vel += Vector(-1*self.speed,0)
        if(self._key.get_key_repeat("l")) and self.rect.right <= self.pos_lim[2] :
            self.vel += Vector(self.speed,0)
        if self._key.get_key_repeat("i") and self.rect.top >= self.pos_lim[1]:
            self.vel += Vector(0,-1*self.speed)
        if self._key.get_key_repeat("k") and self.rect.bottom <= self.pos_lim[3]:
            self.vel += Vector(0,self.speed)
           
        self.position += self.vel