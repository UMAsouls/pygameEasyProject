from typing import List
import pygame
import sys
import injector
import os

from .IGameObject import IGameObject

from pygameEasy.Groups import IObjectGroup as I0
from pygameEasy.GameObject import IObjectGroup as I1

#GameObjectをまとめて管理できるオブジェクト
#色々なメタ的な動作をさせられる
class ObjectGroup(I0,I1):
    def __init__(
        self
        ) -> None:
        super().__init__()
        
        self._name: str = ""
        
        self.id_dict : dict[str, int] = {}
        self.name_dict: dict[str, int] = {}
        self.type_dict: dict[str, list[int]] = {}
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, n:str) -> None:
        self._name = n
        
    def get_objects(self, name: str) -> GeneratorExit:
        for i in self.sprites():
            if(i.name == name):
                yield i
                
    def sprites(self) -> list[IGameObject]:
        return super().sprites()
    
    def set_obj(self, id:str, obj:IGameObject):
        self.id_dict[id] = obj
        self.add(obj)
        
        
    def set_data(self, data: dict) -> None:
        self._name = data["name"]
            
            
    def get_obj_by_id(self, id: str) -> IGameObject:
        return self.id_dict[id]
        
    def update(self):
        pass
