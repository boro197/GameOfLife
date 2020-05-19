from .abstract_widget import AbstractWidget, abstractmethod, PG_COLORS


class AbstractControllableWidget(AbstractWidget):

    def __init__(self, parent=None, x=0, y=0, width=0, height=0, color=PG_COLORS.get('white')):
        super().__init__(parent=parent, x=x, y=y, width=width, height=height, color=color)
        self._observers = []

    def add_controllable_observer(self, observer):
        if isinstance(observer, AbstractControllableWidget):
            self._observers.append(observer)
        else:
            raise ValueError('Observer must implement AbstractControllableWidget')

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass
