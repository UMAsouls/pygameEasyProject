import os
import pygame
from pygame.locals import *
from typing import Any
import json
import sys

from pygame_gui import UIManager

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#いつかモジュール化して消す
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pygameEasy import *

import startup
from editor import Editor
from emulator import Emulator

#from pygameEasy.DependencyMaker import Dependency
    
PROJECT_PATH = os.path.abspath(startup.start())

#更新処理
def update(emulator: Emulator, editor: Editor, dt: float) -> None:
    """更新処理

        エディタの更新処理をここでまとめて行う
        
        Args:
            emulator (Emulator): エミュレータ
            editor (Editor): エディタ
            dt (float): フレーム間の時間
    """
    
    for event in pygame.event.get():
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()

        if(event.type == KEYDOWN):
            if(event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        emulator.event_update(event)
        editor.event_update(event)
        
    emulator.update()
    editor.update(dt)
    
def main():
    with open(PROJECT_PATH + "\project.json") as f:
        project: dict[str, str|int] = json.loads(f.read())
    
    pygame.init()
    pygame.display.set_caption("Editor")
    
    screen = pygame.display.set_mode([1920,1080])
    sc_rect = screen.get_rect()
    
    em_size = (
        sc_rect.width*3//5,
        sc_rect.height*3//5
    )
    emulate_window = pygame.Surface(em_size)
    em_rect = emulate_window.get_rect()
    em_rect.left = sc_rect.width // 5
    
    emulator = Emulator(PROJECT_PATH, emulate_window, em_rect)
    editor = Editor()
    clock = pygame.Clock()
    
    #emulator.load(project["start_scene"])
    emulator.load("2player.json")
    
    while(True):
        dt = clock.tick(60) /1000.0
        update(emulator, editor, dt)
        
        screen.fill([0,255,0,0])
        screen.blit(emulate_window, em_rect)
        editor.draw(screen)
        
        pygame.display.update()
    
    


if __name__ == "__main__" :
    main()