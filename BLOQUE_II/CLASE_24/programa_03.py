import matplotlib.pyplot as plt
import numpy as np

y1 = np.random.randn(100).cumsum()
y2 = np.random.randn(100).cumsum()

fig = plt.figure()
ax1 = plt.axes()
ax1.plot(y1)

ax2 = plt.axes([0,0,0.5,0.5])
ax2.plot(y2, color = "orange")

plt.show()