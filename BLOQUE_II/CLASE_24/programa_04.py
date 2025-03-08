import matplotlib.pyplot as plt
import numpy as np

y1 = np.random.randn(100).cumsum()
y2 = np.random.randn(100).cumsum()
y3 = np.random.randn(100).cumsum()

fig = plt.figure()
fig.add_subplot(2, 3, 5)
plt.plot(y1, color = "green")
fig.add_subplot(2, 3, 1)
plt.plot(y2, color = "red")

plt.show()