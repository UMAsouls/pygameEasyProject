from abc import ABC, abstractmethod

class Iinspector(ABC):
    
    @abstractmethod
    def recreate_ui(self) -> None:
        pass
    
    @abstractmethod
    def set_obj_data(self, data: dict[str, str|int|list|dict]) -> None:
        pass