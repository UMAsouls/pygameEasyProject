import pygame
import abc

class ISingleGroup(metaclass = abc.ABCMeta):
    @abc.abstractclassmethod
    def position_set(self) -> None:
        pass