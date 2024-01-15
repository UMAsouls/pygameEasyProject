import pygame
from pygame.locals import *
import os

from pygameEasy.GameObject import GameObject
from pygameEasy.Vector import Vector

from .TestBullet import TestBullet

class TestObject(GameObject):
    
    def set_data(self, data):
        super().set_data(data)
        
        self.vel = Vector(0,0)

        self.ball = data["ball_data"]
        self.speed = data["speed"]
        self.hitpoint = 100
        
        self.change_pivot("center")


    def shoot(self , k):
        bullet: TestBullet  = self._obj_setter.make_obj(self.ball)
        bullet.position = self.position
        bullet.mode = k
        self._drawer.add(bullet)

    def on_collide(self, obj: GameObject):
        pass
       
    def update(self):
        super().update()
        self.vel = Vector(0,0)
        
        if(self._key.get_key_repeat("j")):
            self.vel += Vector(-1*self.speed,0)
        if(self._key.get_key_repeat("l")):
            self.vel += Vector(self.speed,0)
        if(self._key.get_key_repeat("i")):
            self.vel += Vector(0,-1*self.speed)
        if(self._key.get_key_repeat("k")):
            self.vel += Vector(0,self.speed)
            
            
        if(self._key.get_key_down("c")):
            self.shoot(1)

        if(self._key.get_key_down("v")):
            self.shoot(2)

        if(self._key.get_key_down("m")):
            self.shoot(3)

        if(self._key.get_key_down("n")):
            self.shoot(4)
            
        self.position += self.vel
            