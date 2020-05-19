from numpy import zeros, random, sum


class BoardController:
    def __init__(self, model):
        self.__model = model
        self.__init_model__()

    def random(self):
        old_matrix = self.__model.data
        self.__model.data = random.randint(2, size=(len(old_matrix), len(old_matrix[0])))

    def expansion_from_left_top_corner(self):
        self.__model.data[0][1] = 1
        self.__model.data[1][0] = 1
        self.__model.data[1][1] = 1
        self.__model.data[1][2] = 1
        self.__model.data[2][2] = 1

    def explosion(self):
        self.__model.data[55][51] = 1
        self.__model.data[56][50] = 1
        self.__model.data[56][51] = 1
        self.__model.data[56][52] = 1
        self.__model.data[57][52] = 1

        self.__model.data[54][40] = 1
        self.__model.data[55][39] = 1
        self.__model.data[55][40] = 1
        self.__model.data[55][41] = 1
        self.__model.data[56][41] = 1

    def butterfly(self):
        self.__model.data[55][51] = 1
        self.__model.data[56][50] = 1
        self.__model.data[56][51] = 1
        self.__model.data[56][52] = 1

    def __init_model__(self):
        self.butterfly()

    def modify_matrix(self):
        old_matrix = self.__model.data
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
        self.__model.data = new_matrix
