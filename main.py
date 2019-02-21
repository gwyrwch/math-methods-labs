from Equation import *
from GaussMethod import GaussMethod
from OutputMethods import OutputMethods
import sys


def gauss():
    print('Gaussian elimination method. Initial system: ')
    OutputMethods.print_system(equation.A)

    GaussMethod.solve(equation)
    print(
        "\nAnswer:",
        equation.X,
        end='\n\n'
    )

    print('Error estimates. ')
    GaussMethod.error_estimates(matrix_copy, equation.X)


def inverse_matrix():
    print("Inverse matrix. ")
    OutputMethods.print_matrix(
        GaussMethod.inverse_matrix(matrix)
    )


if __name__ == '__main__':
    f = open("input.txt")

    A = [
        list(map(float, line.split()))
        for line in f
    ]

    matrix_copy = [
        [j for j in i]
        for i in A
    ]

    matrix = [line[:-1] for line in A]

    equation = Equation(A)

    if sys.argv[1] == 'gauss':
        gauss()
    elif sys.argv[1] == 'inverse_matrix':
        inverse_matrix()
    else:
        print('wrong args')








