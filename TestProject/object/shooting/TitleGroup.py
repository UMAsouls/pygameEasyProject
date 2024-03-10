import pygame
import sys

from pygameEasy import *

class TitleGroup(ObjectGroup):
    def start(self) -> None:

        self.object_count = 0
        self.selecter = -1
        
        self.key = Key.get_instance()
        self.scene_loader = SceneLoader.get_instance()
        
        self.select_event = self.Event(self.Event.LisType.NULL, self.Event.BinType.SELECT)
        self.select_event.set_binder(self, "select", "text")
        
        self.change_event = self.Event(self.Event.LisType.NULL, self.Event.BinType.SELECT)
        self.change_event.set_binder(self, "change", "text")
        
        self.set_event(self.select_event)
        self.set_event(self.change_event)
        
    def update(self):
        super().update()
        
        self.change_event.selecter_stop()
        self.select_event.selecter_stop()

        if self.key.get_key_down("up"):
            self.change_event.selecter = self.selecter
            
            self.selecter = (self.selecter - 1) % 2
            
            self.select_event.selecter = self.selecter
        
        if self.key.get_key_down("down"):
            self.change_event.selecter = self.selecter
            self.selecter = (self.selecter + 1) % 2
            
            self.select_event.selecter = self.selecter
        
        if self.key.get_key_down("enter") and self.selecter != -1:
            if self.selecter == 0:
                self.scene_loader.scene_load("2player.json")
            elif self.selecter == 1:
                pygame.quit()
                sys.exit()