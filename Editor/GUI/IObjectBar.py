from abc import ABC, abstractmethod

class IObjectBar(ABC):
    
    @abstractmethod
    def get_obj_selected(self) -> dict[str, str|int|list|dict]:
        pass
    
    @abstractmethod
    def recreate_ui(self) -> None:
        """uiを構成する
        """
        
    @abstractmethod
    def obj_load(self, obj_list) -> None:
        pass