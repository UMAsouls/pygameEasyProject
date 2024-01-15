import pygame
from pygame.locals import *
from pygame.mixer import *

import abc


class IMusic(metaclass = abc.ABCMeta):
    
    @abc.abstractclassmethod
    def set_path(self, path: str) -> None:
        pass
    
    @abc.abstractclassmethod
    def update(self) -> None:
        pass
    
    