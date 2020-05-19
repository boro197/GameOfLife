from numpy import random

from .abstract_init_array_strategy import AbstractInitArrayStrategy


class RandomInitArrayStrategy(AbstractInitArrayStrategy):
    def __init__(self):
        super().__init__('Random')

    def __call__(self, input_matrix):
        return random.randint(2, size=(len(input_matrix), len(input_matrix[0])))
