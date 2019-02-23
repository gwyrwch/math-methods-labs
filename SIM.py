from GaussMethod import GaussMethod
from math import log


class SIM:

    @staticmethod
    def solve(equation):
        SIM.convert_system(equation)

        matrixB = [line[:-1] for line in equation.A]
        rateB = GaussMethod.matrixRate(matrixB)
        print('Rate of matrix B: ',rateB, '<', 1, '--', rateB < 1)

        SIM.print_matrix(equation.A)
        print()
        SIM.do_iteration(equation, 0)
        SIM.do_iteration(equation, 1)
        k = SIM.get_number_of_iterations(
            rateB,
            [line[0] for line in equation.x_matrix],
            [line[1] for line in equation.x_matrix]
        )

        for i in range(2, k + 1):
            SIM.do_iteration(equation, i)

    @staticmethod
    def convert_system(equation):
        for i in range(equation.n):
            divider = equation.A[i][i]
            for j in range(equation.m + 1):
                equation.A[i][j] /= divider

        E = [[
                1 if i == j else 0
                for j in range(equation.n)
            ]
            for i in range(equation.n)
        ]

        for i in range(equation.n):
            for j in range(equation.n):
                equation.A[i][j] = E[i][j] - equation.A[i][j]

    @staticmethod
    def get_number_of_iterations(rateB, x0, x1):
        epsilon = 0.01
        rate_x = 0
        for i in range(len(x0)):
            rate_x = max(rate_x, abs(x0[i] - x1[i]))

        return round(log(epsilon / rate_x * (1 - rateB), rateB)) + 1

    @staticmethod
    def do_iteration(equation, iter_num):
        if iter_num == 0:
            for i in range(equation.n):
                equation.x_matrix[i][iter_num] = equation.A[i][equation.m]
            return

        for i in range(equation.n):
            for j in range(equation.n):
                equation.x_matrix[i][iter_num] += equation.x_matrix[j][iter_num - 1] * equation.A[i][j]
            equation.x_matrix[i][iter_num] += equation.A[i][equation.m]

        print('iteration', iter_num, ':')
        SIM.print_matrix(equation.x_matrix)

    @staticmethod
    def print_matrix(matrix):
        for line in matrix:
            print([round(el, 3) for el in line])
        print()
