import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
inner_ax= fig.add_axes([0.6, 0.6, 0.25, 0.25])
x1 = np.arange(10)
y1 = np.array([1, 4, 6, 3,6, 3,6,7,5, 7])
x2 = np.arange(10)
y2 = np.array([4, 3, 6, 2, 7, 2, 4, 7, 9, 6])
ax.plot(x1, y1)
inner_ax.plot(x2, y2)

# 展示图形
plt.show()