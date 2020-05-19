from math import floor

from .abstract_init_array_strategy import AbstractInitArrayStrategy


class ButterflyInitArrayStrategy(AbstractInitArrayStrategy):
    def __init__(self):
        super().__init__('Butterfly')

    def __call__(self, input_matrix):
        x_length = floor(len(input_matrix) / 2)
        y_length = floor(len(input_matrix[0]) / 2)

        input_matrix[x_length + 5][x_length + 1] = 1
        input_matrix[x_length + 6][x_length] = 1
        input_matrix[x_length + 6][x_length + 1] = 1
        input_matrix[x_length + 6][x_length + 2] = 1
        return input_matrix
