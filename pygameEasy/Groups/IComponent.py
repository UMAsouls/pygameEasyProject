import pygame
import abc

from . import IGameObject

class IComponent(metaclass = abc.ABCMeta):
    @property
    @abc.abstractclassmethod
    def name(self) -> str:
        pass
    
    @property
    @abc.abstractclassmethod
    def main(self) -> IGameObject:
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def get_kid(self, name: str) -> "IComponent":
        pass