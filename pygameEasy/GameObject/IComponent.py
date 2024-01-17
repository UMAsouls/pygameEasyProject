import abc

from . import IGameObject
from pygameEasy.Vector import Vector

class IComponent(metaclass = abc.ABCMeta):
    @property
    @abc.abstractclassmethod
    def main(self) -> IGameObject:
        pass
    
    @main.setter
    @abc.abstractclassmethod
    def main(self, value: "IComponent") -> None:
        pass
    
    @property
    @abc.abstractclassmethod
    def parent(self) -> "IComponent":
        pass
    
    @property
    @abc.abstractclassmethod
    def root(self) -> "IComponent":
        pass
    
    @property
    @abc.abstractclassmethod
    def position(self) -> Vector:
        pass
    
    @abc.abstractclassmethod
    def position_set(self) -> None:
        pass
    
    @abc.abstractclassmethod
    def get_kid(self, name:str) -> "IComponent":
        pass
    
    @abc.abstractclassmethod
    def kill(self) -> None:
        pass
    
    