from pygame import Event
from dataclasses import dataclass

from GUI import EventData
from __const import CHANGE_DATA_EVENT

@dataclass
class DataChangeEvent(EventData):
    key:str
    idx:int
    data: int|str
    
    def make_event(self) -> Event:
        return super().make_event(CHANGE_DATA_EVENT, key=self.key, idx=self.idx, data=self.data)