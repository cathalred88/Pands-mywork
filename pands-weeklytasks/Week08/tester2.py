import matplotlib.pyplot as plt
import numpy as np

line = [0.2, 0.3, 0.37, 0.4, 0.6, 0.7, 0.72, 0.75, 0.77, 0.78, 0.79, 0.795]
distribution = [0.2, 0.3, 0.3, 0.4, 0.7, 0.7, 0.7, 0.8]

fig, ax = plt.subplots(1, 1)

ax2 = ax.twinx()
ax3 = ax2.twiny()

ax.plot(line)
ax.set_xlabel('line xaxis')
ax.set_ylabel('line yaxis')

ax3.hist(distribution, orientation='horizontal', alpha=.5)
ax3.invert_xaxis()
ax3.set_xlabel('hist xaxis, note where 0 is')
# note this needs to be ax2 due to subtle overlay issues....
ax2.set_ylabel('hist yaxis')
plt.draw()
plt.show()
