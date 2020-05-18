from .abstract_widget import AbstractWidget, pg_colors
from .cell import Cell
from model import BoardModel
from pygame import display, draw
from random import randint


class Board(AbstractWidget):
    def __init__(self, parent=None, x=0, y=0, width=0, height=0, cell_size=10, color=pg_colors.get("white")):
        super().__init__(parent=parent, x=x, y=y, width=width, height=height, color=color)
        self.__model = BoardModel(100, 100)
        self.__cell_size = cell_size

    def __add_cells__(self):
        cell_x = self._x
        cell_y = self._y
        while cell_y < self._y + self._height:
            while cell_x < self._width:
                self.add_component(
                    Cell(parent=self, x=cell_x, y=cell_y, width=self.__cell_size, height=self.__cell_size,
                         color=pg_colors.get("red")))
                cell_x = cell_x + 10
            cell_y = cell_y + self.__cell_size
            cell_x = 0

    def show(self):
        screen = display.get_surface()
        screen.fill(self._color)
        cell_x = self._x
        cell_y = self._y

        for line in self.__model.data:
            for cell in line:
                if cell == 1:
                    c = pg_colors.get("black")
                else:
                    c = pg_colors.get("white")
                draw.rect(screen, c, (cell_x, cell_y, self.__cell_size, self.__cell_size))
                cell_x = cell_x + self.__cell_size
            cell_y = cell_y + self.__cell_size
            cell_x = self._x

        for child in self._children:
            child.show()

    def process_event(self):
        pass
