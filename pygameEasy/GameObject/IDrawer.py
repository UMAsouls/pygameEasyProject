from typing import List, Optional
import pygame
import abc

from pygame.rect import Rect
from pygame.surface import Surface

class IDrawer(pygame.sprite.LayeredDirty, metaclass = abc.ABCMeta):
    
    @abc.abstractclassmethod
    def draw(self, screen: Surface) -> List[Rect]:
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def update(self) -> None:
        raise NotImplementedError