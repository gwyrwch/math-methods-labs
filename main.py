from Equation import *
from GaussMethod import *

if __name__ == '__main__':
    f = open("input.txt")

    A = [
        list(map(float, line.split()))
        for line in f
    ]

    matrix = [
        [j for j in i]
        for i in A
    ]

    matrix_copy = [
        [j for j in i]
        for i in matrix
    ]

    matrix = [line[:-1] for line in matrix]

    equation = Equation(A)

    GaussMethod.solve(equation)

    GaussMethod.errorEstimates(matrix_copy, equation.X)

    print("answer:")
    print(equation.X)
    print()

    for line in GaussMethod.inverseMatrix(matrix):
        print(line)



