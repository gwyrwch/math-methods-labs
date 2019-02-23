from SquareRootMethod import SquareRootMethod
from PrintMethods import PrintMethods
from math import atan
from math import cos
from math import sin


class RotationMethod:
    @staticmethod
    def find_eigenvalue(matrix):
        # RotationMethod.symmetrize_the_matrix(matrix)

        PrintMethods.print_matrix(matrix)
        i, j = RotationMethod.find_i0_j0(matrix)
        print(i, j)
        u0 = RotationMethod.find_u0(matrix, i, j)
        matrix = RotationMethod.do_iteration(matrix, u0)
        PrintMethods.print_matrix(matrix)

    @staticmethod
    def symmetrize_the_matrix(matrix):
        a_t = SquareRootMethod.transpose_matrix(matrix)
        matrix = SquareRootMethod.matrix_product(a_t, matrix)


    @staticmethod
    def find_i0_j0(matrix):
        max_el_cords = [0, 0]
        # max_el = 0
        # for i in range(len(matrix)):
        #     for j in range(len(matrix)):
        #         if i != j and i < j and abs(max_el - abs(matrix[i][j])) < 10 ** -9:
        #             max_el_cords = [i, j]
        #             max_el = max(max_el, matrix[i][j])

        max_el = 0
        for i in range(len(matrix)):
            for k in range(i + 1, len(matrix)):
                if abs(matrix[i][k] > max_el):  # todo: wrong. need epsilon to compare
                    max_el = matrix[i][k]
                    max_el_cords = [i, k]

        return max_el_cords



    @staticmethod
    def find_phi(matrix, i0, j0):
        return 1 / 2 * atan(
            2 * matrix[i0][j0] / (matrix[i0][i0] - matrix[j0][j0])
        )

    @staticmethod
    def find_u0(matrix, i0, j0):
        u0 = [[
            1 if i == j else 0
            for j in range(len(matrix))
        ]
            for i in range(len(matrix))
        ]
        phi = RotationMethod.find_phi(matrix, i0, j0)

        u0[i0][i0] = cos(phi)
        u0[i0][j0] = (-1) * sin(phi)
        u0[j0][i0] = sin(phi)
        u0[j0][j0] = cos(phi)

        PrintMethods.print_matrix(u0)
        return u0

    @staticmethod
    def do_iteration(matrix, u0):
        u0_t = SquareRootMethod.transpose_matrix(u0)
        b = SquareRootMethod.matrix_product(matrix, u0)

        PrintMethods.print_matrix(matrix)
        return SquareRootMethod.matrix_product(u0_t, b)



