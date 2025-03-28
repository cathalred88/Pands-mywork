# wk08Part1.py
# script space for testing code in Lab from week 08
# Author Cathal Redmond 27 Mar 2025 

import numpy as np
import matplotlib.pyplot as plt
# it is a good idea to have your absolute values set into variables at the beginning of your program
minSalary= 20000
maxSalary = 80000
low = 21
high = 65
numberOfEntries = 100
size = numberOfEntries

np.random.seed(1)

salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
ages = np.random.randint(low, high, size)
#salariesPlus = salaries + 5000 # this will add 5000 to the salaries. 
#salariesMult = salaries * 1.05 # adding 5% to each salary. 
#print (salariesMult)

#newSalaries = salariesMult.astype(int)
#print(newSalaries)

plt.scatter(ages, salaries, label = "Salaries") #this will be random

# add x squared line
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints # multiply each entry by itself

plt.plot(xpoints, ypoints, color = 'r', label = "x squared")

plt.title("Random Plot")
plt.xlabel("Salaries")
plt.ylabel("Age")
plt.legend()
#plt.show() # see how axis have changed

plt.savefig('prettier-plot.png')