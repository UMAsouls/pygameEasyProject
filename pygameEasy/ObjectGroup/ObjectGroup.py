from collections.abc import Generator
import pygame
import sys
import injector
import os
from enum import Flag, auto

from .IGameObject import IGameObject
from .IEventListener import IEventListener
from .IEventBinder import IEventBinder

from pygameEasy.Groups import IObjectGroup as I0
from pygameEasy.GameObject import IObjectGroup as I1

#GameObjectをまとめて管理できるオブジェクト
#色々なメタ的な動作をさせられる
class ObjectGroup(I0,I1):
    def __init__(
        self
        ) -> None:
        super().__init__()
        
        self._name: str = ""
        
        self.id_dict : dict[str, list[IGameObject]] = {}
        self.name_dict: dict[str, int] = {}
        self.type_dict: dict[str, list[int]] = {}
        
        self._events: list[ObjectGroup.Event] = []
        
    abc = 0
        
    
    class Event:
        class LisType(Flag):
            NULL = auto()
            AND = auto()
            OR = auto()
            
        class BinType(Flag):
            NULL = auto()
            ALL = auto()
            SELECT = auto()
            RANGE = auto()
        
        def __init__(self, listype: LisType, bintype: BinType):
            self._listener: list[IEventListener] = []
            self._binder: list[IEventBinder] = []
            
            self._listype: self.LisType = listype
            self._bintype: self.BinType = bintype
            
            #bindするindex
            #bintype = SELECTで用いる
            self._selecter: int = -1
            
            #bindする範囲
            #bintype = RANGEで用いる
            self._bind_range: list[tuple[int]] = []
        
        #リスナーセット
        #grpにあるobjectを追加させる(id指定)
        def set_listener(self, grp: "ObjectGroup", type:str, *id: str):
            obj_list: list[IGameObject] = []
            for i in id:
                obj_list += grp.get_obj_list_by_id(i)
            
            self._listener = [i.get_event_listener(type) for i in obj_list]
        
        #バインダーセット
        #grpにあるobjectを追加させる(id指定)
        def set_binder(self, grp: "ObjectGroup", type:str, *id: str):
            obj_list: list[IGameObject] = []
            for i in id:
                obj_list += grp.get_obj_list_by_id(i)
            
            self._binder = [i.get_event_binder(type) for i in obj_list]
        
        #bindする範囲を追加する   
        def add_bind_range(self, start: int, end: int):
            if(len(self._binder)):
                start = start % len(self._binder)
            else:
                start = 0
                
            if(len(self._binder)):
                end = end % len(self._binder)
            else:
                end = 0
            
            try:
                if(end < start): raise ValueError
            except ValueError:
                print("Range error: failed to add")
            
            self._bind_range.append((start,end))
            
        #bind_rangeをリセット
        def reset_bind_range(self):
            self._bind_range = []
            
        #selecterのゲッター,セッター
        @property
        def selecter(self) -> int:
            return self._selecter
        
        @selecter.setter
        def selecter(self, value: int) -> None:
            if len(self._binder):
                self._selecter = value % len(self._binder)
            else:
                self._selecter = -1
                
        def selecter_stop(self):
            self._selecter = -1

        
        #listype == AND
        #AND処理
        #イベントリストの全てが活性化していたらbind
        def and_checker(self) -> bool:
            checker: bool = True
            for i in self._listener:
                if not i.status:
                    checker = False
                    
            return checker
        
        #listype == OR
        #OR処理
        #イベントが一つでも活性化していたらbind            
        def or_checker(self):
            for i in self._listener:
                if i.status:
                    return True
            
        def check(self) -> bool:
            if self._listype == self.LisType.AND:
                return self.and_checker()
            elif self._listype == self.LisType.OR:
                return self.or_checker()
            elif self._listype == self.LisType.NULL:
                return True
        
        #中断and終了処理
        #全てのイベントリスナを非活性にさせる
        def cancel(self) -> None:
            for i in self._listener:
                i.status = False
        
        #bintype == ALL
        #全ての実行イベントを起動       
        def all_bind(self) -> None:
            for i in self._binder:
                i.bind()
        
        #bintype == SELECT
        
        def select_bind(self) -> None:
            #selecter = -1 で何もしない
            if self.selecter == -1: return
            self._binder[self._selecter].bind()
        
        #bintype == RANGE
        #bind_range変数によって指定したものを起動
        def range_bind(self) -> None:
            for i in self._bind_range:
                for j in range(i[0],i[1]):
                    self._binder[j].bind()
                     
        #イベント実行
        def bind(self) -> None:
            if self._bintype == self.BinType.ALL:
                self.all_bind()
            elif self._bintype == self.BinType.SELECT:
                self.select_bind()
            elif self._bintype == self.BinType.RANGE:
                self.range_bind()
            elif self._bintype == self.BinType.NULL:
                pass
            
            self.cancel()
        
        #更新処理    
        def update(self) -> None:
            if self.check():
                self.bind()
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, n:str) -> None:
        self._name = n
    
    #指定した名前と同じオブジェクト全てを返す
    def get_objects(self, name: str) -> Generator:
        for i in self.sprites():
            if(i.name == name):
                yield i
                
    def sprites(self) -> list[IGameObject]:
        return super().sprites()
    
    def set_obj(self, id:str, obj: list[IGameObject]):
        self.id_dict[id] = [i for i in obj]
        self.add(obj)
        
    
    def set_event(self, event:Event):
        self._events.append(event)
        
        
    def set_data(self, data: dict) -> None:
        self._name = data["name"]
    
    #指定したidのオブジェクトのリストを返す
    def get_obj_list_by_id(self, id: str) -> list[IGameObject]:
        return self.id_dict[id]
    
    #指定したidのオブジェクトリストの先頭を返す        
    def get_obj_by_id(self, id: str) -> IGameObject:
        return self.id_dict[id][0]
    
    #イベントのupdate 
    def event_check(self) -> None:
        for i in self._events:
            i.update()
        
    def update(self):
        pass
