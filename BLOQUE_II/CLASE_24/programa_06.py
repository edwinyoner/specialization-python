import matplotlib.pyplot as plt
import numpy as np

y = np.random.randn(100).cumsum()

xtick_label = ["2010", "2011", "2012", "2013", "2014", "2015"]

fig, ax = plt.subplots()
plt.plot(y)
#plt.grid(color = "orange")
plt.grid(color = "orange",
         linewidth = 1.5,
         alpha = 0.5,
         linestyle  = 'dotted')

plt.show()