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

