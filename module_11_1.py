import matplotlib.pyplot as plt

x = [1, 4, 7, 13, 16]
y = [10, 8, 13, 17, 12]
plt.plot(x, y, marker='o', color='blue')
plt.title("Линейный график")
plt.xlabel("X-ось")
plt.ylabel("Y-ось")
plt.show()

data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.hist(data, bins=5, color='green', alpha=0.7)
plt.title("Гистограмма")
plt.xlabel("Значения")
plt.ylabel("Частота")
plt.show()

sizes = [50, 40, 10]
labels = ['Apple', 'Samsung', 'OPPO']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Круговая диаграмма")
plt.show()

