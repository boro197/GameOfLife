from math import floor

from .abstract_init_array_strategy import AbstractInitArrayStrategy


class ExplosionInitArrayStrategy(AbstractInitArrayStrategy):
    def __init__(self):
        super().__init__("Explosion")

    def __call__(self, input_matrix):
        x_length = floor(len(input_matrix) / 2)
        y_length = floor(len(input_matrix[0]) / 2)
        input_matrix[x_length + 5][x_length + 1] = 1
        input_matrix[x_length + 6][x_length] = 1
        input_matrix[x_length + 6][x_length + 1] = 1
        input_matrix[x_length + 6][x_length + 2] = 1
        input_matrix[x_length + 7][x_length + 2] = 1

        input_matrix[x_length + 4][x_length - 10] = 1
        input_matrix[x_length + 5][x_length - 11] = 1
        input_matrix[x_length + 5][x_length - 10] = 1
        input_matrix[x_length + 5][x_length - 9] = 1
        input_matrix[x_length + 6][x_length - 9] = 1

        return input_matrix
