# wk08Part1.py
# script space for testing code in Lab from week 08
# Author Cathal Redmond 27 Mar 2025 

import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints #multiply each entry by itself
plt.plot(xpoints, ypoints)
plt.show()

