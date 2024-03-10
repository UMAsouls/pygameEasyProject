from abc import ABC, abstractmethod

class IEventBinder(ABC):
    
    @property
    @abstractmethod
    def type(self) -> str:
        pass
    
    @abstractmethod
    def bind(self) -> None:
        pass