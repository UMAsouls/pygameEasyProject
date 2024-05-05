from abc import ABC, abstractmethod

from pygameEasy import *

class IEmulator(ABC):
    @abstractmethod
    def load(self, path:str) -> None:
        pass
    
    @abstractmethod
    def get_obj_selected(self) -> GameObject:
        pass
    
    @abstractmethod
    def select_by_id(self, id: str) -> None:
        pass
    
    @abstractmethod
    def event_update(self, event) -> None:
        pass
    
    @abstractmethod
    def update(self) -> None:
        pass
    
    @abstractmethod
    def end_set(self) -> None:
        pass
    
    @abstractmethod
    def obj_pos_set(self, pos: tuple[int, int]) -> None:
        pass
    
    