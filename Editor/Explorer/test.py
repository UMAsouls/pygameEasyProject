from pygame import Rect,Event
import pygame
from pygame.locals import *
import os
import sys
import json

from pygame_gui import UIManager

os.chdir(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Explorer import Explorer

from __const import CHANGE_SCENE_EVENT

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

with open("test_data/config.json") as f:
    config: dict[str, str|int] = json.loads(f.read())
    
PROJECT_PATH: str = config["project_path"]

#更新処理
def update(manager: UIManager, explorer: Explorer, dt: float) -> None:
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
                
        if event.type == CHANGE_SCENE_EVENT:
            print(event.path, "scene")
                
        manager.process_events(event)
        explorer.process_event(event)

        #editor.process_events(event)
        
    #editor.update(dt)
    manager.update(dt)
    
def main():
    """main
    """
    with open(PROJECT_PATH + "\project.json") as f:
        project: dict[str, str|int] = json.loads(f.read())
    
    pygame.init()
    #pygame.display.set_caption("Editor")
    
    #データ設定
    screen = pygame.display.set_mode([1920,1080])
    sc_rect = screen.get_rect()
    
    #エミュレータ設定
    em_size = (
        sc_rect.width*3//5,
        sc_rect.height*3//5
    )
    emulate_window = pygame.Surface(em_size)
    em_rect = emulate_window.get_rect()
    em_rect.left = sc_rect.width // 5
    
    #インスペクター設定
    in_size = (
        sc_rect.width*1//5,
        sc_rect.height*3//5
    )
    in_topleft = (
        sc_rect.width*4//5,
        0
    )
    in_rect = pygame.Rect(
        in_topleft,
        in_size
    )
    
    #オブジェバー設定
    bar_size = (
        sc_rect.width*1//5,
        sc_rect.height*3//5
    )
    bar_topleft = (
        0,
        0
    )
    bar_rect = pygame.Rect(
        bar_topleft,
        bar_size
    )
    
    exp_size = (
        sc_rect.width,
        sc_rect.height*2//5
    )
    exp_topleft = (
        0,
        sc_rect.height*3//5
    )
    exp_rect = pygame.Rect(
        exp_topleft,
        exp_size
    )
    
    
    ui_manager = UIManager(sc_rect.size,"test_data/theme.json")
    
    #モジュール作成
    """
    emulator = Emulator(PROJECT_PATH, emulate_window, em_rect)
    scene_editor = SceneEditor(PROJECT_PATH)
    inspector = Inspector(ui_manager, in_rect)
    obj_bar = ObjectBar(ui_manager, bar_rect)
    editor = GUI(project,ui_manager,obj_bar,inspector,scene_editor,emulator)
    """
    explorer = Explorer(ui_manager,exp_rect)
    clock = pygame.Clock()
    
    
    #初期セットアップ
    #editor.start()
    explorer.load(PROJECT_PATH)
    explorer.recreate_ui()
    
    #メインループ
    while(True):
        dt = clock.tick(60) /1000.0
        update(ui_manager, explorer, dt)
        
        screen.fill(ui_manager.ui_theme.get_colour('normal_bg'))
        screen.blit(emulate_window, em_rect)
        #editor.draw(screen)
        ui_manager.draw_ui(screen)
        
        pygame.display.update()
    
    


if __name__ == "__main__" :
    main()