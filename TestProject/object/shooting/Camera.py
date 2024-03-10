import pygame

from pygameEasy import *

class Camera(GameObject):
    def set_data(self, data):
        super().set_data(data)

        self.drawer = Drawer.get_instance()
        self.drawer.set_camera(self)
        self.drawer.zoom = 100
        self.zoom = 100
        self.mode = True
        
        size = pygame.display.get_surface().get_size()
        self.change_pivot("center")
        self.position = Vector(size[0]/2, size[1]/2)
        
    def update(self):
        super().update()