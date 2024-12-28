import matplotlib.pyplot as plt

# Данные для визуализации
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание линейного графика
plt.plot(x, y, marker='o')
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()

# Сохранение графика в файл
plt.savefig('plot.png')

# Показ графика
plt.show()