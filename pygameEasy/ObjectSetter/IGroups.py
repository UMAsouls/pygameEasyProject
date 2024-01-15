import abc

from .IObjectGroup import IObjectGroup
from .ISingleGroup import ISingleGroup

class IGroups(metaclass = abc.ABCMeta):
    
    @abc.abstractclassmethod
    def add_group(self, grp: IObjectGroup) -> None:
        pass
    
    @abc.abstractclassmethod
    def add_component(self, single: ISingleGroup) -> None:
        pass
    
    @abc.abstractclassmethod
    def get_component_by_name(self, name: str) -> None:
        pass