from OutputMethods import OutputMethods
from numpy import linalg


class GaussMethod:
    @staticmethod
    def solve(equation):
        eps = 10 ** -3

        print('Step by step solution. Direct move: ')
        for i in range(min(equation.n, equation.m)):
            if abs(equation.A[i][i]) < eps:
                bad = True
                for k in range(i + 1, equation.n):
                    if abs(equation.A[k][i]) > eps:
                        equation.A[k], equation.A[i] = equation.A[i], equation.A[k]
                        bad = False
                        break
                if bad:
                    continue

            for j in range(i + 1, equation.n):
                factor = equation.A[j][i] / equation.A[i][i]
                for k in range(0, equation.m + 1):
                    equation.A[j][k] -= equation.A[i][k] * factor
            OutputMethods.print_system(equation.A)

        print('Using back-substitution: ')
        for i in range(equation.m - 1, -1, -1):
            if i >= equation.n or abs(equation.A[i][i]) < eps:
                equation.X.append(0)
                continue

            s = 0
            for k in range(equation.m - 1, i, -1):
                s += equation.A[i][k] * equation.X[equation.m - 1 - k]
            x = round((equation.A[i][equation.m] - s) / equation.A[i][i], 4)
            equation.X.append(x)
            print(equation.X)

        equation.X.reverse()

        wrong = False
        for j in range(equation.n):
            s = 0
            for i in range(equation.m):
                s += equation.X[i] * equation.A[j][i]

            wrong = wrong or abs(s - equation.A[j][equation.m]) > eps

        if wrong:
            print('No solution')
            return

    @staticmethod
    def inverse_matrix(matrix):
        eps = 10 ** -9
        m = len(matrix[0])

        for i in range(len(matrix)):
            for j in range(m):
                matrix[i] += [1] if i == j else [0]

        m = len(matrix[0])
        print('Extended matrix:')
        OutputMethods.print_extended_matrix(matrix)

        print('Step by step solution. Direct move: ')
        for i in range(min(len(matrix), m)):
            if abs(matrix[i][i]) < eps:
                bad = True
                for k in range(i + 1, len(matrix)):
                    if abs(matrix[k][i]) > eps:
                        matrix[k], matrix[i] = matrix[i], matrix[k]
                        bad = False
                        break
                if bad:
                    continue

            for j in range(i + 1, len(matrix)):
                factor = matrix[j][i] / matrix[i][i]
                for k in range(0, m):
                    matrix[j][k] -= matrix[i][k] * factor

            OutputMethods.print_extended_matrix(matrix)

        print('Using reverse: ')
        for i in range(len(matrix) - 1, -1, -1):
            divider = matrix[i][i]
            for j in range(m):
                if abs(matrix[i][j]) > eps:
                    matrix[i][j] /= divider

            for j in range(i + 1, len(matrix)):
                factor = matrix[i][j]
                for k in range(0, m):
                    matrix[i][k] -= matrix[j][k] * factor

            OutputMethods.print_extended_matrix(matrix)

        m = len(matrix[0]) // 2
        matrix = [line[m:] for line in matrix]

        matrix = [[
                round(j, 4) for j in i
            ]
            for i in matrix
        ]

        return matrix

    @staticmethod
    def error_estimates(init_matrix, x):
        rate_a = GaussMethod.matrix_rate(
            [
                line[:-1]
                for line in init_matrix
            ]
        )
        rateb = GaussMethod.free_matrix_members_rate(init_matrix)
        rate_inv_a = round(
            GaussMethod.matrix_rate(
                linalg.inv(
                    [
                        line[:-1]
                        for line in init_matrix
                    ]
                )
            ),
            4
        )
        rate_x = GaussMethod.solutions_rate(x)

        abs_err_b = 0.001
        abs_err_x = rate_inv_a * abs_err_b
        relative_err_x = round(abs_err_x / rate_x, 4)
        relative_err_b = round(abs_err_b / rateb, 4)

        print(
            "Absolute error: ",
            abs_err_x
        )
        print(
            "Relative error: ",
            relative_err_x,
            "<=",
            round(rate_a * rate_inv_a * relative_err_b, 4)
        )

    @staticmethod
    def solutions_rate(vector_x):
        max_x = 0
        for x in vector_x:
            max_x = max(max_x, x)
        return max_x

    @staticmethod
    def matrix_rate(matrix):
        s = 0
        for line in matrix:
            s = max(s, sum(map(abs, line)))
        return s

    @staticmethod
    def free_matrix_members_rate(matrix):
        maxb = 0
        b_position = len(matrix[0]) - 1

        for i in range(len(matrix)):
            maxb = max(maxb, matrix[i][b_position])

        return maxb


