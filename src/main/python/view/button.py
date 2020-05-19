from os import path

from pygame import draw, display
from pygame import image, transform

from .abstract_widget import AbstractWidget, PG_COLORS, pg_constants, RESOURCES_PATH


class Button(AbstractWidget):
    def __init__(self, on_click, parent=None, x=0, y=0, width=0, height=0, color=PG_COLORS.get('white'), icon_path=''):
        super().__init__(parent=parent, x=x, y=y, width=width, height=height, color=color)
        self.__on_click = on_click
        self.__icon_path = RESOURCES_PATH + icon_path
        self.__clicked = False

    def show(self):
        screen = display.get_surface()
        if path.exists(self.__icon_path):
            icon = image.load(self.__icon_path)
            icon = transform.scale(icon, (self._width, self._height))
            if self.__clicked:
                icon.fill((255, 255, 255, 128), None, pg_constants.BLEND_RGBA_MULT)
            screen.blit(icon, (self._x, self._y))
        else:
            if self.__icon_path is not "":
                print("Path {0} does not exist !".format(self.__icon_path))
            draw.rect(screen, self._color, (self._x, self._y, self._width, self._height))

    def process_event(self, new_event):
        if new_event.type == pg_constants.MOUSEBUTTONDOWN and self.contains(new_event.pos[0], new_event.pos[1]):
            self.__clicked = True
            self.__on_click()
        if new_event.type == pg_constants.MOUSEBUTTONUP and self.__clicked:
            self.__clicked = False
