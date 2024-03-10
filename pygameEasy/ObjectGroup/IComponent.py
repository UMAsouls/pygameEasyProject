import pygame
from abc import ABC,abstractmethod

class IComponent(ABC):
    @abstractmethod
    def position_set(self) -> None:
        pass
    
    @abstractmethod
    def get_kid(self, name:str) -> "IComponent":
        pass