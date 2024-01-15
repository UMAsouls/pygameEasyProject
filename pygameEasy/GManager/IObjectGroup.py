import pygame
import abc

from .IGameobject import IGameObject

class IObjectGroup(pygame.sprite.LayeredDirty, metaclass = abc.ABCMeta):
    pass