from abc import ABC, abstractmethod

from pygame.color import THECOLORS as PG_COLORS
from pygame import constants as pg_constants

RESOURCES_PATH = "C:\\Users\\tborowiak\\PycharmProjects\\GameOfLife\\src\\main\\resources\\"


class AbstractWidget(ABC):
    def __init__(self, parent=None, x=0, y=0, width=0, height=0, color=PG_COLORS.get("white")):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._parent = parent
        self._children = []
        self._external_dialog_opened = False

    def contains(self, x, y):
        x_inside = self._x < x < self._x + self._width
        y_inside = self._y < y < self._y + self._height
        return x_inside and y_inside

    def add_component(self, child):
        self._children.append(child)

    @abstractmethod
    def show(self):
        pass

    def process_event(self, new_event):
        for child in self._children:
            child.process_event(new_event)
