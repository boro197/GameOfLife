from math import floor

from controller import BoardController
from model import BoardModel
from pygame import display, draw

from .abstract_widget import AbstractWidget, PG_COLORS


class Board(AbstractWidget):
    def __init__(self, parent=None, x=0, y=0, width=0, height=0, cell_size=5, color=PG_COLORS.get("black"), living_cell_color = PG_COLORS.get("white")):
        super().__init__(parent=parent, x=x, y=y, width=width, height=height, color=color)
        self.__cell_size = cell_size
        self.__living_cell_color= living_cell_color
        self.__model = BoardModel(floor(self._width / cell_size), floor(self._height / cell_size))
        self.__controller = BoardController(self.__model)

    def show(self):
        screen = display.get_surface()
        cell_x = self._x
        cell_y = self._y
        draw.rect(screen, self._color, (self._x, self._y, self._width, self._height))

        for line in self.__model.data:
            for cell in line:
                if cell == 1:
                    draw.rect(screen, self.__living_cell_color, (cell_x, cell_y, self.__cell_size, self.__cell_size))
                cell_x = cell_x + self.__cell_size
            cell_y = cell_y + self.__cell_size
            cell_x = self._x

        for child in self._children:
            child.show()

        self.__controller.modify_matrix()
