import pygame
from abc import ABC, abstractmethod

from pygameEasy.Vector import Vector

class IGameObject(pygame.sprite.DirtySprite, ABC):
    @property
    @abstractmethod
    def position(self) -> Vector:
        pass
    
    @position.setter
    @abstractmethod
    def position(self, vec: Vector) -> None:
        pass