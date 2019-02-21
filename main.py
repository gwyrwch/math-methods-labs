from Equation import *
from SIM import SIM
from GaussMethod import *
from SeidelMethod import SeidelMethod
import sys

def seidel():
    print('Seidel method: ')
    SeidelMethod.solve(equation)
    SIM.get_answer(equation.seidel_matrix)

def sim():
    print('Method of simple iterations: ')
    SIM.solve(equation)
    SIM.get_answer(equation.x_matrix)


if __name__ == '__main__':
    f = open("input.txt")

    A = [
        list(map(float, line.split()))
        for line in f
    ]

    print('Initial system: ')
    SIM.print_system(A)

    equation = Equation(A)

    if sys.argv[2] == 'seidel':
        seidel()
    elif sys.argv[1] == 'sim':
        sim()
    else :
        print('wrong argument')











