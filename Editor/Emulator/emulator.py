import os
import pygame
from pygame.locals import *
from typing import Any
import json
import sys

from pygame_gui import UIManager

from pygameEasy import GameObject

#いつかモジュール化して消す
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pygameEasy import *
from Editor.GUI import IEmulator as I0

class Emulator(I0):
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
        self._selecting_obj: GameObject = None
        """選択中のオブジェクト
        """
        self._changed: bool = False
        """オブジェが変更されたか
        """
        
        self.__mouse_pushing: bool = False
        """マウスを長押ししてるか
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
        """マウスの動きでカメラを動かす

        Args:
            mouse_rel (tuple[int,int]): マウスの移動距離
        """
        self.camera.position -= Vector(mouse_rel[0], mouse_rel[1])
        
    def draw_glit(self):
        """グリット線を書く
        """
        
        x_line_pos = (self.rect.height//2 - self.camera.position.y * (self.drawer.zoom/100)) 
        y_line_pos = (self.rect.width//2 - self.camera.position.x * (self.drawer.zoom/100)) 
        
        #横線
        pygame.draw.line(
            self.window,
            (100,100,100,0),
            (0, x_line_pos),
            (self.rect.width, x_line_pos),
            5
        )
        
        #縦線
        pygame.draw.line(
            self.window,
            (100,100,100,0),
            (y_line_pos, 0),
            (y_line_pos, self.rect.height),
            5
        )
        
    def draw_obj_frame(self) -> None:
        """選択オブジェクトの枠を描く
        """
        if(self._selecting_obj == None):
            return
        
        rect = self._selecting_obj.rect.copy()
        rect.left = self.rect.width//2 + (rect.left - self.camera.position.x) * (self.drawer.zoom/100)
        rect.top = self.rect.height//2 + (rect.top - self.camera.position.y) * (self.drawer.zoom/100)
        rect.width *= (self.drawer.zoom/100)
        rect.height *= (self.drawer.zoom/100)
        
        pygame.draw.rect(self.window,[255,0,0],rect, width=3)
        

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
    
    def get_real_pos(self, pos: tuple[int,int]) -> Vector:
        """マウスの画面上に位置をゲーム内の位置に変換

        Args:
            pos (tuple[int,int]): マウスの位置

        Returns:
            list[GameObject]: オブジェクト一覧
        """
        
        real_pos = Vector(pos[0] - self.rect.left, pos[1] - self.rect.top)
        real_pos.x -= self.rect.width//2
        real_pos.y -= self.rect.height//2
        real_pos /= (self.drawer.zoom/100)
        real_pos += self.camera.position
        
        return real_pos
    
    def change_obj(self, obj: GameObject) -> None:
        """選択中オブジェクトを変える

        Args:
            obj (GameObject): 変更先オブジェクト
        """
        
        self._selecting_obj = obj
        
    def select_by_id(self, id:str) -> None:
        obj = self.groups.get_single_by_name(id)
        
        self.change_obj(obj)
        
    def get_obj_selected(self) -> GameObject:
        """オブジェクトが選択された時にそれを返す

        Returns:
            GameObject: 選択されたオブジェクト
        """
        if(self._changed):
            return self._selecting_obj
        else:
            return None
        
        
    def event_update(self, event:pygame.Event):
        """イベントに対する処理
            
        Args:
            event (pygame.Event): イベント
        """
        
        if(event.type == MOUSEBUTTONDOWN):
            if self.mouse_check(event.pos):
                if event.button == 1 and not self.__mouse_pushing:
                    real_pos = self.get_real_pos(event.pos)
                    objs = self.drawer.get_sprites_at(real_pos.change2list())
                    if(len(objs) >= 1):
                        self.change_obj(objs[-1])
                        self._changed = True
                
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
        self.draw_glit()
        self.draw_obj_frame()
        
        #self.camera.position += Vector(1,1) 
        
    def end_set(self):
        self._changed = False   

    def reload(self):
        """シーンの再読み込み前の初期化処理
        """
        
        self.groups.init()
        self.drawer.init()


if __name__ == "__main__" :
    pass