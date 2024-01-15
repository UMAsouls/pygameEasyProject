import pygame
from pygame import locals
import os
import math

from pygameEasy.GameObject import GameObject
from pygameEasy.Vector import Vector

from .Bat import Bat
#from .Base import Base

class Bullet(GameObject):
    def set_data(self, data):
        super().set_data(data)

        self.t = 0
        self.mode = 0
        
        self.lim_rect = pygame.display.get_surface().get_rect().copy()
        self.disp_rect = pygame.display.get_surface().get_rect().copy()
        
        self.lim_rect.size = [self.lim_rect.right + 200, self.lim_rect.bottom + 20]
        
        self.lim_rect.midbottom = self.disp_rect.midbottom
        
        self.vel = Vector(2000,-90)
        
        self.clock = pygame.time.Clock()
        
        self.hit = self._music.get_sound("damage.ogg")
        self.ref_effect = self._music.get_sound("damaged7.mp3")
        self.shooter = self._groups.get_single_by_name("attack")
        
        self.effect_data = data["effect"]
        
        self.change_pivot("center")

    def set_position(self, x, y):
        self._position = (x, y)

    def set_velocity(self, speed, angle):
        x = speed * math.cos(math.radians(angle))
        y = speed * -1*math.sin(math.radians(angle))
        self.vel = Vector(x,y)
    
    #ストレート       
    def set_velocity_street(self):
        self.set_velocity(550, -90)

    #カーブ
    def set_velocity_crave(self, gravity):
        self.set_velocity(900,-30)
        vx0 = self.vel.x
        vy0 = self.vel.y
        
        dx_dt = -gravity * self.t + vx0
        dy_dt = vy0

        self.vel = Vector(dx_dt, dy_dt)
        self.t += self.clock.get_time() /1000

    #逆カーブ
    def set_velocity_uncrave(self, gravity):
        self.set_velocity(900,-150)
        vx0 = self.vel.x
        vy0 = self.vel.y
        
        dx_dt = gravity * self.t + vx0
        dy_dt = vy0

        self.vel = Vector(dx_dt, dy_dt)
        self.t += self.clock.get_time() /1000

    #行って戻って
    def set_velocity_goback(self, gravity):
        self.set_velocity(300,-270)
        vx0 = self.vel.x
        vy0 = self.vel.y

        dy_dt = gravity * self.t + vy0
        dx_dt = vx0 * self.t

        self.vel = Vector(dx_dt, dy_dt)
        self.t += self.clock.get_time() /1000

    #反射
    def reflect(self, angle_ref):
        self._music.play_effect(self.ref_effect)
        self.vel.x = (self.vel.x **2 + self.vel.y **2 ) **0.5 * math.cos(math.radians(angle_ref + 90))
        self.vel.y = -1 * (self.vel.x **2 + self.vel.y **2 ) **0.5 * math.sin(math.radians(angle_ref + 90))
        self.mode = -1
        
        
    def lockon(self, pos:Vector):
        d_angle = (pos - self.position).angle()
        v_angle = self.vel.angle()
        
        if(d_angle > v_angle):
            v_angle += 360
        direction = v_angle - d_angle
    
        
        if(direction > 90 and direction < 180):
            self.acc = Vector.get_by_polar(500, self.vel.angle() + 90)
            print(1, direction, self.acc)
        elif(direction >= 180 and direction < 270):
            self.acc = Vector.get_by_polar(500, self.vel.angle() - 90)
            print(2, direction, self.acc)
        else:
            self.acc = (pos-self.position).normalize()*1000
            print(3,direction, self.acc)
            
        self.vel += self.acc*self.clock.get_time()/1000
        
    def chase(self):
        
        self.vel += self.acc*self.clock.get_time()/1000
        
        
        
    def bomb(self):
        self._music.play_effect(self.hit)
        effect = self._obj_setter.make_obj(self.effect_data)
        effect.position = self.position
        self._drawer.add(effect)
        self.kill()
        
    def on_collide(self, obj: GameObject):
        if isinstance(obj, Bat):
            if self.mode != -1:
                if obj.mode == 1:
                    self.reflect(obj.angle)
                elif obj.mode == 2:
                    self.reflect(obj.angle - 180)
            
           
    def update(self):
        self.clock.tick()
        super().update()
        if self.mode == 1:
           self.set_velocity_street()

        elif self.mode == 2:
            self.set_velocity_crave(900)

        elif self.mode == 3:
            self.set_velocity_uncrave(900)

        elif self.mode == 4:
            self.set_velocity_goback(800)
            
        elif self.mode == -1:
            self.lockon(self.shooter.position)
            
        self.angle = 360 - (self.vel.angle() - 90) + 180

        self._position += self.vel * self.clock.get_rawtime() / 1000
        
        if not self.lim_rect.colliderect(self.rect):
            self.kill()