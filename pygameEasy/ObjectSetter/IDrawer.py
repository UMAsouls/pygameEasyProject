import abc
import pygame

class IDrawer(pygame.sprite.LayeredDirty, metaclass = abc.ABCMeta):
    pass