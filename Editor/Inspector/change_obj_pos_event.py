from pygame import Event
from GUI import EventData
from dataclasses import dataclass

from __const import CHANGE_OBJ_POS_EVENT

@dataclass
class ChangeObjPosEvent(EventData):
    pos: tuple[int, int]
    
    def make_event(self) -> Event:
        return Event(CHANGE_OBJ_POS_EVENT, pos=self.pos)