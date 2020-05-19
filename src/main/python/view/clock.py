from pygame import draw, display

from .abstract_widget import AbstractWidget, PG_COLORS


class Clock(AbstractWidget):
    def __init__(self, parent=None, x=0, y=0, width=0, height=0, color=PG_COLORS.get("white")):
        super().__init__(parent=parent, x=x, y=y, width=width, height=height, color=color)

    def show(self):
        screen = display.get_surface()
        draw.rect(screen, self._color, (self._x, self._y, self._width, self._height))
