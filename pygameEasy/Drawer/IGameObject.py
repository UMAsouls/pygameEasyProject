import pygame
import abc

class IGameObject(pygame.sprite.DirtySprite, metaclass = abc.ABCMeta):
    
    @property
    def rect(self) -> pygame.Rect:
        pass
    
    @property
    def changed(self) -> bool:
        pass
    
    @abc.abstractclassmethod
    def on_collide(self, obj: "IGameObject") -> None:
        pass