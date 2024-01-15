import pygame
import abc

from .IGameobject import IGameObject

class IDrawer(pygame.sprite.LayeredDirty, metaclass = abc.ABCMeta):
    @abc.abstractclassmethod
    def init(self) -> None:
        raise NotImplementedError()