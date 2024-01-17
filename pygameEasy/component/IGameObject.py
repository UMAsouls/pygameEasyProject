import pygame
import abc

from .IComponent import IComponent
from pygameEasy.Vector import Vector

class IGameObject(pygame.sprite.DirtySprite, metaclass = abc.ABCMeta):
    @property
    @abc.abstractclassmethod
    def name(self) -> str:
        raise NotImplementedError()
    
    @property
    @abc.abstractclassmethod
    def component(self) -> IComponent:
        pass
    
    @component.setter
    @abc.abstractclassmethod
    def component(self, component: IComponent) -> None:
        pass
    
    @property
    @abc.abstractclassmethod
    def position(self) -> Vector:
        pass