import  matplotlib.pyplot as plt
from random_walk import RandomWalk

# Построение случайного блуждания и нанесение точек на диаграмму.
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    # Назначение размера области просмотра.
    plt.figure(figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds,
                s=1)
    # Выделение первой и последней точек.
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', s=100)

    # Удаление осей.
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)


    plt.show()

    keep_running = input("Построить ещё (y/n): ")
    if keep_running == "n":
        break
