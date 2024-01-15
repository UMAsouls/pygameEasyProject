from pygameEasy.ObjectGroup import ObjectGroup
from pygameEasy.GameObject import GameObject

from .Bar1 import Bar1
from .Base import Base

class HPbar(ObjectGroup):
    def set_data(self, data: dict) -> None:
        super().set_data(data)
        
        self.green:Bar1 = self.get_obj_by_id("bar1")
        self.base:Base = self.get_obj_by_id("base")
        
    def update(self):
        super().update()
        
        self.green.set_ratio(self.base.get_hp_ratio())