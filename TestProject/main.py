import os
import pygame
from pygame.locals import *
from typing import Any

import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#いつかモジュール化して消す
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pygameEasy.GManager import GManager

from pygameEasy.GManager import IGameObject
from pygameEasy.GManager import IDrawer
from pygameEasy.GManager import IGroups
from pygameEasy.GManager import IKey
from pygameEasy.GManager import ISceneLoader
from pygameEasy.GManager import IObjectGroup
from pygameEasy.GManager import ISingleGroup
from pygameEasy.GManager import IObjectSetter
from pygameEasy.GManager import IMusic

from pygameEasy.GameObject import GameObject
from pygameEasy.ObjectGroup import ObjectGroup

from pygameEasy.DependencyMaker import Dependency

for i in os.listdir("object"):
    if i[0] == "_" or i[0] == ".": 
        continue
    exec(f"from object" + " import " + f"{i}")
    
    
PROJECT_PATH = os.getcwd()

#jsonデータからobjectを作る
def make_obj_from_data(data: dict[str, Any]) -> IGameObject:

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
            single,
            PROJECT_PATH
        )
        
        #data内で子を指定することにする
        if "kid" in data:
            for i in data["kid"]:
                kid: IGameObject = make_obj_from_data(i)
                kid.component.parent = single
        
        obj.set_data(data)
            
        return obj

#GameObjectを追加する処理
def add_obj(data: dict, groups: IGroups, drawer: IDrawer):
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

def main():
    obj_setter: IObjectSetter = Dependency[IObjectSetter]()
    obj_setter.set_func(add_obj, add_group, make_obj_from_data)
    obj_setter.set_dependency(Dependency[IGroups]() ,Dependency[IDrawer]())
    
    scene_loader: ISceneLoader = Dependency[ISceneLoader]()
    scene_loader.set_path(PROJECT_PATH)
    
    music: IMusic = Dependency[IMusic]()
    music.set_path(PROJECT_PATH)
    
    gm = GManager(
        groups=Dependency[IGroups](),
        key=Dependency[IKey](),
        drawer=Dependency[IDrawer](),
        scene_loader=Dependency[ISceneLoader](),
        object_setter=Dependency[IObjectSetter](),
        music = music
        )
    #gm.set_func(set_data)
    gm.scene_loader.scene_load("title.json")
    gm.MainLoop()


if __name__ == "__main__" :
    main()