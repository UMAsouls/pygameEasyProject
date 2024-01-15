import pygame
import abc

from .IObjectGroup import IObjectGroup
from .IGameobject import IGameObject

class ISingleGroup(metaclass = abc.ABCMeta):
    @property
    @abc.abstractclassmethod
    def main(self, obj: IGameObject) -> None:
        raise NotImplementedError()