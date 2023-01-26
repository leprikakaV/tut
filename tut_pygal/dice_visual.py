import pygal
from die import Die

# Создание двух кубиков D6
die1 = Die()
die2 = Die(10)

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
max_results = die1.num_sides + die2.num_sides

for value in range(2, max_results+1):
    frequence = results.count(value)
    frequencies.append(frequence)

hits = pygal.Bar()

hits.title = "Рез. 1000 бросков 2 кубиков D6"
hits.x_labels = [i for i in range(2, max_results+1)]
hits.x_title = "results"
hits.y_title = "frequence"


hits.add("D6+D10", frequencies)

hits.render_to_file("dice_visual.svg")
