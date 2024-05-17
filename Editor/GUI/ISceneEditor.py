from abc import ABC, abstractmethod

from pygameEasy import *

class ISceneEditor(ABC):
    
    @abstractmethod
    def set_obj_by_obj(self, obj:GameObject) -> None:
        pass
    
    @abstractmethod
    def set_obj_by_id(self, id: str) -> None:
        pass
    
    @abstractmethod
    def scene_load(self, path:str) -> None:
        pass
    
    @abstractmethod
    def get_scene(self) -> dict[str, int|str|list|dict]:
        pass 
    
    @abstractmethod
    def get_selecting_obj_id(self) -> str:
        pass
    
    @abstractmethod
    def get_selecting_obj_data(self) -> dict[str, int|str|list|dict]:
        pass
    
    @abstractmethod
    def data_change(self, key: str, idx: int, data: int | str) -> None:
        pass
    
    @abstractmethod
    def save_scene(self) -> None:
        pass