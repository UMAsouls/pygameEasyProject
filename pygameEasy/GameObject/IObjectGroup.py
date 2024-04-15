import abc
import pygame

class IObjectGroup(pygame.sprite.LayeredDirty,metaclass = abc.ABCMeta):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        raise NotImplementedError()
    
    @name.setter
    @abc.abstractmethod
    def name(self, name: str) -> None:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def set_data(self, data: list):
        raise NotImplementedError()