from pygame import display, init, event, draw

from .abstract_widget import AbstractWidget, PG_COLORS
from .board import Board
from .toolbar import Toolbar


class Window(AbstractWidget):
    def __init__(self, parent=None, x=0, y=0, width=0, height=0, color=PG_COLORS.get("white"), title="Main Window"):
        super().__init__(parent=parent, x=x, y=y, width=width, height=height, color=color)
        self.__title = title
        self.__sidebar_height = 100

        board = Board(parent=self, x=2, y=self.__sidebar_height, width=width - 4,
                      height=height - self.__sidebar_height - 2,
                      color=PG_COLORS.get("black"), living_cell_color=PG_COLORS.get('white'))
        toolbar = Toolbar(parent=self, x=2, y=2, width=width - 4, height=self.__sidebar_height - 4,
                          color=PG_COLORS.get("gray40"))

        toolbar.add_controllable_observer(board)

        self.add_component(toolbar)
        self.add_component(board)

    def show(self):
        init()
        screen = display.set_mode([self._width, self._height])
        display.set_caption(self.__title)
        while True:
            for e in event.get():
                self.process_event(e)
            screen.fill(self._color)
            for child in self._children:
                child.show()
            display.flip()