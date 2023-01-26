from die import Die
import  pygal

# Создание кубика D6.
die = Die()

results = []
for foll_num in range(1000):
    result = die.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
for value in range(1, die.num_sides+1):
    frequence = results.count(value)
    frequencies.append(frequence)

# Визуализация результатов.
hist = pygal.Bar()

hist.title = "Результаты броска одного кубика D6 1000 раз"
hist.x_labels = [i for i in range(1, die.num_sides+1)]
hist.x_title = "Result"
hist.y_title = "Частота выпадания"

hist.add("D6", frequencies)
hist.render_to_file("die_visual.svg")