from .abstract_init_array_strategy import AbstractInitArrayStrategy


class ExpansionInitArrayStrategy(AbstractInitArrayStrategy):
    def __init__(self):
        super().__init__('Expansion')

    def __call__(self, input_matrix):
        input_matrix[0][1] = 1
        input_matrix[1][0] = 1
        input_matrix[1][1] = 1
        input_matrix[1][2] = 1
        input_matrix[2][2] = 1
        input_matrix[3][2] = 1
        input_matrix[2][1] = 1
        input_matrix[3][1] = 1
        return input_matrix
