import pygame
import abc

class IComponent(metaclass = abc.ABCMeta):
    @abc.abstractclassmethod
    def position_set(self) -> None:
        pass