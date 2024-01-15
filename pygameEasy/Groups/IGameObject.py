import pygame
import abc

class IGameObject(pygame.sprite.DirtySprite, metaclass = abc.ABCMeta):
    pass