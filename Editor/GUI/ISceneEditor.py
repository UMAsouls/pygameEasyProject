from abc import ABC, abstractmethod

from pygameEasy import *

class ISceneEditor(ABC):
    
    @abstractmethod
    def set_obj_by_obj(self, obj:GameObject) -> None:
        pass
    
    @abstractmethod
    def scene_load(self, path:str) -> None:
        pass
    
    @abstractmethod
    def get_scene(self) -> dict[str, int|str|list|dict]:
        pass 