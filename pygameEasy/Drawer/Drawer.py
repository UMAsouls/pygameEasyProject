from typing import Any, Iterable
import pygame
import sys

from pygame.sprite import AbstractGroup

from . import IGameObject

from pygameEasy.Singleton import Singleton

from pygameEasy.Vector import Vector

class NoCameraSettedException(Exception):
    pass

class Drawer(pygame.sprite.LayeredDirty,Singleton):
    rect_list: list[pygame.Rect] = []
    _camera: IGameObject = None
    _zoom: float = 100
    __disp_size: Vector = None
    _started: bool = False
    _window: pygame.Surface = None
    
    @classmethod    
    def get_instance(cls) -> "Drawer":
        if cls._instance == None:
            cls._instance = cls.__internal_new__()
            cls.inited: bool = False
            pygame.sprite.LayeredDirty.__init__(cls._instance)
        
        return cls._instance
    
    @property
    def zoom(self) -> int:
        return self.zoom
    
    @zoom.setter
    def zoom(self, value: float) -> None:
        if(value > 0):
            self._zoom = float(value)
        else:
            self._zoom = 0.01
            
    @property
    def started(self) -> bool:
        return self._started
    
    def set_camera(self, camera: IGameObject) -> None:
        """cameraセット

        Args:
            camera (IGameObject): カメラとなるオブジェクト
        """
        
        self._camera = camera       
    
    #初期化       
    def init(self, window: pygame.Surface) -> None:
        """初期化

        Args:
            window (pygame.Surface): ゲームを映す画面
        """
        
        self.rect_list = []
        self._window = window
        size = window.get_size()
        self.__disp_size = Vector(size[0],size[1])
        pygame.sprite.LayeredDirty.__init__(self)
        self._started = False
    
     
    def make_camera_rect(self) -> pygame.Rect:
        """cameraの位置と拡大倍率から描写範囲を確定させる

        Raises:
            NoCameraSettedException: カメラがセットされていない時の例外

        Returns:
            pygame.Rect: カメラの描写範囲
        """
        
        camera_size: Vector = self.__disp_size / (self._zoom/100)
        camera_rect: pygame.Rect = pygame.Rect(0,0,camera_size.x,camera_size.y)
        
        if self._camera != None:
                camera_rect.center = self._camera.rect.center
        else:
            raise NoCameraSettedException("No camera object is setted")
        
        return camera_rect
        
    #描写
    #cameraとzoomから確定させた描写範囲をlensに映してdisp_sizeに拡大
    def draw(self):
        camera_rect = self.make_camera_rect()
        
        for i in self.sprites():
            i.rect.left -= camera_rect.left
            i.rect.top -= camera_rect.top
        
        lens = pygame.Surface(camera_rect.size)
        lens.fill([50,90,170,0])
        rects = pygame.sprite.LayeredDirty.draw(self,lens)
        
        screen = pygame.transform.scale(
            lens,
            [self.__disp_size.x, self.__disp_size.y]
        )
        
        self._window.blit(screen, [0,0])
        
        #pygame.display.update(self.rect_list)
        self.rect_list = []
        return rects
    
    def sprites(self) -> list[IGameObject]:
        return super().sprites()
    
    def __rect_list_gen(self):
        for i in self.sprites():
            if i.changed:
                yield i.rect
                
    def start(self):
        for i in self.sprites():
            i.start()
            
        self._started = True
    
    def setup(self):
        for i in self.sprites():
            i.setup()
    
    #全てのオブジェクトを一斉に更新させる
    def update(self):
        for i in self.sprites():
            collides: list[IGameObject] = pygame.sprite.spritecollide(i,self,False)
            for j in collides:
                if i.visible:
                    i.on_collide(j)
        
        for i in self.sprites():
            i.setup()
            i.update()
        
        self.rect_list = list(self.__rect_list_gen())
        
        
    def remove(self, *sprites: Any | AbstractGroup | Iterable) -> None:
        for i in sprites:
            self.rect_list.append(i.rect)
        super().remove(*sprites)
           
            
from pygameEasy.DependencyConfig import Config

configs = [
]
            
        