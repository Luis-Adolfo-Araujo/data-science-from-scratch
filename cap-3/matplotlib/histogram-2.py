from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")

# se não fizer isso, o matplotlib rotulará o eixo x como 0, 1
# e adicionará um +2.013e3 off no canto
plt.ticklabel_format(useOffset=False)

#o eixo y mostra apenas a parte acima de 500
plt.axis([2016.5, 2018.5, 499, 506])
#                        start, end
plt.title("Look at the 'Huge' Increase!")
plt.show()