from RotationMethod import RotationMethod
from PrintMethods import PrintMethods

if __name__ == '__main__':
    f = open('input.txt')

    matrix = [
        list(map(float, line.split()))
        for line in f
    ]

    RotationMethod.check_with_numpy(matrix)
    RotationMethod.find_eigenvalue(matrix)












