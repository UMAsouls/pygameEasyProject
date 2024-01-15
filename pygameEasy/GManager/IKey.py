import abc

class IKey(metaclass = abc.ABCMeta):
    @abc.abstractclassmethod
    def update(self):
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def key_up_update(self):
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def key_down_update(self):
        raise NotImplementedError()