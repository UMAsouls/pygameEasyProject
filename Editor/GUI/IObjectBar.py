from abc import ABC, abstractmethod

from pygame import Event

class IObjectBar(ABC):
    
    @abstractmethod
    def get_obj_selected(self) -> str:
        pass
    
    @abstractmethod
    def recreate_ui(self) -> None:
        """uiを構成する
        """
        
    @abstractmethod
    def obj_load(self, obj_list: list[dict]) -> None:
        pass
    
    @abstractmethod
    def process_event(self, event: Event) -> None:
        pass
    
    @abstractmethod
    def select_by_id(self, id: str) -> None:
        pass
    
    @abstractmethod
    def end_set(self) -> None:
        pass