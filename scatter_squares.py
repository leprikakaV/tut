import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens,
            s=10, edgecolors='none')

x_values_cub = list(range(1, 1001))
y_values_cub = [x**3 for x in x_values_cub]
plt.scatter(x_values_cub, y_values_cub, c=y_values_cub, cmap=plt.cm.Reds,
            s=10, edgecolors='none')

# Назначение заголовка диаграммы и меток осей.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Назначение диапазона для каждой оси.
# plt.axis([0, 1100, 0, 1100000])

# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', which="major", labelsize=14)
plt.show()
# plt.savefig('squares_plot.png', bbox_inches="tight")