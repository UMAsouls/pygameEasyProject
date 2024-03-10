import abc

class IEventListener(abc.ABC):
    @property
    @abc.abstractmethod
    def status(self) -> bool:
        pass
    
    @status.setter
    @abc.abstractmethod
    def status(self, value:bool) -> None:
        pass
    
    @property
    @abc.abstractmethod
    def type(self) -> str:
        pass