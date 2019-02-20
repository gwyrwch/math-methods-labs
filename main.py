from Equation import *
from SIM import SIM
from GaussMethod import *
from SeidelMethod import SeidelMethod


if __name__ == '__main__':
    f = open("input.txt")

    A = [
        list(map(float, line.split()))
        for line in f
    ]

    equation = Equation(A)
    SIM.solve(equation)

    #SeidelMethod.solve(equation)
    #SIM.print_matrix(equation.seidel_matrix)







