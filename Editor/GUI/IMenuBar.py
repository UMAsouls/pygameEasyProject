from abc import ABC,abstractmethod
from pygame import Rect,Event

class IMenuBar(ABC):
    def process_event(self, event:Event) -> None:
        pass
    
    def recreate_ui(self) -> None:
        pass