from math import floor

from controller import BoardController, ButterflyInitArrayStrategy, RandomInitArrayStrategy, ExplosionInitArrayStrategy, \
    ExpansionInitArrayStrategy
from model import BoardModel
from pygame import display, draw
from pygame.font import SysFont

from .abstract_controllable_widget import AbstractControllableWidget
from .abstract_widget import PG_COLORS, pg_constants


class Board(AbstractControllableWidget):
    def __init__(self, parent=None, x=0, y=0, width=0, height=0, cell_size=5, color=PG_COLORS.get('black'),
                 living_cell_color=PG_COLORS.get('white')):
        super().__init__(parent=parent, x=x, y=y, width=width, height=height, color=color)
        self.__cell_size = cell_size
        self.__living_cell_color = living_cell_color
        self.__model = BoardModel(floor(self._width / cell_size), floor(self._height / cell_size))
        self.__controller = BoardController(self.__model, 0.01)
        self.__welcome_message = 'Press play to start !'
        self.__current_strategy_text = 'Current strategy is: '
        self.__instruction_text = 'Press number from 1 to 4 to change strategy.'

    def show(self):
        screen = display.get_surface()
        draw.rect(screen, self._color, (self._x, self._y, self._width, self._height))

        if not self.__controller.stopped:

            cell_x = self._x
            cell_y = self._y

            for line in self.__model.data:
                for cell in line:
                    if cell == 1:
                        draw.rect(screen, self.__living_cell_color,
                                  (cell_x, cell_y, self.__cell_size, self.__cell_size))
                    cell_x = cell_x + self.__cell_size
                cell_y = cell_y + self.__cell_size
                cell_x = self._x

            for child in self._children:
                child.show()
        else:
            font = SysFont('', 60)

            current_strategy_text = self.__current_strategy_text + self.__controller.strategy

            welcome_text = font.render(self.__welcome_message, True, PG_COLORS.get('white'))
            current_strategy = font.render(current_strategy_text, True, PG_COLORS.get('white'))
            instruction_text = font.render(self.__instruction_text, True, PG_COLORS.get('white'))

            text_width, text_height = font.size(self.__welcome_message)
            cs_text_width, cs_text_height = font.size(current_strategy_text)
            i_text_width, i_text_height = font.size(self.__instruction_text)

            screen.blit(welcome_text,
                        (self._x + self._width / 2 - text_width / 2, self._y + self._height / 2 - text_height * 2.5))
            screen.blit(instruction_text,
                        (self._x + self._width / 2 - i_text_width / 2, self._y + self._height / 2 - text_height))
            screen.blit(current_strategy,
                        (self._x + self._width / 2 - cs_text_width / 2, self._y + self._height / 2 + text_height / 2))

    def play(self):
        self.__controller.play()

    def pause(self):
        self.__controller.pause()

    def stop(self):
        self.__controller.stop()

    def process_event(self, new_event):
        if self.__controller.stopped and new_event.type == pg_constants.KEYDOWN:
            if new_event.key == pg_constants.K_1:
                self.__controller.strategy = RandomInitArrayStrategy()
            elif new_event.key == pg_constants.K_2:
                self.__controller.strategy = ButterflyInitArrayStrategy()
            elif new_event.key == pg_constants.K_3:
                self.__controller.strategy = ExplosionInitArrayStrategy()
            elif new_event.key == pg_constants.K_4:
                self.__controller.strategy = ExpansionInitArrayStrategy()
        else:
            for child in self._children:
                child.process_event(new_event)
