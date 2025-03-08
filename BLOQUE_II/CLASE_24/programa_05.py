import matplotlib.pyplot as plt
import numpy as np

x = range(100, 200)
y = np.random.randn(100).cumsum()

xtick_label = ["Perú", "Argentina", "Brazil", "Chile", "Colombia", "Paraguay"]
xtick_label = ["2010", "2011", "2012", "2013", "2014", "2015"]

fig, ax = plt.subplots()
plt.plot(x, y)
plt.title("Ventas 2025", fontsize = 20, color = "orange")
plt.xlabel("Años", color = "red")
plt.ylabel("Dolares", color = "green")
#plt.xticks(range(120, 180, 10))
#plt.xticks(range(50, 170, 20), xtick_label)
plt.xticks(range(120, 180, 10), xtick_label)
#plt.yticks(range(120, 180, 10))

plt.show()