import pygame
from abc import ABC, abstractmethod

class IObjectGroup(pygame.sprite.LayeredDirty, ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def update(self) -> None:
        pass
    
    @abstractmethod
    def event_check(self) -> None:
        pass
    
