from abc import ABC,abstractmethod
from pygame import Event


class EventData(ABC):
    
    @abstractmethod
    def make_event(self) -> Event:
        pass