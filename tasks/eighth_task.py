import sys
import numpy as np
from munkres import Munkres, print_matrix

matrix = [[5, 9, 1, 10],
          [10, 3, 2, 4],
          [8, 7, 4, 5],
          [6, 17, 2, 5]]

print_matrix(matrix)
cost_matrix = []
for row in matrix:
    cost_row = []
    for col in row:
        cost_row += [sys.maxsize - col]
    cost_matrix += [cost_row]

m = Munkres()
indexes = m.compute(cost_matrix)
print('\nЛучшие пары и их значения:')
total = 0
for row, column in indexes:
    value = matrix[row][column]
    total += value
    print(f'({row}, {column}) -> {value}')


class HungarianAlg(object):

    def __init__(self, cost_matrix):
        self.O = cost_matrix
        self.C = cost_matrix.copy()
        self.n, self.m = self.C.shape
        self.row_covered = np.zeros(self.n, dtype=bool)
        self.col_covered = np.zeros(self.m, dtype=bool)
        self.marked = np.zeros((self.n, self.m), dtype=int)

    def _clear_covers(self):
        self.row_covered[:] = False
        self.col_covered[:] = False

    def _clear_marks(self):
        self.marked[:,:] = 0

    def solve(self):
        initial_step = _step0
        if(self.n==self.m):
            initial_step = _step1

        step = initial_step

        while type(step) is not tuple:
            step = step(self)

        if(step[0]):
            self.solution = step[2]
            self.max_cost = step[1]
        return step[0]

    def print_results(self):
        if self.solution == None:
            raise Exception("Решение не найдено")
        for k,v in self.solution.items():
            print("Для {} лучшая пара {}".format(v,k))
        print("Итоговая сумма {}".format(self.max_cost))

def _step0(state):
    #делаем матрицу квадратной
    matrix_size = max(state.n, state.m)
    pad_columns = matrix_size - state.n
    pad_rows = matrix_size - state.m
    state.C = np.pad(state.C, ((0,pad_columns),(0,pad_rows)), 'constant', constant_values=(0))

    state.row_covered = np.zeros(state.C.shape[0], dtype=bool)
    state.col_covered = np.zeros(state.C.shape[1], dtype=bool)
    state.marked = np.zeros((state.C.shape[0], state.C.shape[1]), dtype=int)
    return _step1

def _step1(state):
    #Максимальное значение по столбцам
    state.C = state.C - np.max(state.C,axis=1)[:,np.newaxis]
    return _step2

def _step2(state):
    #Максимальное значение по строкам
    state.C = state.C - np.max(state.C,axis=0)[np.newaxis,:]
    return _step3

def _step3(state):
    '''
    This step tries to find a coverage of all zeroes in the matrix using the minimum amount of row/column covers.
    It then uses this coverage to check for a solution. If one is found, the algorithm stops. Otherwise, it goes to step 4 and back to step 3.
    '''
    row_marked = np.zeros(state.C.shape[0], dtype=bool)
    col_marked = np.zeros(state.C.shape[1], dtype=bool)

    for j in range(state.C.shape[1]):
        for i in range(state.C.shape[0]):
            if(not state.row_covered[i] and not state.col_covered[j] and state.C[i][j]==0):
                state.marked[i][j] = 1
                state.row_covered[i] = True
                state.col_covered[j] = True

    state._clear_covers()

    for i in range(state.C.shape[0]):
        if np.sum(state.marked[i,:])==0:
            row_marked[i] = True
            for j in range(state.C.shape[1]):
                if not col_marked[j] and state.C[i][j] ==0:
                    col_marked[j] = True
                    for k in range(state.C.shape[0]):
                        if not row_marked[k] and state.marked[k][j]==1:
                            row_marked[k]=True

    state.row_covered = np.logical_not(row_marked)
    state.col_covered = col_marked
    num_lines = np.sum(state.row_covered) + np.sum(state.col_covered)

    if num_lines == state.C.shape[0]:
        sol = _check_for_solution(state)
        return sol
    else:
        return _step4

def _step4(state):
    # Если решения на этом шаге нет, то матрица была неверной
    biggest_uncovered = -np.inf
    for i in range(state.C.shape[0]):
        for j in range(state.C.shape[1]):
            if not state.row_covered[i] and \
                    not state.col_covered[j] and \
                    state.C[i][j] > biggest_uncovered:
                biggest_uncovered = state.C[i][j]

    for i in range(state.C.shape[0]):
        for j in range(state.C.shape[1]):
            if not state.row_covered[i] and not state.col_covered[j]:
                state.C[i][j] -= biggest_uncovered
            elif state.row_covered[i] and state.col_covered[j]:
                state.C[i][j] += biggest_uncovered

    state._clear_covers()
    state._clear_marks()
    return _step3

def _check_for_solution(state):
    for j in range(state.C.shape[1]):
        for i in range(state.C.shape[0]):
            if(not state.row_covered[i] and not state.col_covered[j] and state.C[i][j]==0):
                state.marked[i][j] = 1
                state.row_covered[i] = True
                state.col_covered[j] = True
    sol = {}
    cost = 0
    for i in range(state.n):
        for j in range(state.m):
            if(state.marked[i][j]==1):
                sol[j] = i
                cost = cost + state.O[i][j]

    state._clear_covers()

    return len(sol)==state.m, cost, sol

alg = HungarianAlg(np.asarray([[82,83,69,92],[77,37,49,92],[11,69,5,86],[8,9,98,23]]))
alg.solve()
alg.print_results()