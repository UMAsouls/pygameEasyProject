import pygame
import abc

class IGameObject(pygame.sprite.DirtySprite, metaclass = abc.ABCMeta):
    @abc.abstractclassmethod
    def set_data(self, data) -> None:
        raise NotImplementedError()