import json
import os
import injector

from pygameEasy.Singleton import Singleton

#levelの分だけ上の階層のディレクトリの絶対パスを返す
def get_parent_path(level):
    path = __file__
    for i in range(level+1):
       path = os.path.abspath(os.path.join(path, os.pardir)) 
    return path

PROJECT_PATH = os.path.dirname(os.getcwd())

class SceneLoader(Singleton):
    _is_first: bool = True
    _scene_data: list[str] = []
    _end_scene: bool = False
    _path: str = ""
    
    def set_path(self, path: str) -> None:
        self._path = path
        
    def scene_load(self, path: str) -> None:
        """シーンの読み込み
        
        これを行うとend_sceneがTrueとなり読み込みが行われる

        Args:
            path (str): シーンのパス
        """
        path = self._path + "/scene/" + path
        with open(path) as f:
            data = json.load(f)
            
        self._scene_data = data
        
        if(self._is_first): 
            self._is_first = False
        else:
            self._end_scene = True
        
    
    @property
    def scene_data(self):
        data = self._scene_data
        self._scene_data = []
        return data
    
    @property
    def end_scene(self) -> bool:
        tmp = self._end_scene
        self._end_scene = False
        return tmp
    

from pygameEasy.DependencyConfig import Config

configs = [
]