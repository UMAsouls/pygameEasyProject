from pygame import Rect,Event
import pygame
import os
from enum import Flag, auto

from pygame_gui import UIManager

from pygame_gui.elements import \
    UIPanel,UIScrollingContainer,UITextEntryLine,UILabel,UIButton
    
    
from pygame_gui import \
    UI_TEXT_ENTRY_FINISHED, UI_BUTTON_PRESSED
    
from GUI.IExplorer import IExplorer as I0

from .change_scene_event import ChangeSceneEvent
    
from __const import CHANGE_SCENE_EVENT

class FileType(Flag):
    SCENE = auto()

class FileButton(UIButton):
    def __init__(
        self, relative_rect: Rect | tuple[float, float] | pygame.Vector2, text: str, manager: UIManager,
        container: UIScrollingContainer | UIPanel, path: str, type: FileType
        ):
        super().__init__(relative_rect, text, manager, container)
        
        self._path: str = path
        self._type: FileType = type
        
    @property
    def path(self) -> str:
        return self._path
    
    @property
    def type(self) -> FileType:
        return self._type

class Explorer(I0):
    """エクスプローラー
    
        データなどを選択できる部分
    """
    
    def __init__(self, manager: UIManager, rect: Rect) -> None:
        self._manager = manager
        self._project_path: str = None
        """プロジェクトのパス
        """
        self.rect = rect
        """表示するrect
        """
        
        self._selected_dir: str = "scene"
        """選択されたdir
        """
        
        self._paths: list[str] = []
        """選択されたdirのpath
        """
        
        self._panel: UIPanel = None
        """エクスプローラーのパネル
        """
        
        self._dir_panel: UIScrollingContainer = None
        """ディレクトリ選択パネル
        """
        self._dir_panel_rect: Rect = Rect((0,0),(self.rect.width*1/4, self.rect.height))
        """↑のrect(パネル全体の1/4を使う)
        """
        
        self._file_panel: UIScrollingContainer = None
        """ファイル選択パネル
        """
        self._data_panel_rect: Rect = Rect((self.rect.width*1/4,0),(self.rect.width*3/4, self.rect.height))
        """↑のrect(パネル全体の3/4)
        """
        
        self._file_bu_rect: Rect = Rect((0,0), (120,150))
        """ファイル選択ボタンのRect
        """
        self._file_col: int = 10
        """ファイルの列数
        """
        
        self._file_buttons: list[FileButton] = []
        
    def process_event(self, event: Event) -> None:
        if(event.type == UI_BUTTON_PRESSED):
            for i in self._file_buttons:
                if(event.ui_element == i):
                    if i.type == FileType.SCENE:
                        pygame.event.post(ChangeSceneEvent(i.path).make_event())
        
    
    def load(self, path: str) -> None:
        """プロジェクトロード

        Args:
            path (str): プロジェクトパス
        """
        
        self._project_path = path
        self.check_project()
        
    def check_project(self) -> None:
        """プロジェクトの状態をチェック
        """
        self._paths = os.listdir(self._project_path + "/" + self._selected_dir)
        
        
    def create_file_ui(self) -> None:
        for v,i in enumerate(self._paths):
            col = v % self._file_col
            row = v // self._file_col
            
            bu_rect = self._file_bu_rect.copy()
            bu_rect.top = 10 + (bu_rect.height+10)*row
            bu_rect.left = 10 + (bu_rect.width+10)*col
            
            button = FileButton(
                bu_rect, i, self._manager, self._file_panel,
                i,  FileType.SCENE
            )
            
            self._file_buttons.append(button)
            
        
        
    def recreate_ui(self) -> None:
        """UIの作成・再作成
        """
        self._panel = UIPanel(self.rect, manager=self._manager)
        
        self._dir_panel = UIScrollingContainer(
            self._dir_panel_rect, self._manager, container=self._panel
        )
        
        self._file_panel = UIScrollingContainer(
            self._data_panel_rect, self._manager, container=self._panel
        )
        
        self.create_file_ui()
        
        
        
        
        
        
        
        
        
        
        
        
        
        