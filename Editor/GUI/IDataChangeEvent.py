from abc import ABC, abstractmethod
from pygame.event import Event
from queue import Queue

class IDataChangeEvent(ABC):
    
    @property
    @abstractmethod
    def key(self) -> str:
        pass
    
    @property
    @abstractmethod
    def idx(self) -> int:
        pass
    
    @property
    @abstractmethod
    def data(self) -> int| str:
        pass
    
    @abstractmethod
    def get_dict(self) -> dict:
        pass
    
    
    