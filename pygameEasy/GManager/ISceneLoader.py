import abc

class ISceneLoader(metaclass = abc.ABCMeta):
    @property
    @abc.abstractclassmethod
    def end_scene(self) -> bool:
        raise NotImplementedError()
    
    @property
    @abc.abstractclassmethod
    def scene_data(self) -> dict:
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def scene_load(self, path: str) -> None:
        raise NotImplementedError()