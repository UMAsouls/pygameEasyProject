import os
import pygame
import pygame_gui

from pygame_gui import UIManager, UI_BUTTON_PRESSED

from pygame_gui.elements import UIButton
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UILabel

def start():
    pygame.init()
    
    #ディスプレイ設定
    pygame.display.set_caption("start menu")
    pygame.display.set_mode([800,300])
    
    #manager
    manager = UIManager([800,300],"theme.json")
    
    #screen設定
    screen :pygame.Surface = pygame.display.get_surface()
    dis_rect = screen.get_rect()
    
    #bg設定
    background = pygame.Surface(dis_rect.size)
    background.fill(manager.ui_theme.get_colour("hovered_bg"))
    
    #entry
    entry_rect = pygame.Rect([0,0],[400,30])
    entry_rect.center = dis_rect.center
    entry = UITextEntryLine(entry_rect, manager=manager)
    
    #label
    label_rect = pygame.Rect([0,0],[-1,-1])
    label_rect.left = entry_rect.left + 2
    label_rect.top = entry_rect.top - 25
    label = UILabel(relative_rect=label_rect,
                    text="Please insert a project path",
                    manager=manager)
    
    #button
    bu_rect = pygame.Rect([0,0],[-1,-1])
    bu_rect.topleft = [entry_rect.right+5, entry_rect.top]
    button = UIButton(bu_rect, "input", manager=manager)
    
    #clock
    clock = pygame.Clock()
    
    is_running = True
    
    while is_running:
        dt = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == UI_BUTTON_PRESSED:
                if event.ui_element == button:
                    return entry.get_text()
            manager.process_events(event)
            
        manager.update(dt)
        
        screen.blit(background,(0,0))
        manager.draw_ui(screen)
        
        pygame.display.update()
        
    return ""
        
        
if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(start())
            
                
    
    
    
    
    