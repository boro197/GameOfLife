from pygame import draw, display

from .abstract_widget import AbstractWidget, PG_COLORS
from .button import Button
from .clock import Clock


class Toolbar(AbstractWidget):
    def __init__(self, parent=None, x=0, y=0, width=0, height=0, color=PG_COLORS.get("white")):
        super().__init__(parent=parent, x=x, y=y, width=width, height=height, color=color)
        self.add_component(
            Clock(parent=self, x=0, y=0, width=100, height=100,
                  color=PG_COLORS.get("green")))
        self.add_component(
            Button(parent=self, x=0, y=0, width=100, height=100,
                   color=PG_COLORS.get("green"), on_click=self.play))
        self.add_component(
            Button(parent=self, x=0, y=0, width=100, height=100,
                   color=PG_COLORS.get("green"), on_click=self.pause))
        self.add_component(
            Button(parent=self, x=0, y=0, width=100, height=100,
                   color=PG_COLORS.get("green"), on_click=self.stop))

    def play(self):
        print("play")

    def pause(self):
        print("pause")

    def stop(self):
        print("stop")

    def show(self):
        screen = display.get_surface()
        draw.rect(screen, self._color, (self._x, self._y, self._width, self._height))
        for child in self._children:
            child.show()
