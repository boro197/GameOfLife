from threading import Timer

from numpy import zeros, sum

from .abstract_controller import AbstractController
from .abstract_init_array_strategy import AbstractInitArrayStrategy
from .random_init_array_strategy import RandomInitArrayStrategy


class BoardController(AbstractController):
    def __init__(self, model, refresh_interval=0.1, init_strategy=RandomInitArrayStrategy()):
        super().__init__(model)
        self.__running = False
        self.__stopped = True
        self.__interval = refresh_interval
        self.__timer = None
        self.__init_strategy = init_strategy

    @property
    def running(self):
        return self.__running

    @property
    def stopped(self):
        return self.__stopped

    @property
    def strategy(self):
        return self.__init_strategy.name

    @strategy.setter
    def strategy(self, strategy):
        if isinstance(strategy, AbstractInitArrayStrategy):
            self.__init_strategy = strategy
        else:
            raise ValueError('Incorrect strategy type')

    def init_model(self):
        self._model.data = zeros((len(self._model.data), len(self._model.data[0])))
        self._model.data = self.__init_strategy(self._model.data)

    def modify_matrix(self):
        if self.__running:
            old_matrix = self._model.data
            new_matrix = zeros((len(old_matrix), len(old_matrix[0])))
            for i in range(0, len(old_matrix)):
                for j in range(0, len(old_matrix[0])):
                    region = old_matrix[max(0, i - 1): i + 2, max(0, j - 1): j + 2]
                    neighbours = sum(region)
                    if neighbours == 3:
                        new_matrix[i][j] = 1
                    elif neighbours > 4 or neighbours < 2:
                        new_matrix[i][j] = 0
                    else:
                        new_matrix[i][j] = old_matrix[i][j]
            self._model.data = new_matrix
            self.__timer = Timer(self.__interval, self.modify_matrix)
            self.__timer.start()

    def play(self):
        if self.__stopped:
            self.init_model()
        if not self.__running:
            self.__stopped = False
            self.__running = True
            self.modify_matrix()

    def pause(self):
        if self.__running:
            self.__running = False
            if self.__timer is not None:
                self.__timer.cancel()

    def stop(self):
        self.__running = False
        self.__stopped = True
        if self.__timer is not None:
            self.__timer.cancel()
        self._model.data = zeros((len(self._model.data), len(self._model.data[0])))
