from abc import ABC, abstractmethod
import pygame

class Iinspector(ABC):
    
    @abstractmethod
    def recreate_ui(self) -> None:
        pass
    
    @abstractmethod
    def set_obj_data(self, data: dict[str, str|int|list|dict]) -> None:
        pass
    
    @abstractmethod
    def process_event(self, event: pygame.Event) -> None:
        pass
    
    @abstractmethod
    def pos_data_change(self, data: tuple[int, int]) -> None:
        pass
    
    @abstractmethod
    def reset(self) -> None:
        pass