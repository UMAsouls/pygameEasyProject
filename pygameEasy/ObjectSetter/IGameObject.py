import pygame
import abc

from typing import Any

from .ISingleGroup import ISingleGroup

class IGameObject(metaclass = abc.ABCMeta):
    
    @abc.abstractclassmethod
    def set_data(self, data: dict[str, Any]) -> None:
        pass
    
    @property
    @abc.abstractclassmethod
    def component(self) -> ISingleGroup:
        pass
    
