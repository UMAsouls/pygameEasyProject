import injector
import sys
from typing import Any

from pygameEasy import GameObject
from pygameEasy import Component
from pygameEasy import Groups
from pygameEasy import Drawer
from pygameEasy import ObjectGroup 

PROJECT_PATH = ""

def init(path: str):
    global PROJECT_PATH
    PROJECT_PATH = path
    sys.path.append(path)
    
#jsonデータからobjectを作る
def make_obj_from_data(data: dict[str, Any]) -> GameObject:

    obj_type: type[GameObject]
    
    if(data["class"] == ""):
        obj_type = GameObject
    else:
        exec("from object" + " import " + data["use"])
        obj_type = eval(f"{data['use']}.{data['class']}.{data['class']}")
            
    single = Component()
            
    obj = obj_type(
        single,
        PROJECT_PATH
    )
        
    #data内で子を指定することにする
    if "kid" in data:
        for i in data["kid"]:
            kid: GameObject = make_obj_from_data(i)
            kid.component.parent = single
        
    obj.set_data(data)
            
    return obj

def add_obj(obj: GameObject):
    drawer = Drawer.get_instance()
    groups = Groups.get_instance()
    
    groups.add_component(obj.component)
    drawer.add(obj)
    for i in obj.component.kids:
        drawer.add(i)
    
    
def make_grp_from_data(data: dict[str,Any]):
    groups = Groups.get_instance()
    
    grp_type: type[ObjectGroup]
    
    if(data["class"] == ""):
        grp_type = ObjectGroup
    else:
        exec("from object" + " import " + data["use"])
        grp_type = eval(f"{data['use']}.{data['class']}.{data['class']}")
        
    grp = grp_type()
    
    for k,v in data["objects"].items():
        obj = [groups.get_single_by_name(i) for i in v]
        grp.set_obj(k, obj)
    
    grp.set_data(data)
    
    return grp

def add_grp(grp: ObjectGroup):
    groups = Groups.get_instance()
    groups.add_group(grp)
