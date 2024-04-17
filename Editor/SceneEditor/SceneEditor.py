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
        self._selecting_obj: dict[str, str|int|list|dict] = None
        """選択されたオブジェクトのデータ
        """
        self._selecting_idx: list[int] = []
        """選択されたオブジェクトのインデックス
        """
        self._selecting_id: str = ""
        """選択されたオブジェクトのid
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
        self._selecting_id = ""
        
        comp = obj.component
        obj_stack = deque()
        while(comp != None):
            obj_stack.append(comp.main)
            comp = comp.parent
            
        obj_list: list[dict[str,int|str|list]] = self._scene["obj"]
        
        while(len(obj_stack) > 0):
            obj = obj_stack.pop()
            
            for v,i in enumerate(obj_list):
                if (obj.name == i["name"]):
                    self._selecting_obj = i
                    self._selecting_idx.append(v)
                    self._selecting_id += obj.name + "."
                    if(len(obj_stack) > 0):
                        obj_list = i["kid"]
                    
        self._selecting_id = self._selecting_id[:-1]
        
    def set_obj_by_id(self, id: str) -> None:
        """idによってオブジェクトを選ぶ

        Args:
            id (str): オブジェクトid
        """
        
        names = id.split(".")
        obj_list: list[dict[str,int|str|list]] = self._scene["obj"]
        
        for i in names:
            for v,j in enumerate(obj_list):
                if (i == j["name"]):
                    self._selecting_obj = j
                    self._selecting_idx.append(v)
                    if("kid" in j):
                        obj_list = j["kid"]
                        
        self._selecting_id = id
        
        
    def get_selecting_obj_id(self) -> str:
        return self._selecting_id
                    
                
            
                
        
        
            
    
        