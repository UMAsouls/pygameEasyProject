import pygame

from pygameEasy import *


class BulletEffect(GameObject):
    def start(self):
        
        self.clock = pygame.time.Clock()
        self.t = 0
        self.change_pivot("center")
        
    def update(self):
        super().update()
        
        self.clock.tick()
        self.t += self.clock.get_time() / 1000
        
        if (self.t >= 1.0):
            self.kill()