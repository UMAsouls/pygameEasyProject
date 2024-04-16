import json
from collections import deque

from pygameEasy import *
from Editor.GUI import ISceneEditor as I0

class SceneEditor(I0):
    """シーンを編集するバックエンドクラス
    """
    
    def __init__(self, path: str) -> None:
        self._project_path: str = path
        """プロジェクトのパス
        """
        self._scene: dict[str, str|int|list|dict] = {}
        """シーンのjsonデータ
        """
        self._selected_obj: dict[str, str|int|list|dict] = None
        """選択されたオブジェクトのデータ
        """
        self._selected_idx: list[int] = []
        """選択されたオブジェクトのインデックス
        """
    
    
    def scene_load(self, path: str) -> None:
        """シーンロード

        Args:
            path (str): シーンのパス
        """
        with open(self._project_path+"/scene/"+path) as f:
            self._scene = json.load(f)
            
    def get_scene(self) -> dict[str, int | str | list | dict]:
        return self._scene
            
    
    def set_obj_by_obj(self, obj: GameObject) -> None:
        """GameObjectによってオブジェクトセット

        Args:
            obj (GameObject): _description_
        """
        comp = obj.component
        obj_stack = deque()
        while(comp != None):
            obj_stack.append(comp.main)
            comp = comp.parent
            
        obj_list: list[dict[str,int|str|list]] = self._scene["obj"]
        idx: int = 0
        
        while(not obj_stack):
            obj = obj_stack.pop()
            
            for v,i in enumerate(obj_list):
                if (obj.name == i["name"]):
                    self._selected_obj = i
                    self._selected_idx.append(v)
                    obj_list = i["kid"]
                    
                
            
                
        
        
            
    
        