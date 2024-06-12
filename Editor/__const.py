from pygame.event import custom_type
from pygame import Event
import pygame

CHANGE_OBJ_EVENT = custom_type()
CHANGE_DATA_EVENT = custom_type()
CHANGE_SCENE_EVENT = custom_type()
CHANGE_OBJ_POS_EVENT = custom_type()

CHANGE_SCENE_EVENT = custom_type()

RECREATE_UI_EVENT = custom_type()

SCENE_SAVE_EVENT = custom_type()

RUN_EVENT = custom_type()
STOP_EVENT = custom_type()

def recreate_event_post() -> None:
    pygame.event.post(Event(RECREATE_UI_EVENT))