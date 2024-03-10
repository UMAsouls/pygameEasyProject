import injector

from dataclasses import dataclass

from pygameEasy.DependencyConfig import Config

#DIコンテナ     
class DependencyMaker:
    __config_list: list[Config] = []
    
    def __init__(self):
        self._injector = injector.Injector(self.__class__.configure)
    
    #injectorの初期化処理
    @classmethod
    def configure(cls, binder: injector.Binder):
        for i in cls.__config_list:
            binder.bind(i.interface,to=i.cls,scope=i.scope)
            
    @classmethod
    def set(cls, configs: list[Config]) -> None:
        
        cls.__config_list += configs
        
    def __getitem__(self, klass):
        return lambda: self._injector.get(klass)
    
from pygameEasy.Groups.Groups import configs as c1
DependencyMaker.set(c1)
from pygameEasy.Drawer.Drawer import configs as c2
DependencyMaker.set(c2)
from pygameEasy.SceneLoader.SceneLoader import configs as c3
DependencyMaker.set(c3)
from pygameEasy.ObjectSetter.ObjectSetter import configs as c4
DependencyMaker.set(c4)
from pygameEasy.Key.Key import configs as c5
DependencyMaker.set(c5)
from pygameEasy.component.Component import configs as c6
DependencyMaker.set(c6)
from pygameEasy.Music.Music import configs as c7
DependencyMaker.set(c7)

Dependency = DependencyMaker()