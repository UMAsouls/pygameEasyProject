import pygame
from pygame.locals import *
import os
import copy

from pygameEasy.GameObject import GameObject
from .Bullet import Bullet
from pygameEasy.Vector import Vector

class Base(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        self.hp = 100
        self.max_hp = self.hp
        
        disp_rect = pygame.display.get_surface().get_rect()
        
        self.damaged = False
        self.inv_max = 0.8
        self.inv_time = self.inv_max
        
        self.size = [disp_rect.size[0], disp_rect.size[1]//8]
        
        self.clock = pygame.time.Clock()
        
        self.change_pivot("bottomleft")
        
        self.position = disp_rect.bottomleft

    def on_collide(self, obj: GameObject):
        if isinstance(obj, Bullet):
            if not self.damaged and obj.mode != -1:
                self.hp -= 10 
                self.damaged = True
                obj.bomb()
                
    def get_hp_ratio(self) -> float:
        return self.hp/self.max_hp

        
    def update(self):
        self.clock.tick()
        super().update()
        #print("Hp",self.hp, self.inv_time)
        if(self.damaged):
            self.inv_time -= self.clock.get_time()/1000
            if(self.inv_time < 0):
                self.damaged = False
                self.inv_time = self.inv_max
                
        if(self.hp <= 0):
            self.kill()