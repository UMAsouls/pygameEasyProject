from typing import Any
import pygame
from pygame.locals import *
import numpy as np
import sys

from pygameEasy.Vector import Vector

from . import IComponent

from pygameEasy.Drawer import IGameObject as I0
from pygameEasy.Groups import IGameObject as I2
from pygameEasy.ObjectGroup import IGameObject as I3
from . import IGameObject as I4

from pygameEasy.ObjectGroup import IEventBinder as IEB
from pygameEasy.ObjectGroup import IEventListener as IEL

#ピボット（描写位置)
PIVOTS = {
    "topleft":0, "top":1, "topright":2,
    "left":3, "center":4, "right":5,
    "bottomleft":6, "bottom":7, "bottomright":8
    }

#イベントが見つからなかったときの例外
class NotFoundEventException(Exception):
    pass

#全てのオブジェクトの基礎
class GameObject(I0,I2,I3,I4):
    #コンストラクタ
    def __init__(
        self,
        component: IComponent,
        path: str
        ):
        
        super(GameObject,self).__init__()
        
        self._position :Vector = Vector(0,0)
        self.__angle :int = 0
        self.__size :Vector = Vector(0,0)
        self.__pivot :int = 0
        self._name :str = ""
        self._tag :str = ""
        
        self.__base_image :pygame.Surface = pygame.Surface([0,0])
        self.__base_image.fill((0,0,0,255))
        
        self._component = component
        
        self._changed: bool = False
        
        self._path = path
        
        #元々の要素の初期化
        self.__visible :bool = True
        self.layer :int = 5
        self.dirty :int = 2
        self.__image :pygame.Surface = pygame.Surface([0,0])
        self.__rect :pygame.Rect = self.__image.get_rect()
        
        self.__killed: bool = False
        
        self.__event_listners: dict[self.EventListener] = {}
        self.__event_binders: dict[self.EventBinder] = {}
    
    #イベントが発生したことを知らせる
    class EventListener(IEL):
        def __init__(self, type:str):
            self._type: str = type
            self._status = False
            
        @property
        def type(self) -> str:
            return self._type
        
        @property
        def status(self) -> bool:
            return self._status
        
        @status.setter
        def status(self, value: bool) -> None:
            self._status = value
        
    
    #イベントによって起動する処理   
    class EventBinder(IEB):
        def __init__(self, type:str):
            self._type: str = type
            self._bind_func = None
            
        @property
        def type(self) -> str:
            return self._type
        
        #bindする関数を設定
        #propertyでやるとバグる
        def set_func(self, func) -> None:
            self._bind_func = func
            
        def bind(self) -> None:
            self._bind_func()
    
    #ここからセッター、ゲッター    
    @property
    def rect(self) -> pygame.Rect:
        return self.__rect
    
    @rect.setter
    def rect(self, rect: pygame.Rect) -> None:
        self.__rect = rect
        
    @property
    def image(self) -> pygame.Surface:
        return self.__image
    
    @image.setter
    def image(self, image: pygame.Surface) -> None:
        self.__image = image
        
    @property
    def visible(self) -> bool:
        return self.__visible
    
    @visible.setter
    def visible(self, value: bool) -> None:
        self.__visible = value
        self.changed = True
               
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name) ->None:
        self._name = name
        
    @property
    def position(self) -> Vector:
        return self._position.__copy__()
    
    #positionが変わったらそれに合わせてrectも変化する
    @position.setter
    def position(self, pos: Vector | list[int]) -> None:
        if(isinstance(pos, list | tuple)):
            pos = Vector(pos[0], pos[1])
            
        self._position = pos.__copy__()
        
        #componentのpositionもセットし直し
        self.component.position_set()
        
        self.__rect_set()
        self.changed = True
        
    @property
    def changed(self) -> bool:
        return self._changed
    
    @changed.setter
    def changed(self, value: bool) -> None:
        self._changed = value
        
    @property
    def component(self) -> IComponent:
        return self._component
    
    @component.setter
    def component(self, value: IComponent) -> None:
        self._component: IComponent = value
        if(self._component.main != self):
            self._component.main = self
            
    
    @property
    def angle(self) -> int:
        return self.__angle
    
    @angle.setter
    def angle(self, angle: int) -> None:
        self.__angle = angle % 360
        
        if(self.__angle < 0):
            self.__angle = 360 + self.__angle
        
        self.__image_set()
        
    @property
    def size(self) -> Vector:
        return self.__size.__copy__()
    
    @size.setter
    def size(self, size: Vector | tuple[int]) -> None:
        if isinstance(size,Vector): size = size.change2list()
        self.__size.x = size[0]
        self.__size.y = size[1]
        
        if(self.__size.x <= 0): self.__size.x = 1
        if(self.__size.y <= 0): self.__size.y = 1
        
        self.__image_set()
        
    @property
    def _base_image(self) -> pygame.Surface:
        return self.__base_image
    
    @_base_image.setter
    def _base_image(self, surface: pygame.Surface) -> None:
        self.__base_image = surface
        self.changed = True
        self.__rect_set()
        
    @property
    def killed(self) -> bool:
        return self.__killed
    
    #イベントリスナーのゲッター、セッター
    def get_event_listener(self, type: str) -> EventListener:
        try:
            if type in self.__event_listners:
                return self.__event_listners[type]
            else:
                raise NotFoundEventException(f"object called {self.name} doesn't have event type {type}")
        except NotFoundEventException as err:
            print(err)
            pygame.quit()
            sys.exit()
                
    
    def set_event_listener(self, type: str, value: EventListener) -> None:
        try:
            if(isinstance(value, self.EventListener)):
                self.__event_listners[type] = value
            else:
                raise ValueError()
        except ValueError as err:
            print(f"This is not EventListener:", err)
            pygame.quit()
            sys.exit()
            
            
            
    #イベントバインダーのゲッター、セッター
    def get_event_binder(self, type: str) -> EventBinder:
        try:
            if type in self.__event_binders:
                return self.__event_binders[type]
            else:
                raise NotFoundEventException(f"object called {self.name} doesn't have event type {type}")
        except NotFoundEventException as err:
            print(err)
            pygame.quit()
            sys.exit()
    
    def set_event_binder(self, type: str, value: EventBinder) -> None:
        try:
            if(isinstance(value, self.EventBinder)):
                self.__event_binders[type] = value
            else:
                raise ValueError()
        except ValueError as err:
            print(f"This is not EventBinder:", err)
            pygame.quit()
            sys.exit()
        
    #ここまでセッター、ゲッター
    
    #描写位置を変える
    def change_pivot(self, piv):
        if(type(piv) is int):
            self.__pivot = piv % 9
        elif(piv in PIVOTS):
            self.__pivot = PIVOTS[piv]
        else:
            print(f"error: given centence {piv} isn't contained in pivots")
            
    def on_collide(self, obj: "GameObject"):
        pass
    
    #angleやsizeの値の変化に合わせてimageをセット
    def __image_set(self):
        image: pygame.Surface = pygame.transform.scale(self._base_image,self.__size.change2list())
        image = pygame.transform.rotozoom(image, self.__angle, 1)
        rect = image.get_rect()
        size = self.size.change2list()
        
        #angleが90で割り切れるときはこの特殊処理をしないとサイズがバグる
        #rect_sizeの計算式のせい
        if(self.__angle % 90 == 0):
            self.image = image
            self.rect = self.image.get_rect()
            self.changed = True
            self.__rect_set()
            return
        
        #transform.rotozoomはimageのサイズを変化させるため、それに合わせた変更が必要  
        rect.size = [
            abs(size[0]*np.cos(np.deg2rad(self.__angle))) + abs(size[1]*np.sin(np.deg2rad(self.__angle))),
            abs(size[1]*np.cos(np.deg2rad(self.__angle))) + abs(size[0]*np.sin(np.deg2rad(self.__angle)))
        ]
        
        rect.center = [image.get_width()//2, image.get_height()//2]
        self.image = image.subsurface(rect)
        
        self.rect = self.image.get_rect()
        self.changed = True
        self.__rect_set()
    
    #positionをrectにセット
    def __rect_set(self):
        size = self.rect.size
        pos = self._position
        if(self.component.root != self.component):
            pos += self.component.parent.position
            
        if(self.__pivot == 0):
            self.rect.topleft = pos.change2list()
        elif(self.__pivot == 1):
            self.rect.midtop = pos.change2list()
        elif(self.__pivot == 2):
            self.rect.topright = pos.change2list()
        elif(self.__pivot == 3):
            self.rect.midleft = pos.change2list()
        elif(self.__pivot == 4):
            self.rect.center = pos.change2list()
        elif(self.__pivot == 5):
            self.rect.midright = pos.change2list()
        elif(self.__pivot == 6):
            self.rect.bottomleft = pos.change2list()
        elif(self.__pivot == 7):
            self.rect.midbottom = pos.change2list()
        elif(self.__pivot == 8):
            self.rect.bottomright = pos.change2list()
        else:
            pass
        
        self.rect.size = size
        
    def get_onscreen_rect(self, camera:"GameObject") -> pygame.Rect:
        rect_copy = self.rect.copy()
        rect_copy.left -= camera.rect.left
        rect_copy.top -= camera.rect.top
        return rect_copy
    
    #更新処理  
    def update(self):
        pygame.sprite.DirtySprite.update(self)
        
        if not self.visible:
            return
        
        self.__rect_set()
            
            
    #jsonデータのセット       
    def set_data(self, data):
        self._name = data["name"]
        if("tag" in data): self.tag = data["tag"]
        
        self._position = Vector(data["pos"][0], data["pos"][1])
        
        if("layer" in data): self.layer = data["layer"]
        
        if("path" in data):
            self._base_image = pygame.image.load(self._path + f"/image/{data['path']}")
        self.image = self._base_image.subsurface(self._base_image.get_rect())
        self.rect = self.image.get_rect()
        
        self.component = self._component
        
        self.__size = Vector(self.rect.width,self.rect.height)
        self.__angle = 0
        
        self.__rect_set()
        
        if("size" in data): self.size = Vector(data["size"][0], data["size"][1])
        
        
    def kill(self):
        self.__killed = True
        self.component.kill()
        
        for i in self.groups():
            i.remove(self)
        
        del self
        
        

