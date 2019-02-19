class GaussMethod:

    @staticmethod
    def solve(equation):
        eps = 10 ** -3

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

        for i in range(equation.m - 1, -1, -1):
            if i >= equation.n or abs(equation.A[i][i]) < eps:
                equation.X.append(0)
                continue

            sum = 0
            for k in range(equation.m - 1, i, -1):
                sum += equation.A[i][k] * equation.X[equation.m - 1 - k]
            x = round((equation.A[i][equation.m] - sum) / equation.A[i][i], 4)
            equation.X.append(x)

        equation.X.reverse()

        wrong = False
        for j in range(equation.n):
            sum = 0
            for i in range(equation.m):
                sum += equation.X[i] * equation.A[j][i]

            wrong = wrong or abs(sum - equation.A[j][equation.m]) > eps

        if wrong:
            print('No solution')
            return

    @staticmethod
    def inverseMatrix(matrix):
        eps = 10 ** -9
        m = len(matrix[0])

        for i in range(len(matrix)):
            for j in range(m):
                matrix[i] += [1] if i == j else [0]

        m = len(matrix[0])

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

        for i in range(len(matrix) - 1, -1, -1):
            divider = matrix[i][i]
            for j in range(m):
                if(abs(matrix[i][j]) > eps):
                    matrix[i][j] /= divider
            for j in range(i + 1, len(matrix)):
                factor = matrix[i][j]
                for k in range(0, m):
                    matrix[i][k] -= matrix[j][k] * factor

        m = len(matrix[0]) // 2
        matrix = [line[m:] for line in matrix]

        matrix = [[
                round(j, 4) for j in i
            ]
            for i in matrix
        ]

        return matrix

    @staticmethod
    def errorEstimates(initA, X):
        rateA = GaussMethod.matrixRate([line[:-1] for line in initA])
        rateb = GaussMethod.freeMatrixMembersRate(initA)
        rateInvA = round(GaussMethod.matrixRate(GaussMethod.inverseMatrix(initA)), 4)
        rateX = GaussMethod.solutionsRate(X)
        absErrB = 0.001

        absErrX = rateInvA * absErrB
        relativeErrX = round(absErrX / rateX, 4)

        relativeErrB = round(absErrB / rateb, 4)

        print("Absolute error: ", absErrX)
        print("Relative error: ", relativeErrX, "<=", round(rateA * rateInvA * relativeErrB, 4))

    @staticmethod
    def solutionsRate(vectorX):
        maxX = 0
        for x in vectorX:
            maxX = max(maxX, x)
        return maxX

    @staticmethod
    def matrixRate(matrix):
        s = 0
        for line in matrix:
            s = max(s, sum(map(abs, line)))
        return s

    @staticmethod
    def freeMatrixMembersRate(matrix):
        maxb = 0
        bPosition = len(matrix[0]) - 1
        for i in range(len(matrix)):
            maxb = max(maxb, matrix[i][bPosition])

        return maxb


