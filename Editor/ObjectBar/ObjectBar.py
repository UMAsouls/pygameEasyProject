from Editor.GUI.IObjectBar import IObjectBar as I0

from pygame import Rect,Event

import pygame_gui
from pygame_gui import UIManager
from pygame_gui.elements import UIPanel,UIScrollingContainer,UIButton

class ObjButtonData:
    def __init__(self, data: dict[str, str|int|list|dict], rect: Rect, id = ""):
        self.data = data
        self.rect = rect
        self.open = False
        self.selected = False
        self.kids = []
        
        self.id = id + data["name"]
        
        if("kid" in data):
            self.kids = [
                ObjButtonData(i, Rect(rect.left+20, rect.top, rect.width, rect.height), data["name"]+".")
                for i in data["kid"]
            ]
        
    def top_set(self, top: int) -> None:
        self.rect.top = top

class ObjectBar(I0):
    """オブジェクトバー
    """
    
    def __init__(self, ui_manager: UIManager, rect: Rect) -> None:
        self.ui_manager = ui_manager
        self.rect = rect
        self.objs = []
        self.grps = []
        
        self.selecting_obj: ObjButtonData = None
        self.change = False
        
        self.obj_data = []
        
        self.obj_button_size = [
            self.rect.width-5,
            30
        ]
        
        self.scrollable_size = (0,0)
        
        self.panel: UIPanel = None
        """バーのパネル
        """
        self.obj_container: UIScrollingContainer = None
        """オブジェ部分
        """
        self.obj_buttons: list[UIButton] = []
        
    def obj_load(self, obj_list: list[dict[str, str|int|list|dict]]) -> None:
        """シーンのオブジェからバー生成のためのインスタンス生成

        Args:
            obj_list (list[dict[str, str | int | list | dict]]): オブジェデータ
        """
        rect =  Rect((0,0), self.obj_button_size)
        
        self.objs = [
                ObjButtonData(i, rect.copy())
                for i in obj_list
            ]
        
    def obj_set_by_list(self, objlist: list[ObjButtonData]) -> None:
        
        for i in objlist:
            i.top_set(self.obj_button_size[1]*len(self.obj_buttons))
            self.obj_data.append(i)
            
            if(i.selected):
                button = UIButton(i.rect, i.data["name"], self.ui_manager, container=self.obj_container, object_id="##selected_button")
            else:
                button = UIButton(i.rect, i.data["name"], self.ui_manager, container=self.obj_container)
                
            self.obj_buttons.append(button)
            
            if(i.open): self.obj_set_by_list(i.kids)
            
        self.scrollable_size = (
            self.obj_button_size[0] + 60,
            self.obj_button_size[1] * len(self.obj_buttons)
        )
    
    def obj_select(self, obj: ObjButtonData) -> None:
        if(self.selecting_obj != None):
            self.selecting_obj.selected = False
        self.selecting_obj = obj
        self.selecting_obj.selected = True
        self.recreate_ui()
        
    def select_by_id(self, id: str) -> None:
        id = id.split(".")
        r = self.objs
        obj = None
        for i in id:
            for j in r:
                if i == j.data["name"]:
                    obj = j
                    r = obj.kids
                    
        self.obj_select(obj)

        
    def recreate_ui(self) -> None:
        self.obj_data = []
        self.obj_buttons = []
        self.scrollable_size = (0,0)
        
        self.ui_manager.clear_and_reset()
        
        self.panel = UIPanel(self.rect, manager=self.ui_manager)
        
        self.obj_container = UIScrollingContainer(
            Rect(0,10, self.rect.width, self.rect.height//2-10),
            self.ui_manager,
            starting_height = 2,
            container=self.panel
        )
        
        self.obj_set_by_list(self.objs)
        
        self.obj_container.set_scrollable_area_dimensions(self.scrollable_size)
        
    def process_event(self, event: Event):
        for v,i in enumerate(self.obj_buttons):
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == i:
                    self.change = True
                    self.obj_select(self.obj_data[v])
                    
    def end_set(self) -> None:
        self.change = False
                    
           
    def get_obj_selected(self) -> str:
        if self.change:
            return self.selecting_obj.id
        else:
            return None
