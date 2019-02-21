class OutputMethods:

    @staticmethod
    def print_matrix(matrix):
        for line in matrix:
            print([round(el, 3) for el in line])
        print()

    @staticmethod
    def print_system(matrix):
        for line in matrix:
            print('[', end='')
            for el in line[:-1]:
                print("{:6.3f}".format(el), end=' ')
            print(']', '|', [round(line[-1], 3)])
        print()

    @staticmethod
    def get_answer(matrix_x):
        out = []
        for line in matrix_x:
            out += [line[-1]]

        print('answer: ', [round(el, 3) for el in out])
