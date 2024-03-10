import pygame
from abc import ABC,abstractmethod

from .IComponent import IComponent
from pygameEasy.Vector import Vector

from .IEventBinder import IEventBinder
from .IEventListener import IEventListener

class IGameObject(pygame.sprite.DirtySprite,ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError()
    
    @property
    @abstractmethod
    def component(self) -> IComponent:
        pass
    
    @component.setter
    @abstractmethod
    def component(self, component: IComponent) -> None:
        pass
    
    @property
    @abstractmethod
    def position(self) -> Vector:
        pass
    
    @abstractmethod
    def get_event_listener(self, type:str) -> IEventListener:
        pass
    
    @abstractmethod
    def get_event_binder(self, type:str) -> IEventBinder:
        pass