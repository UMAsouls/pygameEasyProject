import abc
from typing import List,Dict


class ISceneLoader(metaclass=abc.ABCMeta):
    
    @abc.abstractclassmethod
    def scene_load(self, path: str) -> None:
        raise NotImplementedError()