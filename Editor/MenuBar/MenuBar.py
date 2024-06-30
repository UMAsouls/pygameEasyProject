import pygame
from pygame import Event
from pygame import Rect
from pygame.locals import MOUSEBUTTONDOWN
import os
import sys

from pygame_gui import UIManager, \
    UI_BUTTON_PRESSED
from pygame_gui.elements import \
    UIDropDownMenu, UIPanel, UIButton
    
from Editor.GUI.IMenuBar import IMenuBar

from __const import SCENE_SAVE_EVENT,recreate_event_post,run_event_post,stop_event_post
    
class MenuBar(IMenuBar):
    """メニューバー
    """
    def __init__(self, manager: UIManager, rect:Rect) -> None:
        self._manager = manager
        self._rect = rect
        
        self._panel: UIPanel = None
        """パネル
        """
        
        self._bu_panel: UIPanel = None
        """ボタンが押された際に出てくるパネル
        """
        
        self._bu_rect = Rect(
            (0, self._rect.height*1/10),
            (self._rect.width*1/20, self._rect.height*4/5,)
        )
        
        self._file_button: UIButton = None
        self._file_bu_rect = self._bu_rect.copy()
        self._file_bu_rect.left = 5
        
        self._file_panel: UIPanel = None
        
        self._file_selection: dict[str, int] = {
            "save": SCENE_SAVE_EVENT
        }
        
        self._file_panel_rect: Rect = self._bu_rect.copy()
        self._file_panel_rect.top = self._file_bu_rect.bottom + self._rect.top
        self._file_panel_rect.left = self._file_bu_rect.left
        self._file_panel_rect.height = self._bu_rect.height*len(self._file_selection)
        
        self._file_panel_visible: int = 0
        
        self.run_button: UIButton = None
        self.run_button_rect = self._bu_rect.copy()
        self.run_button_rect.left = self._file_bu_rect.right + 5
        
        #self._rect_panel: UIPanel = None
        
        
        
    def recreate_ui(self) -> None:
        self._panal = UIPanel(self._rect, 0, manager=self._manager)
        
        self._file_button = UIButton(
            self._file_bu_rect, "file", self._manager, self._panal
        )
        
        if(self._file_panel_visible):
            self._file_panel = UIPanel(
                self._file_panel_rect, 5, manager=self._manager
            )
        
            i = 0
            for k,v in self._file_selection.items():
                rect = self._bu_rect.copy()
                rect.top = rect.height*i
                UIButton(
                    rect, k, self._manager, self._file_panel
                )
                
        self.run_button = UIButton(
            self.run_button_rect, "Run", self._manager, self._panal
        )
        
        
        
        
    def process_event(self, event: Event) -> None:
        if(event.type == MOUSEBUTTONDOWN):
            pos = event.pos
            
            if (
                not self._file_panel_rect.collidepoint([pos[0], pos[1]]) 
                and self._file_panel_visible
            ):
                self._file_panel_visible = 0
                recreate_event_post()
        
        if(event.type == UI_BUTTON_PRESSED):
            
            if(self._file_panel_visible):
                if(event.ui_element.text in self._file_selection):
                    pygame.event.post(Event(self._file_selection[event.ui_element.text]))
            
            if(event.ui_element == self._file_button) :
                self._file_panel_visible = 1
                recreate_event_post()
                
            if(event.ui_element == self.run_button):
                run_event_post()
                
        
        
        
        