from pygame import Event
from dataclasses import dataclass

from GUI import EventData
from __const import CHANGE_SCENE_EVENT

@dataclass
class ChangeSceneEvent(EventData):
    path: str
    
    def make_event(self) -> Event:
        return Event(CHANGE_SCENE_EVENT, {"path": self.path})