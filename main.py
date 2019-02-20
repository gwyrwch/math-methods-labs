from Equation import *
from SIM import SIM
from GaussMethod import *
from SeidelMethod import SeidelMethod
from SquareRootMethod import SquareRootMethod


if __name__ == '__main__':
    f = open("input.txt")

    A = [
        list(map(float, line.split()))
        for line in f
    ]

    equation = Equation(A)
    SquareRootMethod.matrix_det([line[:-1] for line in equation.A])
    SquareRootMethod.find_inverse_matrix([line[:-1] for line in equation.A])
    SquareRootMethod.solve(equation)











