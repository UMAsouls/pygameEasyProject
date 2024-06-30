import pygame
from pygame.locals import *
import injector

from pygameEasy.Singleton import Singleton

#全てのアルファベットの辞書
key_dict = {pygame.key.name(K_a+i) : K_a+i for i in range(26)}

key_dict = key_dict | {pygame.key.name(K_0+i) : K_0+i for i in range(10)}

key_dict["enter"] = K_RETURN
key_dict["space"] = K_SPACE
key_dict["up"] = K_UP
key_dict["down"] = K_DOWN
key_dict["left"] = K_LEFT
key_dict["right"] = K_RIGHT
key_dict["back"] = K_BACKSPACE
key_dict["R_shift"] = K_RSHIFT

@injector.singleton
class Key(Singleton):
    _key = {}
    for k in key_dict.keys():
        _key[k] = {
            "down": False,
            "repeat": False,
            "up": False
        }

    def get_key_down(self, key: str) -> bool:
        return self._key[key]["down"]
    
    def get_key_repeat(self, key: str) -> bool:
        return self._key[key]["repeat"]
    
    def get_key_up(self, key: str) -> bool:
        return self._key[key]["up"]
            
    def update(self):
        for k,v in self._key.items():
            v["down"] = False
            v["up"] = False
            self._key[k] = v
        
    def key_down_update(self, event: pygame.event.Event):
        for k in self._key:
            if(event.key == key_dict[k]):
                self._key[k]["down"] = True
                self._key[k]["repeat"] = True
    
    def key_up_update(self, event: pygame.event.Event):
        for k in self._key:
            if(event.key == key_dict[k]):
                self._key[k]["up"] = True
                self._key[k]["repeat"] = False
                    