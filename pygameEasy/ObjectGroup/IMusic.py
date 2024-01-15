import pygame
from pygame.locals import *
from pygame.mixer import *

import abc


class IMusic(metaclass = abc.ABCMeta):
    
    @abc.abstractclassmethod
    def get_sound(self, path: str) -> Sound:
        pass
    
    @abc.abstractclassmethod
    def play_bgm(self, sound: Sound) -> None:
        pass
    
    @abc.abstractclassmethod
    def play_effect(self, sound: Sound, maxtime: int = 0) -> None:
        pass
    
    @abc.abstractclassmethod
    def stop_bgm(self, fadetime: int = 0) -> None:
        pass