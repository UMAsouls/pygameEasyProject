import abc
from typing import Any


class Singleton:
    _instance: "Singleton" = None
    
    #これが呼ばれるということはコンストラクタから呼ばれている
    #エラーを吐く
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("コンストラクタを呼ばないで")
    
    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)
    
    #こっちが実質的なコンストラクタ
    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = cls.__internal_new__()
            cls.inited: bool = False
        
        return cls._instance
    
    
        
            
            