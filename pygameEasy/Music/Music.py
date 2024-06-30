import pygame
from pygame.mixer import *
from pygame.locals import *

from pygameEasy.Singleton import Singleton

BGM_END = 25
BGM_CHANGE = 26
BGM_STOP = 27

class Music(Singleton):
    pygame.mixer.init()
    _bgm_channel = Channel(0)
    _bgm_loop: Sound = None
    
    _effect_channels = [
        Channel(1),
        Channel(2),
        Channel(3)
    ]
    _effect_move = 0
    
    _voice_channels = [
        Channel(4),
        Channel(5),
        Channel(6)
    ]
    _voice_move = 0
    
    _other_channel = Channel(7)
    
    _path: str = ""
    
    def set_path(self, path: str) -> None:
        self._path = path
    
    def get_sound(self, path: str) -> Sound:
        sound: Sound = Sound(self._path + "/Music/" + path)
        
        return sound
    
    def play_bgm(self, sound: Sound, loop_sound: Sound = None) -> None:
        self._bgm_channel.play(sound)
        
        if loop_sound != None:
            self._bgm_loop = loop_sound
        else:
            self._bgm_loop = sound
            
        self._bgm_channel.set_endevent(BGM_END)
        
    def set_next_bgm(self, sound: Sound, loop_sound: Sound = None) -> None:
        self._bgm_channel.queue(sound)
        
        if loop_sound != None:
            self._bgm_loop = loop_sound
        else:
            self._bgm_loop = sound
            
        self._bgm_channel.set_endevent(BGM_CHANGE)
        
    def stop_bgm(self, fadetime: int = 0):
        self._bgm_channel.set_endevent(BGM_STOP)
        self._bgm_channel.fadeout(fadetime)
    
    def play_effect(self, sound: Sound, maxtime: int = 0) -> None:
        
        for i in self._effect_channels:
            if not i.get_busy():
                i.play(sound, maxtime= maxtime)
                return
            
        self._effect_channels[self._effect_move].play(sound, maxtime=maxtime)
        self._effect_move = (self._effect_move + 1) % 3
        
        
    def update(self) -> None:
        if pygame.event.peek(BGM_END):
            self._bgm_channel.play(self._bgm_loop)
        
            
