from Editor.GUI import Iinspector as I0

from pygame import Rect
import pygame

from pygame_gui import UIManager

from pygame_gui.elements import \
    UIPanel,UIScrollingContainer,UITextEntryLine,UILabel


class DataType:
    def __init__(self, name: str, data: str|int|list|dict) -> None:
        self.name:str = name
        self.type: type = type(data)
        self.data = data
        
        self.long:int = 1
        self.elements: dict[str, "DataType"] = {}
        
        if(self.type == list):
            self.long = len(data)
            
        elif(self.type == dict):
            self.elements = {k: DataType(k, v) for k,v in self.data.items()}
            
        else:
            self.data = [self.data]

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


class Inspector(I0):
    def __init__(self, ui_manager: UIManager, rect: Rect) -> None:
        self.ui_manager = ui_manager
        self.rect = rect
        self._selecting_obj: dict[str, str|int|list|dict]
        
        self.panel: UIPanel = None
        self.container: UIScrollingContainer = None
        
        self.elements: dict[str, DataType] = {}
        
        
        
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
            k: DataType(k, v) for k,v in self._selecting_obj.items()
        }
        
        self.recreate_ui()