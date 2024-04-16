from Editor.GUI import Iinspector as I0

from pygame import Rect

from pygame_gui import UIManager

from pygame_gui.elements import UIPanel


class Inspector(I0):
    def __init__(self, ui_manager: UIManager, rect: Rect) -> None:
        self.ui_manager = ui_manager
        
        self.panel = UIPanel