from typing import List
import pygame
import sys
import injector
import os

from .IGameObject import IGameObject
from .IDrawer import IDrawer
from .IGroups import IGroups
from .IKey import IKey
from .IObjectSetter import IObjectSetter
from .ISceneLoader import ISceneLoader
from .IMusic import IMusic

from pygameEasy.Groups import IObjectGroup as I0
from pygameEasy.GameObject import IObjectGroup as I1
from pygameEasy.GManager import IObjectGroup as I2
from pygameEasy.ObjectSetter import IObjectGroup as I3
from .IObjectGroup import IObjectGroup as I4

#GameObjectをまとめて管理できるオブジェクト
#色々なメタ的な動作をさせられる
class ObjectGroup(I0,I1,I2,I3,I4):
    def __init__(
        self,
        groups: IGroups,
        drawer: IDrawer, 
        key: IKey, 
        scene_loader: ISceneLoader,
        object_setter: IObjectSetter,
        music: IMusic
        ) -> None:
        super().__init__()
        
        self._groups = groups
        self._drawer = drawer
        self._key = key
        self._scene_loader = scene_loader
        self._obj_setter = object_setter
        self._music = music
        
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
        
        
    def set_data(self, data: dict) -> None:
        self._name = data["name"]
        
        for k,v in data["objects"].items():
            obj = self._groups.get_single_by_name(v)
            self.id_dict[k] = obj
            self.add(obj)
            
            
    def get_obj_by_id(self, id: str) -> IGameObject:
        return self.id_dict[id]
        
    def update(self):
        pass
