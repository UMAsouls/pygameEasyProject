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
    
    def __init__(self, project_path: str, window: pygame.Surface, rect: pygame.Rect):
        self.drawer = Drawer.get_instance()
        """Drawer
        """
        self.groups = Groups.get_instance()
        """Groups
        """
        self.scene_loader = SceneLoader.get_instance()
        """SceneLoader
        """
        self.camera: GameObject = None
        """カメラオブジェクト
        """
        self.window: pygame.Surface = window
        """エミュレータの画面
        """
        self.rect: pygame.Rect = rect
        """エミュレータの描写範囲（四角形情報)
        """
        self._camera_move_mode: bool = False
        """カメラが動くモードか否か
        """
        
        init(project_path)
        self.scene_loader.set_path(project_path)
        self.drawer.init(self.window)
        
    def load(self, scene_path: str) -> None:
        """シーン読み込み

        Args:
            scene_path (str):  シーンのパス
        """
        
        self.scene_loader.scene_load(scene_path)
        self.set_data(self.scene_loader.scene_data)
        
        with open("camera_obj.json") as f:
            c_data = json.loads(f.read())

        self.camera = make_obj_from_data(c_data)
        
        self.drawer.set_camera(self.camera)
    
    def set_data(self, data: dict[str, str|int]):
        """シーンのデータ読み込み

        Args:
            data (dict[str, str | int]): シーンのデータ
        """

        for d in data["obj"]:
            obj = make_obj_from_data(d)
            add_obj(obj)
        
        for d in data["grp"]:
            grp = make_grp_from_data(d)
            add_grp(grp)
            
    def camera_move(self, mouse_rel: tuple[int,int]):
        self.camera.position -= Vector(mouse_rel[0], mouse_rel[1])

    def start(self):
        """シーンの開始時処理

            エディタ上では使わない
        """
        
        self.drawer.start()
        self.drawer.draw()
        self.groups.start()
        
    def mouse_check(self, pos:tuple[int, int])-> bool:
        """マウスがウィンドウ内にあるか

        Args:
            pos (pygame.Event): マウスの場所

        Returns:
            bool: あるかどうか
        """
        
        return self.rect.collidepoint(pos[0], pos[1])
        
        
        
    def event_update(self, event:pygame.Event):
        """イベントに対する処理

            今は何も設定してない
            
        Args:
            event (pygame.Event): イベント
        """
        
        if(event.type == MOUSEBUTTONDOWN):
            if self.mouse_check(event.pos):
                if event.button == 2 :
                    self._camera_move_mode = True

                if event.button == 4:
                    self.drawer.zoom += 5

                if event.button == 5:
                    self.drawer.zoom -= 5
                    if(self.drawer.zoom < 10):
                        self.drawer.zoom = 5
                
        if(event.type == MOUSEBUTTONUP):
            if event.button == 2:
                self._camera_move_mode = False
                
        if(event.type == MOUSEMOTION):
            if self._camera_move_mode:
                self.camera_move(event.rel)
                

    def update(self):
        """エミュレータの更新処理
        """
        self.drawer.setup()
        self.drawer.draw() 
        
        #self.camera.position += Vector(1,1)    

    def reload(self):
        """シーンの再読み込み前の初期化処理
        """
        
        self.groups.init()
        self.drawer.init()


if __name__ == "__main__" :
    pass