users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                     (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# visando eficiencia, utilizar dicts é uma melhor opção do que uma lista de pares, por exemplo.
# É muito mais rápido pesquisar em dicts. Na lista teriamos que iterar sob cada par e procurar 
# o item que está sendo buscado. Então temos:

friendships = {user["id"]: [] for user in users}

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

def number_of_friends(user):
    user_id = user["id"]
    friends_ids = friendships[user_id]
    return len(friends_ids)

total_connections = sum(number_of_friends(user)
                        for user in users)

num_users = len(users)
avg_connectios = total_connections / num_users

num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],
    reverse=True
)

# ---------------------------------------------------------------------
# amigos de amigos para indicação

def foaf_ids_bad(user):
    return [foaf_id 
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]

# a função acima retorna uma lista com os amigos de amigos, independente se o id do amigo é repetido ou não. Ex:

# [0, 2, 3, 0, 1, 3] --> retorno se chamarmos o id 0  
# [1, 2]             --> id 0
# [0, 2, 3]          --> id 1
# [0, 1, 3]          --> id 2 

from collections import Counter

# retorna a quantidade de amigos em comum do id selecionado
# Counter({3: 2}) para o caso acima, indicando que 0 tem dois amigos em comum com 3. 1 e 2.
def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id 
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
    )

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), 
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

# encontra os ids dos usuarios com o mesmo interesse
def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

from collections import defaultdict

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

interest_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interest_by_user_id[user_id].append(interest)

# ----------------------------------------------------------------------------------------------------------------------------------------------- ABOVE -> FROM CHAP 1 -------------------------------------------------------------------------------------------------------------------------------------------------
from matplotlib import pyplot as plt
from random import randint
from typing import List

# cria uma lista de 100 numeros
n_of_friends = [randint(0, 100) for _ in range(100)]

friend_counts = Counter(n_of_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend COunts")
plt.xlabel("# of friends")
plt.ylabel("# of people")

largest_value = max(n_of_friends)
smallest_value = min(n_of_friends)
sorted_values = sorted(n_of_friends)
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

def _median_odd(xs: List[float]) -> float:
    return sorted(xs)[len(xs) // 2]

def _median_even(xs: List[float]) -> float:
    sorted_xs = sorted(xs)
    midpoint = len(sorted_xs) // 2
    return (sorted_xs[midpoint - 1] + sorted_xs[midpoint]) / 2

def median(v: List[float]) -> float:
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == 5.5

# A média é muito sensível a outliers
# Uma generalização da mediana é o quantil, um valor que separa uma determinada porcentagem dos dados ( a mediana separa 50% dos dados)

def quantile(xs: List[float], p: float) -> float:
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

# agora, para calcular a moda, isto é, os valores mais frequentes naquele conjunto:
def mode(xs: List[float]) -> List[float]:
    count = Counter(xs)
    max_count = max(count.values())
    return [x_i for x_i, counts in count.items()
            if counts == max_count]
""" A dispersão expressa a medida da distribuição de dados. Em geral, os valores próximos de zero 
indicam que os dados não estão espalhados e os valores maiores indicam que os valores estão espalhados"""

""" um exemplo é a amplitude (diferença entre o maior e menor número de um conjunto de dados)"""

def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)

"""Outra medida de dispersão mais complexa é a variância. A variância descreve o 
quão dispersos estão os números com relação à média. Em outras palavras, a variância indica o quanto os
valores em um conjunto estão afastados da média. Uma variância alta sugere que os valores estão
mais dispersos em torno da média, enquanto uma variância baixa indica que os valores estão mais 
concentrados próximos à média."""

from scratch.linear_algebra import sum_of_squares, dot

def de_mean(xs: List[float]) -> List[float]:
    """traduza xs subtraindo sua média(para que o resultado tenha média 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float:
    """ Quase o desvio quadrado médio da média"""
    assert len(xs) >= 2, "variance requires at least two elements"
    n = len(xs)
    deviations = de_mean(xs)
    return sum_of_squares(deviations) / (n - 1)

"""A importância do desvio padrão reside no fato de que ele ajuda a entender a consistência ou a 
variabilidade dos dados. Um desvio padrão baixo indica que os valores tendem a estar próximos 
da média, enquanto um desvio padrão alto indica uma maior dispersão dos valores em relação à média."""

import math

def standard_deviation(xs: List[float]) -> float:
    # O desvio padrão é a raiz quadrada da variância
    return math.sqrt(variance(xs))

"""O mesmo problema da média com os outliers atinge a amplitude, assim como o desvio padrão. Para isso
uma alternativa mais eficiente computa a diferença entre valor do 75o percentil e o valor do 25o percentil"""

"""O cálculo do interquartile range (IQR), que é a diferença entre o terceiro quartil (Q3) e o primeiro quartil (Q1), 
é menos sensível a outliers do que o desvio padrão, Isso ocorre porque o IQR se baseia nos valores que compõem os 50%
 centrais dos dados, ignorando os extremos."""

def interquartile_range(xs: List[float]) -> float:
    return quantile(xs, 0.75) - quantile(xs, 0.25)

"""a covariância é um tipo de variância aplicada a pares. Enquanto a variância mede o desvio de uma variável da média
a covariância mede a variação simultânea de duas variáveis em relação às suas médias"""
def covariance(xs: List[float],ys: List[float]) -> float:
    assert len(xs) == len(ys), "xs and ys must have same length"

    return dot(de_mean(xs), de_mean(ys) / len(xs)- 1)