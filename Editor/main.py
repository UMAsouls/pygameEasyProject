import os
import pygame
from pygame.locals import *
from typing import Any
import json
import sys

from pygame_gui import UIManager

#確実にEditorの部分を実行ディレクトリにするために必要
#例えばcmdでpygameEasyProjectがカレントディレクトリでやるとそこが実行ディレクトリになる
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#いつかモジュール化して消す
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pygameEasy import *

#sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import startup
from Emulator.emulator import Emulator
from GUI import GUI
from Inspector.Inspector import Inspector
from SceneEditor.SceneEditor import SceneEditor
from ObjectBar.ObjectBar import ObjectBar
from Explorer.Explorer import Explorer
from MenuBar.MenuBar import MenuBar

#from pygameEasy.DependencyMaker import Dependency
    
PROJECT_PATH = os.path.abspath(startup.start())

#更新処理
def update(emulator: Emulator, editor: GUI, dt: float) -> None:
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

        editor.process_events(event)
        
    editor.update(dt)
    
def main():
    """main
    """
    with open(PROJECT_PATH + "\project.json") as f:
        project: dict[str, str|int] = json.loads(f.read())
    
    pygame.init()
    pygame.display.set_caption("Editor")
    
    #データ設定
    screen = pygame.display.set_mode([1920,1080])
    sc_rect = screen.get_rect()
    
    #メニューバー
    menu_size = (
        sc_rect.width,
        sc_rect.height*1//20
    )
    menu_topleft = (
        0,
        0
    )
    menu_rect = pygame.Rect(
        menu_topleft,
        menu_size
    )
    
    #エミュレータ設定
    em_size = (
        sc_rect.width*3//5,
        sc_rect.height*3//5 
    )
    emulate_window = pygame.Surface(em_size)
    em_rect = emulate_window.get_rect()
    em_rect.left = sc_rect.width // 5
    em_rect.top = menu_size[1]
    
    #インスペクター設定
    in_size = (
        sc_rect.width*1//5,
        sc_rect.height*3//5
    )
    in_topleft = (
        sc_rect.width*4//5,
        menu_size[1]
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
        menu_size[1]
    )
    bar_rect = pygame.Rect(
        bar_topleft,
        bar_size
    )
    
    #エクスプローラー設定
    exp_size = (
        sc_rect.width,
        sc_rect.height*2//5 - menu_size[1]
    )
    exp_topleft = (
        0,
        sc_rect.height*3//5 + menu_size[1]
    )
    exp_rect = pygame.Rect(
        exp_topleft,
        exp_size
    )
    
    
    
    
    ui_manager = UIManager(sc_rect.size,"theme.json")
    
    #モジュール作成
    emulator = Emulator(PROJECT_PATH, emulate_window, em_rect)
    scene_editor = SceneEditor(PROJECT_PATH)
    inspector = Inspector(ui_manager, in_rect)
    obj_bar = ObjectBar(ui_manager, bar_rect)
    explorer = Explorer(ui_manager,exp_rect)
    menubar = MenuBar(ui_manager, menu_rect)
    editor = GUI(
        project,ui_manager,obj_bar,inspector,scene_editor,emulator,explorer,
        menubar
        )
    clock = pygame.Clock()
    
    
    #初期セットアップ
    editor.start()
    
    #メインループ
    while(True):
        dt = clock.tick(60) /1000.0
        update(emulator, editor, dt)
        
        screen.fill(ui_manager.ui_theme.get_colour('normal_bg'))
        screen.blit(emulate_window, em_rect)
        editor.draw(screen)
        
        pygame.display.update()
    
    


if __name__ == "__main__" :
    main()