from matplotlib import pyplot as plt
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 81, 100, 67, 73, 77, 0]

"Notas agrupadas por decil"
'''Um decil é um termo estatístico usado para dividir um conjunto de dados ordenados em dez partes iguais.
 Cada parte representa 10% da distribuição dos dados.'''
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()],
        histogram.values(),
        10,
        edgecolor=(0, 0, 0))

plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()