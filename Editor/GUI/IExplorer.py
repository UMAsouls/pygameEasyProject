from abc import ABC, abstractmethod

from pygame import Event

class IExplorer(ABC):
    
    @abstractmethod
    def process_event(self, event: Event) -> None:
        pass
    
    @abstractmethod
    def load(self, path: str) -> None:
        pass
    
    @abstractmethod
    def recreate_ui(self) -> None:
        pass