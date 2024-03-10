import pygame
from abc import ABC, abstractmethod

class IGameObject(pygame.sprite.DirtySprite, ABC):
    
    @property
    @abstractmethod
    def rect(self) -> pygame.Rect:
        pass
    
    @property
    @abstractmethod
    def changed(self) -> bool:
        pass
    
    @abstractmethod
    def on_collide(self, obj: "IGameObject") -> None:
        pass
    
    @abstractmethod
    def get_onscreen_rect(self, camera: "IGameObject") -> pygame.Rect:
        pass
    
    @abstractmethod
    def setup(self) -> None:
        pass
    
    @abstractmethod
    def start(self) -> None:
        pass
    
    