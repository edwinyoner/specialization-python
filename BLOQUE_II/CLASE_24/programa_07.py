import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
from pyparsing import alphas

y = np.random.randn(100).cumsum()

xtick_label = ["2010", "2011", "2012", "2013", "2014", "2015"]
plt.style.use('dark_background')
fig, ax = plt.subplots()
plt.plot(y, label = "Consumo")
plt.legend()
#Eje X
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(2))
ax.grid(which = "major", axis = "x", color = "SteelBlue")
ax.grid(which = "minor", axis = "x", color = "orange", alpha = 0.5)

#Eje Y
ax.yaxis.set_major_locator(MultipleLocator(2))
ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.grid(which = "major", axis = "y", color = "red")
ax.grid(which = "minor", axis = "y", color = "green", alpha = 0.5)

plt.show()