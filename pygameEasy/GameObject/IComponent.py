from abc import ABC,abstractmethod

from . import IGameObject
from pygameEasy.Vector import Vector

class IComponent(ABC):
    @property
    @abstractmethod
    def main(self) -> IGameObject:
        pass
    
    @main.setter
    @abstractmethod
    def main(self, value: "IComponent") -> None:
        pass
    
    @property
    @abstractmethod
    def parent(self) -> "IComponent":
        pass
    
    @property
    @abstractmethod
    def root(self) -> "IComponent":
        pass
    
    @property
    @abstractmethod
    def position(self) -> Vector:
        pass
    
    @abstractmethod
    def position_set(self) -> None:
        pass
    
    @abstractmethod
    def get_kid(self, name:str) -> "IComponent":
        pass
    
    @abstractmethod
    def kill(self) -> None:
        pass
    
    