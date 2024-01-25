"""Os vetores são dados que são armazenados em listas em python, dados estes que podem ser utilizados
para realizar calculos aritmeticos, mas vale salientar que em python, as listas não são vetores.
Então, para isso é necessário construir essas ferramentas aritméticas"""

# não podemos somar vetores com tamanhos diferentes
from typing import List
from math import sqrt

Vector = List[float]

def add(v: Vector, w: Vector) -> Vector:
    "soma os elementos correspondentes"
    assert len(v) == len(w), "vectors must have same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtraction(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vestors must have same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(Vectors: List[Vector]) -> Vector:
    assert Vectors, "Vectors not provided"

    num_elements = len(Vectors[0])
    assert all(len(v) == num_elements for v in Vectors), "different sizes!"

    return [sum(vector[i] for vector in Vectors)
            for i in range(num_elements)]
assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]
assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))
assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w), "Vectors must have same length"
    return sum(v_i * w_i for v_i, w_i in zip(v, w)) 

assert dot([1, 2, 3], [4, 5, 6]) == 32 # 1 * 4 + 2 * 5 + 3 * 6


def sum_of_squares(v: Vector) -> float:
    # retorna v_1 * v_1 ... v_n * v_n
    return dot(v, v)


def magnitude(v: Vector) -> float:
    "Retorna a magnitude de v"
    return sqrt(sum_of_squares(v))

assert magnitude([3,4]) == 5

# a distancia entre dois vetores é definida por "V(v1 - w1)² + ... + (vn - wn)²"
# para calcular:

def squared_distance(v: Vector, w: Vector) -> float:
    # computa (v1 - w_1)²
    return sum_of_squares(subtraction(v, w))

def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtraction(v, w))