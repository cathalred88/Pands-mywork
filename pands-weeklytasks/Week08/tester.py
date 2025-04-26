import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(5,3))
ax = fig.add_subplot(111)
ax2 = ax.twinx()

x = np.random.rand(10)
y = np.random.rand(10)
y2 = np.random.randint(1,10000, size=10)

l1 = ax.scatter(x,y, c="b", label="lin")
l2 = ax2.scatter(x,y2,  c="r", label="log")

ax2.set_yscale("log")
ax2.legend(handles=[l1, l2])

ax.set_ylabel("Linear axis")
ax2.set_ylabel("Logarithmic axis")
plt.tight_layout()

plt.show()