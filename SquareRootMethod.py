from SIM import SIM
from numpy import linalg
from GaussMethod import GaussMethod


class SquareRootMethod:
    @staticmethod
    def solve(equation):
        a_t = SquareRootMethod.transpose_matrix([line[:-1] for line in equation.A])
        new_b = SquareRootMethod.matrix_product(a_t, [line[-1:] for line in equation.A])
        equation.A = SquareRootMethod.matrix_product(a_t, [line[:-1] for line in equation.A])

        u = SquareRootMethod.find_matrix_u(equation.A)
        u_t = SquareRootMethod.transpose_matrix(u)

        SIM.print_matrix(u)

        y = SquareRootMethod.solve_system(u_t, new_b)
        x = SquareRootMethod.solve_system(u, y, len(u) - 1, -1)
        print('solution:')
        SIM.print_matrix(x)

    @staticmethod
    def solve_system(matrix_a, vector_b, begin=0, step=1):
        vector_x = [[0] for i in range(len(matrix_a))]
        for i in range(begin, len(matrix_a) if begin == 0 else -1, step):
            s = 0
            for j in range(len(matrix_a)):
                s -= matrix_a[i][j] * vector_x[j][0]
            vector_x[i][0] = (vector_b[i][0] + s) / matrix_a[i][i]

        return vector_x

    @staticmethod
    def matrix_product(matrix_a, matrix_b):
        matrix_c = []
        for i in range(len(matrix_a)):
            matrix_c.append([])
            for j in range(len(matrix_b[0])):
                matrix_c[i].append(0)
                for k in range(len(matrix_b)):
                    matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]

        # SIM.print_matrix(matrix_c)
        return matrix_c

    @staticmethod
    def transpose_matrix(matrix):
        matrix_t = []
        for i in range(len(matrix)):
            matrix_t.append([])
            for j in range(len(matrix)):
                matrix_t[i].append(matrix[j][i])

        return matrix_t

    @staticmethod
    def find_matrix_u(matrix):
        n = len(matrix)

        u = [[0] * n for i in range(n)]

        for i in range(n):
            for j in range(n):
                if j < i:
                    continue
                s = 0
                if i == j:
                    for k in range(n):
                        s += u[k][i] ** 2
                    u[i][j] = (matrix[i][j] - s) ** 0.5
                    continue

                else:
                    for k in range(i):
                        s += u[k][i] * u[k][j]

                    u[i][j] = 1 / u[i][i] * (matrix[i][j] - s)
        return u

    @staticmethod
    def matrix_det(matrix):
        det = 1
        matrix_u = SquareRootMethod.find_matrix_u(matrix)
        for i in range(len(matrix_u)):
            det *= matrix_u[i][i] ** 2.0

        print('kek', det, linalg.det(matrix))

        return det

    @staticmethod
    def find_inverse_matrix(matrix):
        e = [[
            1 if i == j else 0 for j in range(len(matrix))
            ]
            for i in range(len(matrix))
        ]

        matrix = SquareRootMethod.matrix_product(SquareRootMethod.transpose_matrix(matrix), matrix)

        u = SquareRootMethod.find_matrix_u(matrix)
        u_t = SquareRootMethod.transpose_matrix(u)

        SIM.print_matrix(u)
        SIM.print_matrix(u_t)
        y = []

        for i in range(len(matrix)):
            y.append(SquareRootMethod.solve_system(u_t, [line[i:i+1] for line in e]))

        for i in range(len(matrix)):
            print(SquareRootMethod.solve_system(u, y[i], len(u) - 1, -1))

        SIM.print_matrix(linalg.inv(matrix))


