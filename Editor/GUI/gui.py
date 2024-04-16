import pygame

from pygame_gui import UIManager
from pygame_gui.elements import UIWindow

from . import IObjectBar,ISceneEditor,IEmulator,Iinspector

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
        self.scene_editor.scene_load(self.project["start_scene"])
        
        self.obj_bar.obj_load(self.scene_editor.get_scene()["obj"])
        self.obj_bar.recreate_ui()
        
    def event_update(self, event: pygame.event.Event):
        """イベントアップデート

        Args:
            event (pygame.event.Event): イベント
        """
        self.ui_manager.process_events(event)
        
    def update(self, dt: float):        
        self.ui_manager.update(dt)
        
        #エミュレータオブジェ選択時処理
        obj = self.emulator.get_obj_selected()
        if(obj != None):
            self.scene_editor.set_obj_by_obj(obj)
        
        #オブジェバーオブジェ選択時処理
        obj_data = self.obj_bar.get_obj_selected()
        if(obj_data != None):
            pass
        
    def draw(self, window: pygame.Surface):
        self.ui_manager.draw_ui(window)