import abc

class IKey(metaclass = abc.ABCMeta):
    @abc.abstractclassmethod
    def get_key_down(self, key) -> bool:
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def get_key_repeat(self, key) -> bool:
        raise NotImplementedError()
        
    @abc.abstractclassmethod
    def get_key_up(self, key) -> bool:
        raise NotImplementedError()