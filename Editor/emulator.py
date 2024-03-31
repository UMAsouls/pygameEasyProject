import os
import pygame
from pygame.locals import *
from typing import Any
import json
import sys

from pygame_gui import UIManager

#いつかモジュール化して消す
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pygameEasy import *
    

class Emulator:
    """フレームワークのエミュレータ
    """
    
    def __init__(self, project_path: str, window: pygame.Surface):
        self.drawer = Drawer.get_instance()
        self.groups = Groups.get_instance()
        self.scene_loader = SceneLoader.get_instance()
        
        init(project_path)
        self.scene_loader.set_path(project_path)
        self.drawer.init(window)
        
    def load(self, scene_path: str) -> None:
        """シーン読み込み

        Args:
            scene_path (str):  シーンのパス
        """
        
        self.scene_loader.scene_load(scene_path)
        self.set_data(self.scene_loader.scene_data)
    
    def set_data(self, data: dict[str, str|int]):
        """シーンのデータ読み込み

        Args:
            data (dict[str, str | int]): シーンのデータ
        """

        for d in data["obj"]:
            obj = make_obj_from_data(d)
            add_obj(obj)
            if(obj.name == data["start_camera"]):
                self.drawer.set_camera(obj)

        for d in data["grp"]:
            grp = make_grp_from_data(d)
            add_grp(grp)

    def start(self):
        """シーンの開始時処理

            エディタ上では使わない
        """
        
        self.drawer.start()
        self.drawer.draw()
        self.groups.start()


    def update(self):
        """エミュレータの更新処理
        """
        self.drawer.setup()
        self.drawer.draw()     

    def reload(self):
        """シーンの再読み込み前の初期化処理
        """
        
        self.groups.init()
        self.drawer.init()


if __name__ == "__main__" :
    pass