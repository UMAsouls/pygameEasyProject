from abc import ABC, abstractmethod

from pygameEasy import *

class IEmulator(ABC):
    def get_obj_selected(self) -> GameObject:
        pass