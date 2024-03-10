import os
import pygame
from pygame.locals import *
from typing import Any

import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#いつかモジュール化して消す
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pygameEasy import *

#from pygameEasy.DependencyMaker import Dependency
    
    
PROJECT_PATH = os.getcwd()
    
def set_data(data: dict[str,Any]):
    for d in data["obj"]:
        obj = make_obj_from_data(d)
        add_obj(obj)
        
    for d in data["grp"]:
        grp = make_grp_from_data(d)
        add_grp(grp)
        
def start():
    drawer = Drawer.get_instance()
    drawer.draw()
    
def update():
    key = Key.get_instance()
    music = Music.get_instance()
    drawer = Drawer.get_instance()
    groups = Groups.get_instance()
    
    drawer.update()
    drawer.draw()
    
    groups.update()
    
    music.update()
    key.update()
    
    for event in pygame.event.get():
        if(event.type == QUIT):
            pygame.quit()
            sys.exit()
                
        if(event.type == KEYDOWN):
            if(event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            key.key_down_update(event)
                
        if(event.type == KEYUP):
            key.key_up_update(event)
            
def reload():
    Groups.get_instance().init()
    Drawer.get_instance().init()
    
def main():
    pygame.init()
    init(PROJECT_PATH)
    scene_loader = SceneLoader.get_instance()
    scene_loader.set_path(PROJECT_PATH)
    scene_loader.scene_load("title.json")
    
    music = Music.get_instance()
    music.set_path(PROJECT_PATH)
    
    screen = pygame.display.set_mode([0,0], DOUBLEBUF|HWSURFACE|NOFRAME)
    scene_loader.end_scene
    
    drawer = Drawer.get_instance()
    drawer.init()
    while(True):
        set_data(scene_loader.scene_data)
        start()
        while(True):
            update()
            if scene_loader.end_scene:
                reload()
                break


if __name__ == "__main__" :
    main()