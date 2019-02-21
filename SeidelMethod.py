from SIM import SIM
from OutputMethods import OutputMethods


class SeidelMethod:
    @staticmethod
    def solve(equation):
        SIM.convert_system(equation)
        OutputMethods.print_system(equation.A)
        SeidelMethod.do_iteration(equation, 0)
        cond = False
        k = 1
        while not cond:
            SeidelMethod.do_iteration(equation, k)
            cond = SeidelMethod.check_condition(equation, k)
            k += 1

    @staticmethod
    def do_iteration(equation, iter_num):
        print('iteration: ', iter_num)
        if not iter_num:
            for i in range(equation.n):
                equation.seidel_matrix.append([])
                equation.seidel_matrix[i].append(0)
            OutputMethods.print_matrix(equation.seidel_matrix)
            return

        for i in range(equation.n):
            res_x = 0
            for j in range(equation.n):
                res_x += equation.A[i][j] * equation.seidel_matrix[j][iter_num if j < i else iter_num - 1]

            equation.seidel_matrix[i].append(res_x + equation.A[i][equation.m])

        OutputMethods.print_matrix(equation.seidel_matrix)

    @staticmethod
    def check_condition(equation, iter_num):
        epsilon = 0.01
        x_cur = [line[iter_num] for line in equation.seidel_matrix]
        x_prev = [line[iter_num - 1] for line in equation.seidel_matrix]
        rate = 0
        for i in range(len(x_cur)):
            rate = max(rate, abs(x_cur[i] - x_prev[i]))

        rate = round(rate, 2)

        if rate - epsilon <= 10 ** -19:
            print('Condition: ', rate, '<=', epsilon, '\n')
            return True
        print('Condition: ', rate, '>', epsilon, '\n')
        return False




