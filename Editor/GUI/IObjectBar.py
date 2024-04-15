from abc import ABC, abstractmethod

class IObjectBar(ABC):
    
    @abstractmethod
    def get_obj_selected(self) -> dict[str, str|int|list|dict]:
        pass