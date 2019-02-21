class Equation:
    def __init__(self, A):
        self.A = A
        self.n = len(A)
        self.m = len(A[0]) - 1
        self.X = []
