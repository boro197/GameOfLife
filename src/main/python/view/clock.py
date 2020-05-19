from .abstract_widget import AbstractWidget, PG_COLORS


class Clock(AbstractWidget):
    def __init__(self, parent=None, x=0, y=0, width=0, height=0, color=PG_COLORS.get("white")):
        super().__init__(parent=parent, x=x, y=y, width=width, height=height, color=color)

    def show(self):
        pass

    def process_event(self, new_event):
        pass
