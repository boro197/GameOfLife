from abc import ABC, abstractmethod
from pygame.color import THECOLORS as pg_colors
from pygame import display

class AbstractWidget(ABC):
    def __init__(self, parent=None, x=0, y=0, width=0, height=0, color=pg_colors.get("white")):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._parent = parent
        self._children = []

    def contains(self, x, y):
        x_inside = self._x < x < self.x + self._width
        y_inside = self._y < y < self.y + self._height
        return x_inside and y_inside

    def add_component(self, child):
        self._children.append(child)

    def get_screen(self):
        if self._parent is None:
            return display.get_surface()
        else:
            return self._parent.get_screen()

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def process_event(self):
        pass
