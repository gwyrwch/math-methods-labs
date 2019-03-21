from SquareRootMethod import SquareRootMethod
from PrintMethods import PrintMethods
from math import atan
from math import cos
from math import sin
from numpy import linalg


class RotationMethod:
    @staticmethod
    def find_eigenvalue(matrix):
        output_file = open("output.txt", 'w')
        epsilon = 0.001
        matrix = RotationMethod.symmetrize_the_matrix(matrix)
        output_file.write('\n'.join(["Symmetrized matrix :"]))
        output_file.write('\n')

        output_file.write('\n'.join([
            str([round(el, 3) for el in i])
            for i in matrix
        ]))
        output_file.write('\n\n')

        u = [[
            1 if i == j else 0
            for j in range(len(matrix))
        ]
            for i in range(len(matrix))
        ]
        cnt = 0
        while True:
            i, j = RotationMethod.find_i0_j0(matrix)
            if abs(matrix[i][j]) < epsilon:
                break

            output_file.write(" ".join(["Position of max element: ", str(round(matrix[i][j], 3)), "is", str(i), str(j)]))
            output_file.write('\n')

            u0 = RotationMethod.find_u0(matrix, i, j)
            output_file.write("Matrix U" + str(cnt))
            output_file.write('\n')

            output_file.write('\n'.join([
                str([(round(el, 3)) for el in i])
                for i in u0
            ]))
            output_file.write('\n')

            u = SquareRootMethod.matrix_product(u, u0)
            matrix = RotationMethod.do_iteration(matrix, u0)

            output_file.write("Matrix A" + str(cnt))
            output_file.write('\n')

            output_file.write('\n'.join([
                str([(round(el, 3)) for el in i])
                for i in matrix
            ]))
            output_file.write('\n\n')

            cnt += 1

        print("Results with rotation method: ", "Matrix eigenvalues: ", sep="\n")
        for i in range(len(matrix)):
            print(round(matrix[i][i], 3), end=" ")

        print("\n\nMatrix eigenvectors: ")
        PrintMethods.print_matrix(u)

    @staticmethod
    def symmetrize_the_matrix(matrix):
        a_t = SquareRootMethod.transpose_matrix(matrix)
        matrix = SquareRootMethod.matrix_product(a_t, matrix)
        return matrix

    @staticmethod
    def check_with_numpy(matrix):
        print("Results with numpy library: ", "Matrix eigenvalues: ", sep="\n")
        matrix = RotationMethod.symmetrize_the_matrix(matrix)
        for i in linalg.eig(matrix)[0]:
            print(round(i, 3), end=" ")

        print("\n\nMatrix eigenvectors: ")
        PrintMethods.print_matrix(linalg.eig(matrix)[1])

    @staticmethod
    def find_i0_j0(matrix):
        max_el_cords = [0, 0]
        max_el = 0
        for i in range(len(matrix)):
            for k in range(i + 1, len(matrix)):
                if abs(matrix[i][k]) > max_el:
                    max_el = abs(matrix[i][k])
                    max_el_cords = [i, k]

        return max_el_cords

    @staticmethod
    def find_phi(matrix, i0, j0):
        if abs(matrix[i0][i0] - matrix[j0][j0]) == 10**-9:
            raise ZeroDivisionError()

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

        return u0

    @staticmethod
    def do_iteration(matrix, u0):
        u0_t = SquareRootMethod.transpose_matrix(u0)
        b = SquareRootMethod.matrix_product(matrix, u0)

        return SquareRootMethod.matrix_product(u0_t, b)



