from numpy import zeros


class BoardModel:
    def __init__(self, x_length, y_length):
        self.__matrix = zeros((y_length, x_length))

    @property
    def data(self):
        return self.__matrix

    @data.setter
    def data(self, data):
        self.__matrix = data
