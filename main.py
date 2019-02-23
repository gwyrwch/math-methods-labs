from RotationMethod import RotationMethod


if __name__ == '__main__':
    f = open("input.txt")

    matrix = [
        list(map(float, line.split()))
        for line in f
    ]

    RotationMethod.find_eigenvalue(matrix)











