import pygame
from abc import ABC, abstractmethod

from . import IGameObject

class IComponent(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    
    @property
    @abstractmethod
    def main(self) -> IGameObject:
        raise NotImplementedError()
    
    @abstractmethod
    def get_kid(self, name: str) -> "IComponent":
        pass