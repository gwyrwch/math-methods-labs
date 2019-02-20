class Equation:
    def __init__(self, A):
         self.A = A
         self.n = len(A)
         self.m = len(A[0]) - 1
         self.X = []
         self.x_matrix = [[
                0 for j in range(self.n)
             ]
             for i in range(self.n)
         ]
         self.seidel_matrix = []

