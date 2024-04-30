
from Editor.GUI import IDataChangeEvent

class DataChangeEvent(IDataChangeEvent):
    
    def __init__(self, key: str, idx: int, data: int|str) -> None:
        self._key = key
        self._idx = idx
        self._data = data
        
    @property
    def key(self) -> str:
        return self._key
    
    @property
    def idx(self) -> int:
        return self._idx
    
    @property
    def data(self) -> int | str:
        return self._data
    
    def get_dict(self) -> dict:
        return {"key": self.key, "idx": self.idx, "data": self.data}