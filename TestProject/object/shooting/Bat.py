import pygame
from pygame import locals
import os
import math

from pygameEasy import *


class Bat(GameObject):

    def hit(self, obj):
        obj.set_velocity(10,-90)

    def set_data(self, data):
        super().set_data(data)

        if "speed" in data:
            self.speed = data["speed"]

        raw_size = [270,180]
        disp_size = pygame.display.get_surface().get_size()
        
        self.size = [
            raw_size[0] * disp_size[0] // 1920,
            raw_size[1] * disp_size[1] // 1080
        ]
        
        self.rect = self.image.get_rect(center = self.rect.center)
        self.copy = self.image.copy()
        self.visible = False
        
        self.change_pivot("center")
        self.radius = 180
        self.position = [100,50]    #親positionとの相対位置
        self.mode = 0
        
        self.music = Music.get_instance()
        self.key = Key.get_instance()
        
        self.swing = self.music.get_sound("light_saber1.mp3")
        self.stop = False
        
        self.clock = pygame.time.Clock()
        self.c_lim = 0.4
        self.count = self.c_lim
        
    def on_collide(self, obj: GameObject):
        pass

    def rotate_bat(self):
        if self.mode == 1 :
            self.visible = True
            self.angle += 360*self.clock.get_rawtime()//1000
            if self.angle >= 180:
                self.mode = 0
                self.count = 0
                
        elif self.mode == 2:
            self.visible = True
            self.angle -= 360*self.clock.get_rawtime()//1000
            if self.angle > 180 and self.angle  < 360:
                self.mode = 0
                self.count = 0
            
        else:
            self.visible = False
            self.angle = 0
            self.count += self.clock.get_time() / 1000


    def update(self):
        self.clock.tick()
        
        super().update()
        
        if self.stop:
            return

        self.vel = Vector(0,0)

        #self.position = obj.rect.center

        if self.key.get_key_down("enter"):
            if self.mode == 0 and self.count >= self.c_lim:
                self.mode = 1
                self.music.play_effect(self.swing)
                
                
        if self.key.get_key_down("R_shift"):
            if self.mode == 0 and self.count >= self.c_lim:
                self.mode = 2
                self.angle = 180
                self.music.play_effect(self.swing)
            
        if self.key.get_key_up("enter"):
            pass
        
        self.rotate_bat()

        self.position = Vector(
            self.radius*math.cos(math.radians(self.angle)),
            -1*self.radius*math.sin(math.radians(self.angle))
        )