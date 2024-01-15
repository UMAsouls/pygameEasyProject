import pygame
import abc

class IObjectGroup(pygame.sprite.LayeredDirty, metaclass = abc.ABCMeta):
    pass