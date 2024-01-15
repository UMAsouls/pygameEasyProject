import abc
import pygame

class IObjectGroup(pygame.sprite.LayeredDirty,metaclass = abc.ABCMeta):
    @property
    @abc.abstractclassmethod
    def name(self) -> str:
        raise NotImplementedError()
    
    @name.setter
    @abc.abstractclassmethod
    def name(self, name: str) -> None:
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def set_data(self, data: list):
        raise NotImplementedError()