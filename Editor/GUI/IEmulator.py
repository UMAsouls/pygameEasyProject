from abc import ABC, abstractmethod

from pygameEasy import *

class IEmulator(ABC):
    def get_obj_selected(self) -> GameObject:
        pass
    
    def select_by_id(self, id: str) -> None:
        pass
    
    def event_update(self, event) -> None:
        pass
    
    def update(self) -> None:
        pass
    
    def end_set(self) -> None:
        pass
    
    