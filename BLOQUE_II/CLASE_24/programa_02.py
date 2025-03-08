import matplotlib.pyplot as plt
import numpy as np
#print(help(plt.show()))
#print(help(plt.subplots))
y = np.random.randn(100).cumsum()
fig, ax = plt.subplots()
fig, ax = plt.subplots(2, 2)
fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)
fig.set_size_inches(9, 9)
print(fig, ax)
ax[1,0].plot(y)
plt.show()