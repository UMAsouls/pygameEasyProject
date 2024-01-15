import pygame
import abc

class IObjectGroup(pygame.sprite.LayeredDirty, metaclass = abc.ABCMeta):
    @property
    @abc.abstractclassmethod
    def name(self) -> str:
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def update(self) -> None:
        pass
    
