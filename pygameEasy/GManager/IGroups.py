import pygame
import abc

from .IObjectGroup import IObjectGroup

class IGroups(metaclass = abc.ABCMeta):
    @abc.abstractclassmethod
    def add_group(self, group: IObjectGroup):
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def init(self) -> None:
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def update(self) -> None:
        pass