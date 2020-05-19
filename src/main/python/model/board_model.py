from numpy import zeros

from .abstract_model import AbstractModel


class BoardModel(AbstractModel):
    def __init__(self, x_length, y_length):
        super().__init__()
        self._data = zeros((y_length, x_length))
