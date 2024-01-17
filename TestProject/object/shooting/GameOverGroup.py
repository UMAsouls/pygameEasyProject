import pygame

from pygameEasy import *

from .Base import Base
from .Counter import Counter
from .GameOverText import GameOverText
from .Attack import Attack
from .Defense import Defense

class GameOverGroup(ObjectGroup):
    def set_data(self, data: dict) -> None:
        super().set_data(data)
        
        self.base: Base = self.get_obj_by_id("base")
        self.counter: Counter = self.get_obj_by_id("counter")
        self.text: GameOverText = self.get_obj_by_id("text")
        self.select1: GameOverText = self.get_obj_by_id("select1")
        self.select2: GameOverText = self.get_obj_by_id("select2")
        
        self.attack: Attack = self.get_obj_by_id("attack")
        self.defence: Defense = self.get_obj_by_id("defence")
        self.bat = self.defence.component.get_kid("bat").main
        
        self.music = Music.get_instance()
        self.key = Key.get_instance()
        self.scene_loader = SceneLoader.get_instance()
        
        self.winner = ""
        self.over: bool = False

        self.object_count = 0
        self.object = ""
        
        self.win = self.music.get_sound("win.ogg")
    
    #選択肢を選択するプログラム
    def selecter(self):
        if self.text.visible:
            if self.key.get_key_down("up"):
                if self.object_count == 1:
                    self.select2.color = (255,255,255,0)
                    self.select1.color = (255,0,0,0)
                    self.object = self.select1
                else:
                    self.select1.color = (255,0,0,0)
                    self.object_count = 1
                    self.object = self.select1
        
            if self.key.get_key_down("down"):
                if self.object_count == 1:
                    self.select1.color = (255,255,255,0)
                    self.select2.color = (255,0,0,0)
                    self.object = self.select2
                else:
                    self.select2.color = (255,0,0,0)
                    self.object_count = 1
                    self.object = self.select2

            if self.key.get_key_down("enter"):
                if self.object == self.select1:
                    self.scene_loader.scene_load("2player.json")
                    Counter.visible = True
                elif self.object == self.select2:
                    self.scene_loader.scene_load("title.json")
                    Counter.visible = True
        else:
            pass
    
    def text_set(self):
        self.text.visible = True
        self.select1.visible = True
        self.select2.visible = True
        
        self.text.change_pivot("center")
        self.select1.change_pivot("center")
        self.select2.change_pivot("center")
        
        size = pygame.display.get_surface().get_size()
        
        self.text.position = [size[0]//2, size[1]*4//10]
        self.select1.position = [size[0]//2, size[1]*6//10]
        self.select2.position = [size[0]//2, size[1]*7//10]
        
        self.text.text += self.winner
        
    def machin_stop(self):
        self.attack.stop = True
        self.defence.stop = True
        self.bat.stop = True
        
    def music_set(self):
        self.music.stop_bgm()
        self.music.play_effect(self.win)
        
    def update(self):
        super().update()
        
        if self.over:
            self.selecter()
            return
        
        if self.base.get_hp_ratio() <= 0:
            self.winner = "Attack"
            self.over = True
            self.text_set()
            self.machin_stop()
            self.music_set()
            self.counter.visible = False
            
        elif self.counter.count <= 0:
            self.winner = "Defense"
            self.over = True
            self.text_set()
            self.machin_stop()
            self.music_set()
            self.counter.visible = False
            
        
        