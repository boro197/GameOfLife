from abc import abstractmethod, ABC


class AbstractInitArrayStrategy(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def __call__(self, input_matrix):
        pass
