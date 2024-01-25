'''Um gráfico de barras é uma boa opção para mostrar como algumas quantidades variam em um 
conjunto discreto de itens. Por exemplo o número de Oscars recebidos pelos filmes indicados'''

from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

plt.bar(range(len(movies)), num_oscars)

plt.title("My Favorite Movies")
plt.ylabel("# of Academy Awards")

plt.xticks(range(len(movies)), movies)
plt.show()