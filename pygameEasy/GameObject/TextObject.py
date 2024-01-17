from typing import Any
import pygame
from pygame.locals import *
import os
import sys

from pygameEasy.Vector import Vector
from . import IComponent

from .GameObject import GameObject

PROJECT_PATH = os.path.dirname(os.getcwd())

class TextObject(GameObject):
    def __init__(
            self,
            component: IComponent,
            path: str
            ):
        super().__init__(component, path)
        
        self.__text: str = ""
        self.__font: pygame.font.Font = None
        self.__text_size: int = 50
        self.__color: tuple[int] = (0,0,0,0)
        self.__antialias = False
    
    def __render(self):
        self._base_image = self.font.render(self.text, self.antialias, self.color)
        if(self.text != ""):
            self.size = self.font.size(self.text)
        else:
            self.size = [0,0]
        
        
    @property
    def text(self) -> str:
        return self.__text
    
    @text.setter
    def text(self, text: str) -> None:
        self.__text = text
        self.__render()
        
    @property
    def font(self) -> pygame.font.Font:
        return self.__font
    
    @font.setter
    def font(self, font: pygame.font.Font) -> None:
        self.__font = font
        self.__render()
        
    @property
    def text_size(self) -> int:
        return self.__text_size
    
    @text_size.setter
    def text_size(self, size) -> None:
        self.__text_size = size
        self.__render()
        
    @property
    def color(self) -> tuple[int]:
        return self.__color
    
    @color.setter
    def color(self, color: tuple[int]):
        self.__color = color
        self.__render()
        
    @property
    def antialias(self) -> bool:
        return self.__antialias
    
    @antialias.setter
    def antialias(self, value: bool) -> None:
        self.__antialias = value
        self.__render() 
        
    def set_data(self, data) -> None:
        super().set_data(data)
        
        if(data["text_size"] != None):
            self.__text_size = data["text_size"]
        
        if(data["TTF"] != None):
            self.__font = pygame.font.Font(self._path + f"/TTF/{data['TTF']}",self.__text_size)
        else:
            self.__font = pygame.font.SysFont("HGゴシックM",self.__text_size)
            
        if(data["color"] != []):
            self.__color = (
                data["color"]["red"],
                data["color"]["green"],
                data["color"]["blue"],
                data["color"]["trans"]
            )
        
        if(data["antialias"] != None):
            self.__antialias = data["antialias"]
            
        if(data["text"] != None):
            self.__text = data["text"]
        else:
            self.__text = ""
            
        self.__render()
        