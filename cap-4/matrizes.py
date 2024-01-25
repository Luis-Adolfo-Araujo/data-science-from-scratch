from vetores import Vector
from typing import List, Tuple, Callable

Matrix = List[List[float]]

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [5, 6]]

def shape(A: Matrix) -> Tuple[int, int]:
    """retorna numero de linhas de A, e o numero de colunas de A"""
    num_rows = len(A)
    num_columns = len(A[0]) if A else 0 # Numero de elementos na primeira linha
    return num_rows, num_columns

""" Para uma matriz n x k, podemos considerar cada linha da matriz n x k como um
 vetor de comprimento k e cada coluna como um vetor de comprimento n """

def get_row(A: Matrix, i: int) -> Vector:
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    return [A_i[j]
            for A_i in A]

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]

def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i, j: 1 if i==j else 0)

assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]