from numpy import random


class BoardModel:
    def __init__(self, x_length, y_length):
        self.__matrix = random.randint(2, size=(y_length, x_length))

    @property
    def data(self):
        return self.__matrix
