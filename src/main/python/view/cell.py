from .abstract_widget import AbstractWidget, pg_colors
from pygame import display, draw


class Cell(AbstractWidget):
    def __init__(self, parent=None, x=0, y=0, width=0, height=0, cell_size=10, color=pg_colors.get("white")):
        super().__init__(parent=parent, x=x, y=y, width=width, height=height, color=color)

    def show(self):
        screen = self.get_screen()
        screen.fill(self._color)
        cell_x = self._x
        cell_y = self._y
        draw.rect(screen, self._color, (self._x, self._y, self._width, self._height))

    def process_event(self):
        pass
