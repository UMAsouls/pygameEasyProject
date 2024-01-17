from typing import Any, Iterable, Union
import pygame

from pygame.sprite import AbstractGroup

from . import IGameObject

from pygameEasy.Singleton import Singleton

class Drawer(pygame.sprite.LayeredDirty,Singleton):
    rect_list: list[pygame.Rect] = []
    
    @classmethod    
    def get_instance(cls) -> "Drawer":
        if cls._instance == None:
            cls._instance = cls.__internal_new__()
            cls.inited: bool = False
            pygame.sprite.LayeredDirty.__init__(cls._instance)
        
        return cls._instance
        
            
            
    def init(self) -> None:
        self.rect_list = []
        pygame.sprite.LayeredDirty.__init__(self)

    def draw(self, screen: pygame.Surface):
        rects = pygame.sprite.LayeredDirty.draw(self,screen)
        #pygame.display.update(self.rect_list)
        pygame.display.flip()
        self.rect_list = []
        return rects
    
    def sprites(self) -> list[IGameObject]:
        return super().sprites()
    
    def __rect_list_gen(self):
        for i in self.sprites():
            if i.changed:
                yield i.rect
        
    def update(self):
        for i in self.sprites():
            collides: list[IGameObject] = pygame.sprite.spritecollide(i,self,False)
            for j in collides:
                if i.visible:
                    i.on_collide(j)
        
        for i in self.sprites():
            i.update()
        
        self.rect_list = list(self.__rect_list_gen())
        
        
    def remove(self, *sprites: Any | AbstractGroup | Iterable) -> None:
        for i in sprites:
            self.rect_list.append(i.rect)
        super().remove(*sprites)
           
            
from pygameEasy.DependencyConfig import Config

configs = [
]
            
        