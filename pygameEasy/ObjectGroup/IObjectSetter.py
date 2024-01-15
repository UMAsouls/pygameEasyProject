import abc

from .IGameObject import IGameObject

class IObjectSetter(metaclass = abc.ABCMeta):
    
    @abc.abstractclassmethod
    def add_obj(data) -> None:
        pass
    
    @abc.abstractclassmethod
    def make_obj(data) -> IGameObject:
        pass