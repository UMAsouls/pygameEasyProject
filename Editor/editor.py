import pygame

from pygame_gui import UIManager

class Editor:
    def __init__(self) -> None:
        dis_size = pygame.display.get_surface().get_size()
        self.ui_manager = UIManager(dis_size,"theme.json")
        
    def event_update(self, event: pygame.event.Event):
        self.ui_manager.process_events(event)
        
    def update(self, dt: float):
        self.ui_manager.update(dt)
        
    def draw(self, window: pygame.Surface):
        self.ui_manager.draw_ui(window)