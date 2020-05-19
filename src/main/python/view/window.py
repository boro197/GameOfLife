from pygame import display, init, event, draw

from .abstract_widget import AbstractWidget, PG_COLORS
from .board import Board
from .toolbar import Toolbar


class Window(AbstractWidget):
    def __init__(self, parent=None, x=0, y=0, width=0, height=0, color=PG_COLORS.get("white"), title="Main Window"):
        super().__init__(parent=parent, x=x, y=y, width=width, height=height, color=color)
        self.__title = title
        self.__sidebar_height = 100
        self.add_component(
            Toolbar(parent=self, x=0, y=0, width=width, height=self.__sidebar_height, color=PG_COLORS.get("blue3")))
        self.add_component(
            Board(parent=self, x=2, y=self.__sidebar_height, width=width - 4, height=height - self.__sidebar_height -2,
                  color=PG_COLORS.get("gray40"), living_cell_color=PG_COLORS.get('deepskyblue3')))

    def show(self):
        init()
        screen = display.set_mode([self._width, self._height])
        display.set_caption(self.__title)

        while True:
            for e in event.get():
                self.process_event(e)
            screen.fill(self._color)
            draw.circle(screen, (0, 0, 255), (250, 250), 75)
            for child in self._children:
                child.show()
            display.flip()
