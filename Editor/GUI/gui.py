import pygame

from pygame_gui import UIManager
from pygame_gui.elements import UIWindow

from .IObjectBar import IObjectBar
from .Iinspector import Iinspector
from .ISceneEditor import ISceneEditor
from .IEmulator import IEmulator

from __const import *


class GUI:
    """エディタのGUIを総括するクラス
    """
    def __init__(
        self,
        project: dict[str, int|str|list|dict],
        ui_manager: UIManager, 
        obj_bar: IObjectBar, 
        inspector: Iinspector, 
        scene_editor: ISceneEditor, 
        emulator: IEmulator
        ) -> None:
        
        self.project = project
        
        self.ui_manager = ui_manager
        
        self.scene_editor = scene_editor
        self.inspector = inspector
        self.obj_bar = obj_bar
        self.emulator = emulator
        
    def start(self):
        """スタート時処理
        """
        self.emulator.load(self.project["start_scene"])
        self.scene_editor.scene_load(self.project["start_scene"])
        
        self.obj_bar.obj_load(self.scene_editor.get_scene()["obj"])
        self.obj_bar.recreate_ui()
        
        self.inspector.recreate_ui()
        
    def process_events(self, event: pygame.event.Event):
        """イベントの処理

        Args:
            event (pygame.event.Event): イベント
        """
        self.emulator.event_update(event)
        
        self.ui_manager.process_events(event)
        
        self.obj_bar.process_event(event)
        
        self.inspector.process_event(event)
        
        if event.type == CHANGE_DATA_EVENT:
            key = event.key
            idx = event.idx
            data = event.data
            self.scene_editor.data_change(key, idx, data)
            
        if event.type == CHANGE_OBJ_POS_EVENT:
            pos = event.pos
            print(pos)
        
    def update(self, dt: float): 
        self.emulator.update()       
        self.ui_manager.update(dt)
        
        #エミュレータオブジェ選択時処理
        obj = self.emulator.get_obj_selected()
        if(obj != None):
            self.scene_editor.set_obj_by_obj(obj)
            self.obj_bar.select_by_id(self.scene_editor.get_selecting_obj_id())
            self.inspector.set_obj_data(self.scene_editor.get_selecting_obj_data())
            
        
        #オブジェバーオブジェ選択時処理
        id = self.obj_bar.get_obj_selected()
        if(id != None):
            self.scene_editor.set_obj_by_id(id)
            self.emulator.select_by_id(id)
            self.inspector.set_obj_data(self.scene_editor.get_selecting_obj_data())
            
        self.emulator.end_set()
        self.obj_bar.end_set()
        
    def draw(self, window: pygame.Surface):
        self.ui_manager.draw_ui(window)