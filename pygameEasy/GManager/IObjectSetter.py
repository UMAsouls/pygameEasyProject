import abc

from . import IGroups,IDrawer

class IObjectSetter(metaclass = abc.ABCMeta):
    
    @abc.abstractclassmethod
    def set_func(self, add_obj, add_group) -> None:
        pass
    
    @abc.abstractclassmethod
    def set_data(data: dict):
        pass
    
    @abc.abstractclassmethod
    def set_dependency(self, groups: IGroups, drawer: IDrawer) -> None:
        pass