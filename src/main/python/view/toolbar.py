from pygame import draw, display

from .abstract_controllable_widget import AbstractControllableWidget
from .abstract_widget import PG_COLORS
from .button import Button


class Toolbar(AbstractControllableWidget):
    def __init__(self, parent=None, x=0, y=0, width=0, height=0, color=PG_COLORS.get("white")):
        super().__init__(parent=parent, x=x, y=y, width=width, height=height, color=color)
        margin = 10
        widget_height = height - margin * 2
        self.add_component(
            Button(parent=self, x=margin, y=margin, width=widget_height, height=widget_height,
                   color=PG_COLORS.get("green"), on_click=self.play, icon_path="play.png"))
        self.add_component(
            Button(parent=self, x=widget_height + margin * 2, y=margin, width=widget_height, height=widget_height,
                   color=PG_COLORS.get("blue"), on_click=self.pause, icon_path="pause.png"))
        self.add_component(
            Button(parent=self, x=2 * (widget_height + margin) + margin, y=margin, width=widget_height,
                   height=widget_height,
                   color=PG_COLORS.get("red"), on_click=self.stop, icon_path="stop.png"))

    def play(self):
        for observer in self._observers:
            observer.play()

    def pause(self):
        for observer in self._observers:
            observer.pause()

    def stop(self):
        for observer in self._observers:
            observer.stop()

    def show(self):
        screen = display.get_surface()
        draw.rect(screen, self._color, (self._x, self._y, self._width, self._height))
        for child in self._children:
            child.show()
