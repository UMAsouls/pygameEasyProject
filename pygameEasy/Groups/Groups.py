import pygame
import injector
import sys

from . import IGameObject
from . import IObjectGroup
from . import IComponent

from pygameEasy.Singleton import Singleton

@injector.singleton
class Groups(Singleton):
    _groups: dict[str, IObjectGroup] = {}
    _singles: dict[str, IComponent] = {}
    _types = {}  
    __groups_same_names: dict[str, int] = {}
    __singles_same_names: dict[str, int] = {}
                        
    def init(self) -> None:
        self._groups = {}
        self._singles = {}
        self._types = {} 
        self.__groups_same_names = {}
        self.__singles_same_names = {}
        
    def get_group_by_name(self, name:str) -> IObjectGroup:
        return self._groups[name]
    
    def add_group(self, group: IObjectGroup) -> None:
        if group.name in self.__groups_same_names:
            self.__groups_same_names[group.name] += 1
            group.name += f"({self.__groups_same_names[group.name]})"
        else:
            self.__groups_same_names[group.name] = 0
        
        self._groups[group.name] = group
            
    def add_component(self, single: IComponent) -> None:
        if single.name in self.__singles_same_names:
            self.__singles_same_names[single.name] += 1
            single.name += f"({self.__singles_same_names[single.name]})"
        else:
            self.__singles_same_names[single.name] = 0
        
        self._singles[single.name] = single
        
        
    def get_single_by_name(self, name:str) -> IGameObject:
        names = name.split(".")
        single: IComponent = self._singles[names[0]]
        
        for i in names[1:]:
            single = single.get_kid(i)
            
        return single.main
    
    def get_component_by_name(self, name: str) -> IComponent:
        names = name.split(".")
        single: IComponent = self._singles[names[0]]
        
        for i in names[1:]:
            single = single.get_kid(i)
            
        return single
    
    def get_group_by_type(self) -> IObjectGroup:
        return
    
    def remove_single(self, name: str) -> None:
        self._singles[name] = None
        
    def remove_obj_from_grp(self, obj: IGameObject) -> None:
        for g in self._groups.values():
            g.remove(obj)
            
    def start(self):
        for i in self._groups.values():
            i.start()
    
    def update(self):
        for i in self._groups.values():
            i.update()
            
        for i in self._groups.values():
            i.event_check()
    