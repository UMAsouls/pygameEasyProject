import injector

from . import IDrawer
from . import IGroups
from . import IGameObject

from pygameEasy.GManager import IObjectSetter as I0
from pygameEasy.GameObject import IObjectSetter as I1
from .IObjectSetter import IObjectSetter as I2

from pygameEasy.Singleton import Singleton

class ObjectSetter(I0, I1, I2, Singleton):
    _make_obj_tmp = None
    _add_obj_tmp = None
    _add_group_tmp = None
    _groups: IGroups = None
    _drawer: IDrawer = None
        
    def set_func(self, add_obj, add_group, make_obj) -> None:
        self._make_obj_tmp = make_obj
        self._add_obj_tmp = add_obj
        self._add_group_tmp = add_group
        
    def set_dependency(self, groups: IGroups, drawer: IDrawer):
        self._groups: IGroups = groups
        self._drawer: IDrawer = drawer
        
    def make_obj(self, data: dict) -> IGameObject:
        return self._make_obj_tmp(data)
        
    def add_obj(self, data: dict) -> None:
        self._add_obj_tmp(data, self._groups, self._drawer)
    
    def add_group(self, data: dict) -> None:
        self._add_group_tmp(data, self._groups, self._drawer)
        
    def set_data(self, data: dict) -> None:
        for d in data["obj"]:
            self.add_obj(d)
        
        for d in data["grp"]:
            self.add_group(d)


from pygameEasy.DependencyConfig import Config

configs = [
    Config(I0, lambda: ObjectSetter.get_instance()),
    Config(I1, lambda: ObjectSetter.get_instance()),
    Config(I2, lambda: ObjectSetter.get_instance())
]