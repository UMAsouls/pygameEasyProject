from Editor.GUI import IObjectBar as I0

from pygame import Rect

from pygame_gui import UIManager

from pygame_gui.elements import UIPanel,UIScrollingContainer,UIButton

class ObjButtonData:
    def __init__(self, data: dict[str, str|int|list|dict], rect: Rect):
        self.data = data
        self.rect = rect
        self.open = False
        self.selected = False
        self.kids = []
        
        if("kids" in data):
            self.kids = [
                ObjButtonData(i, Rect(rect.left+20, rect.top, rect.width, rect.height))
                for i in data["kids"]
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
        
        self.objs_data = []
        
        self.obj_button_size = [
            self.rect.width - 20,
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
            self.objs_data.append(i)
            self.obj_buttons.append(UIButton(i.rect, i.data["name"], self.ui_manager, container=self.obj_container))
            
            if(i.open): self.obj_set_by_list(i.kids)
            
        self.scrollable_size = (
            self.obj_button_size[0] + 60,
            self.obj_button_size[1] * len(self.obj_buttons)
        )
            

        
    def recreate_ui(self) -> None:
        self.obj_data = []
        self.obj_buttons = []
        self.scrollable_size = (0,0)
        
        self.ui_manager.clear_and_reset()
        
        self.panel = UIPanel(self.rect, manager=self.ui_manager)
        
        self.obj_container = UIScrollingContainer(
            Rect(10,10, self.rect.width-10, self.rect.height//2 - 10),
            self.ui_manager,
            starting_height = 2,
            container=self.panel
        )
        
        self.obj_set_by_list(self.objs)
        
        self.obj_container.set_scrollable_area_dimensions(self.scrollable_size)
        
        
           
    def get_obj_selected(self) -> dict[str, str | int | list | dict]:
        return None
