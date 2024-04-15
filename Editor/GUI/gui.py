import pygame

from pygame_gui import UIManager
from pygame_gui.elements import UIWindow

from . import IObjectBar,ISceneEditor,IEmulator

class GUI:
    """エディタのGUIを総括するクラス
    """
    def __init__(self, obj_bar: IObjectBar, inspector, scene_editor: ISceneEditor, emulator: IEmulator) -> None:
        dis_size = pygame.display.get_surface().get_size()
        self.ui_manager = UIManager(dis_size,"theme.json")
        
        self.scene_editor = scene_editor
        self.obj_bar = obj_bar
        self.emulator = emulator
        
    def event_update(self, event: pygame.event.Event):
        self.ui_manager.process_events(event)
        
    def update(self, dt: float):        
        self.ui_manager.update(dt)
        
        #エミュレータオブジェ選択時処理
        obj = self.emulator.get_obj_selected()
        if(obj != None):
            pass
        
        #オブジェバーオブジェ選択時処理
        obj_data = self.obj_bar.get_obj_selected()
        if(obj_data != None):
            pass
        
    def draw(self, window: pygame.Surface):
        self.ui_manager.draw_ui(window)