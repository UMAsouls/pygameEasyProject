import sys
from typing import Iterable, Any
import injector
import os

from pygame.sprite import AbstractGroup, LayeredDirty

from . import ObjectGroup
from . import IGameObject

from pygameEasy.Groups import ISingleGroup as I0
from pygameEasy.GManager import ISingleGroup as I1
from pygameEasy.GameObject import ISingleGroup as I2
from .ISingleGroup import ISingleGroup as I3
from pygameEasy.ObjectSetter import ISingleGroup as I4

from pygameEasy.Vector import Vector

#コンポーネント(的なもの)
class SingleGroup(I0,I1,I2,I3,I4, LayeredDirty):
    def __init__(self) -> None:
        LayeredDirty.__init__(self)
        self._main: IGameObject = None
        self._name: str = ""
        
        self._position: Vector = Vector(0,0)
        
        self._root : "SingleGroup" = self
        self._parent : "SingleGroup" = None
        self._kids: dict[str, "SingleGroup"] = {}
        self._kid_names: list[str] = []
        
        self.__same_names: dict[str, int] = {}
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        self._name = value
        
    @property
    def root(self) -> "SingleGroup":
        return self._root
    
    @root.setter
    def root(self, component: "SingleGroup") -> None:
        self._root = component

    #mainのゲッター
    @property
    def main(self) -> IGameObject:
        return self._main
    
    @property
    def position(self) -> Vector:
        return self._position
    
    #コンポーネントのデータ本体を格納
    #同時にオブジェクトにコンポーネントを登録
    @main.setter
    def main(self, obj: IGameObject) -> None:
        if(self._main != None):
            self.remove(self._main)
            
        self.add(obj)
        self._name = obj.name
        self._main = obj
        
        if(self._main.component != self):
            self._main.component = self
            
        self.position_set()
            
    #親の取得
    @property
    def parent(self) -> "SingleGroup":
        return self._parent
    
    #親の設定
    @parent.setter
    def parent(self, component: "SingleGroup") -> None:
        if not component.is_kid(self):
            component.set_kid(self)
        
        self._parent = component
        self.root = component.root
            
    @property
    def kids(self) -> list[IGameObject]:
        return self.sprites()[1:]
    

    #子の存在
    def is_kid(self, component: "SingleGroup") -> bool:
        return (component.name in self._kids)
    
    #子の取得
    def get_kid(self, name: str) -> "SingleGroup":
        return self._kids[name]
    
    #子の設定
    def set_kid(self, component: "SingleGroup") -> None:
        if component.name in self.__same_names:
            self.__same_names[component.name] += 1
            component.name += f"({self.__same_names[component.name]})"
        else:
            self.__same_names[component.name] = 0
        
        self._kids[component.name] = component
        self.add(component.sprites())
        
        component.parent = self
    
    #positionの更新  
    def position_set(self) -> None:    
        self._position = self.main.position
        if(self._parent != None):
            self._position += self._parent.position
            
        for i in self.kids:
            i.component.position_set()
            
    def kill(self):
        
        for i in self._kids.values():
            i.kill()
        
        if(self.parent != None):
            self.parent.remove(self.main)
            
        del self
            
    def remove(self, *sprites: IGameObject | AbstractGroup | Iterable) -> None:
        
        for i in sprites:
        
            for k,v in self._kids.items():
                if v.main == i:
                    self._kids[k] = None
                    continue
                
                if v.has(i):
                    v.remove(i)
                
        
            super().remove(i.component)
        
    
    
from pygameEasy.DependencyConfig import Config

configs = [
    Config(I0, SingleGroup),
    Config(I1, SingleGroup),
    Config(I2, SingleGroup),
    Config(I3, SingleGroup),
    Config(I4, SingleGroup)
]
        