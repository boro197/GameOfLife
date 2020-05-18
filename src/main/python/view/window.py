from .abstract_widget import AbstractWidget, pg_colors
from .board import Board
from pygame import display, init, quit, event, QUIT, draw, time


class Window(AbstractWidget):
    def __init__(self, parent=None, x=0, y=0, width=0, height=0, color=pg_colors.get("white"), title="Main Window"):
        super().__init__(parent=parent, x=x, y=y, width=width, height=height, color=color)
        self.__title = title
        self.add_component(Board(parent=self, x=0, y=0, width=width, height=height, color=pg_colors.get("blue")))

    def show(self):
        init()
        pyg_clock = time.Clock( )
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

    def process_event(self, new_event):
        if new_event.type == QUIT:
            exit(0)
