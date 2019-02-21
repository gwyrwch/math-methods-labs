from Equation import *
from GaussMethod import GaussMethod
from OutputMethods import OutputMethods


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

    print('Initial system: ')
    OutputMethods.print_system(equation.A)

    GaussMethod.solve(equation)
    print("\nAnswer:")
    print(equation.X, end='\n\n')

    inverse_matrix = GaussMethod.inverse_matrix(matrix)
    print("Inverse matrix: ")
    for line in inverse_matrix:
        print(line)

    print()
    GaussMethod.error_estimates(matrix_copy, equation.X)




