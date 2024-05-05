from pygame import Rect
import pygame

from pygame_gui import UIManager

from pygame_gui.elements import \
    UIPanel,UIScrollingContainer,UITextEntryLine,UILabel
    
from pygame_gui import \
    UI_TEXT_ENTRY_FINISHED
    
from GUI.Iinspector import Iinspector as I0
    
from __const import CHANGE_DATA_EVENT

from .data_change_event import DataChangeEvent
from .change_obj_pos_event import ChangeObjPosEvent


class DataCase:
    def __init__(self, name: str, data: str|int|list|dict, nec_key: list[str], id:str = "") -> None:
        self.name:str = name
        self.type: type = type(data)
        self.data: self.type = data
        self.nec_key: list[str] = nec_key
        self.id = id + self.name
        
        self.long:int = 1
        self.type_list: list[type] = []
        self.elements: dict[str, "DataCase"] = {}
        
        if(self.type == list):
            self.long = len(data)
            self.type_list = [type(i) for i in data]
            
        elif(self.type == dict):
            self.elements = {k: DataCase(k, v, nec_key, self.id+".") for k,v in self.data.items()}
            
        else:
            self.data = [self.data]
            self.type_list = [self.type]

        self.panel: UIPanel = None
        self.title: UILabel = None
        self.text_entry: list[UITextEntryLine] = None
        
    def _make_dict_ui(self, ui_manager: UIManager, rect:Rect, container: UIScrollingContainer | UIPanel) -> None:
        """dict用のUI作成関数

        Args:
            ui_manager (UIManager): マネージャー
            rect (Rect): 構成するrect (の参照)(高さは0)
            container (UIScrollingContainer | UIPanel): コンテナ
        """
        
        title_size = (rect.width//3, 20)
        entry_size = (rect.width//3, 30)
        
        self.panel = UIPanel(rect, manager=ui_manager,container=container)
        title_rect = Rect((5,0), title_size)
        self.title = UILabel(title_rect, self.name, ui_manager, container=self.panel)
        
        e_rect = Rect(5, title_size[1]+5, rect.width, 0)
        for k,v in self.elements.items():
            v.recreate_ui(ui_manager, e_rect, self.panel)
            e_rect = Rect(5, e_rect.top + e_rect.height + 15, e_rect.width, 0)
            
        rect.height = e_rect.top+e_rect.height + 10
        self.panel.set_dimensions(rect.size)
        
    def recreate_ui(self, ui_manager: UIManager, rect:Rect, container: UIScrollingContainer | UIPanel) -> None:
        """UI作成

            位置が設定された高さ0のrectを入力することでUIを作成できる
            
        Args:
            ui_manager (UIManager): マネージャー
            rect (Rect): 構成するrect (の参照)(高さは0)
            container (UIScrollingContainer | UIPanel): コンテナ
        """
        if(self.type == dict):
            self._make_dict_ui(ui_manager, rect, container)
            return
        
        title_size = (rect.width//3, 20)
        entry_size = (rect.width//3, 30)
        
        self.panel = UIPanel(rect, manager=ui_manager,container=container)
        title_rect = Rect((5, 0), title_size)
        self.title = UILabel(title_rect, f"{self.name}", ui_manager, container=self.panel)
        
        self.text_entry = [
            UITextEntryLine(
                Rect(
                    (5 + (entry_size[0]+10)*i, title_size[1]+5),
                    entry_size
                ),
                manager=ui_manager,
                container = self.panel,
                initial_text=str(self.data[i])
            )
            for i in range(self.long)
        ]
        
        rect.height = (title_size[1]+5) + entry_size[1] + 10
        self.panel.set_dimensions(rect.size)
        self.panel.rebuild()
        
    def post_pos_change_event(self) -> None:
        """位置変更時の処理

        Args:
            idx (int): インデックス
            data (int): データ本体
        """
        if self.id != "pos":
            raise Exception("This is not pos data place")
        
        pos = (int(self.data[0]), int(self.data[1]))
        
        event = ChangeObjPosEvent(pos)
        pygame.event.post(event.make_event())
        
        
    def text_entry_event(self, event : pygame.Event):
        """テキスト入力時処理

        Args:
            event (pygame.Event): イベント
        """
        if self.type == dict:
            for v,i in self.elements.items():
                i.process_event(event)
                
        else:
            for v,i in enumerate(self.text_entry):
                if event.ui_element == i:
                    self.data[v] = self.type_list[v](event.text)
                    
                    if self.id == "pos":
                        self.post_pos_change_event()
                    
                    ev = DataChangeEvent(self.id, v, self.type_list[v](event.text))
                    pygame.event.post(ev.make_event())
        
    def process_event(self, event: pygame.Event):
        """イベントの処理

        Args:
            event (pygame.Event): イベント
        """
        if event.type == UI_TEXT_ENTRY_FINISHED:
            self.text_entry_event(event)
            
        
    def text_change(self, idx: int, data: int | str) -> None:
        self.text_entry[idx].set_text(str(data))
            
        
        


class Inspector(I0):
    def __init__(self, ui_manager: UIManager, rect: Rect) -> None:
        self.ui_manager = ui_manager
        self.rect = rect
        self._selecting_obj: dict[str, str|int|list|dict]
        
        self.panel: UIPanel = None
        self.container: UIScrollingContainer = None
        
        self.elements: dict[str, DataCase] = {}
        
        self.nec_key: list[str] = ["pos"]
        
    def process_event(self, event: pygame.Event) -> None:
        for i in self.elements.values():
            i.process_event(event)
        
        
    def recreate_ui(self) -> None:
        """UIを構成する
        """
        self.panel = UIPanel(
            self.rect, manager=self.ui_manager
        )
        
        self.container = UIScrollingContainer(
            Rect((0,0), (self.rect.width, self.rect.height)), self.ui_manager,
            container=self.panel
        )
        
        
        e_rect = Rect(0, 10, self.rect.width, 0)
        for k,v in self.elements.items():
            v.recreate_ui(self.ui_manager, e_rect, self.container)
            e_rect = Rect(5, e_rect.top + e_rect.height + 15, e_rect.width, 0)
            
        self.container.set_scrollable_area_dimensions((self.rect.width, e_rect.top + e_rect.height + 5))
        
    def set_obj_data(self, data: dict[str, str | int | list | dict]) -> None:
        self._selecting_obj = data
        self.elements = {
            k: DataCase(k, v, self.nec_key) for k,v in self._selecting_obj.items()
        }
        
        self.recreate_ui()
        
    def pos_data_change(self, data: tuple[int, int]) -> None:
        """pos部分のデータを設定

        Args:
            data (tuple[int, int]): pos部分データ
        """
        
        self.elements["pos"].text_change(0, data[0])
        self.elements["pos"].text_change(1, data[1])