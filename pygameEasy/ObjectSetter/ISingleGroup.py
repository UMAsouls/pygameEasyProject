import pygame
import abc

class ISingleGroup(metaclass = abc.ABCMeta):
    
    @property
    @abc.abstractclassmethod
    def parent(self) -> "ISingleGroup":
        pass
    
    @parent.setter
    @abc.abstractclassmethod
    def parent(self, component: "ISingleGroup") -> None:
        pass
    
    @property
    @abc.abstractclassmethod
    def kids(self) -> list:
        pass
    