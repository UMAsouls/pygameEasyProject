import pygame
from pygame.locals import *
import os
import copy

from pygameEasy.GameObject import GameObject
from .TestBullet import TestBullet
from pygameEasy.Vector import Vector

class TestBase(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        self.hp = 100
        
        disp_rect = pygame.display.get_surface().get_rect()
        
        self.damaged = False
        self.inv_max = 50
        self.inv_time = self.inv_max
        
        self.size = [disp_rect.size[0], disp_rect.size[1]//8]
        
        self.change_pivot("bottomleft")
        
        self.position = disp_rect.bottomleft

    def on_collide(self, obj: GameObject):
        if isinstance(obj,TestBullet):
            if not self.damaged:
                self.hp -= 10 
                self.damaged = True

        
    def update(self):
        super().update()
        #print("Hp",self.hp, self.inv_time)
        if(self.damaged):
            self.inv_time -= 1
            if(self.inv_time < 0):
                self.damaged = False
                self.inv_time = self.inv_max
                
        if(self.hp < 0):
            self.kill()
        
        