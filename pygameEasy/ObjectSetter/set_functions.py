import pygame
import os
from typing import Any

from .IGameObject import IGameObject
from .ISingleGroup import ISingleGroup
from .IObjectGroup import IObjectGroup

from .IGroups import IGroups
from .IDrawer import IDrawer
from .IKey import IKey
from .ISceneLoader import ISceneLoader
from .IObjectSetter import IObjectSetter
from .IMusic import IMusic

from GameObject import GameObject
from ObjectGroup import ObjectGroup

for i in os.listdir("object"):
    if i[0] == "_" or i[0] == ".": 
        continue
    exec(f"from object" + " import " + f"{i}")
    

from DependencyMaker import Dependency

#jsonデータからobjectを作る
def make_obj_from_data(data: dict[str, Any], module) -> IGameObject:

        obj_type: type[IGameObject]
    
        if(data["class"] == ""):
            obj_type = GameObject
        else:
            obj_type = eval(f"{data['use']}.{data['class']}.{data['class']}")
            
        single: ISingleGroup = Dependency[ISingleGroup]()
            
        obj = obj_type(
            Dependency[IGroups](),
            Dependency[IDrawer](),
            Dependency[IKey](),
            Dependency[ISceneLoader](),
            Dependency[IObjectSetter](),
            Dependency[IMusic](),
            single
        )
        
        obj.set_data(data)

        #data内で子を指定することにする
        if "kid" in data:
            for i in data["kid"]:
                kid: IGameObject = make_obj_from_data(i)
                kid.component.parent = single
            
        return obj

#GameObjectを追加する処理
def add_obj(data: dict, groups: IGroups, drawer: IDrawer, module):
    obj: IGameObject = make_obj_from_data(data)
    groups.add_component(obj.component)
    drawer.add(obj)
    for i in obj.component.kids:
        drawer.add(i)
        
        
        
def make_grp_from_data(data: dict[str,Any]):
    
    grp_type: type[IObjectGroup]
    
    if(data["class"] == ""):
        grp_type = ObjectGroup
    else:
        print(data["class"])
        grp_type = eval(f"{data['use']}.{data['class']}.{data['class']}")
        
    grp = grp_type(
        Dependency[IGroups](),
        Dependency[IDrawer](),
        Dependency[IKey](),
        Dependency[ISceneLoader](),
        Dependency[IObjectSetter](),
        Dependency[IMusic](),
    )
    
    grp.set_data(data)
    
    return grp

#グループを追加する処理
#後々作る
def add_group(data: dict, groups: IGroups, drawer: IDrawer):
    grp = make_grp_from_data(data)
    groups.add_group(grp)