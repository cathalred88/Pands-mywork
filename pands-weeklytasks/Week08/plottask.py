#plottask.py
# script for plotting histograms and a funstion on same axis 
# Author Cathal Redmond 26 Apr 2025
'''
Instructions: 
Write a program called plottask.py that displays:

a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range 0 to 10, 
on the one set of axes.
Some marks will be given for making the plot look nice (legend etc).

Please put a copy of the image of the plot (.png file) into the repository
'''
#References
# https://www.w3schools.com/python/ref_func_pow.asp

# imports
import matplotlib.pyplot as pt
import numpy as np


# define number of points in series
size = 1000
# define standard deviation
stdDev= 2
# define the mean
mean = 5

#formula for calculating the points we will use for histogram 
values = np.random.normal(mean, stdDev, size)
print(values)

#formula for creating a histogram from the standard deviation points
hist = pt.hist(values, 100)

# script for creating the plot for equation y(x)=x3  ## substutiting Y for H
x = np.linspace(0,10, 1000)
equation = pow(x,3)

# script for defining the plot Contents & Area formatting
fig = pt.figure(figsize=(5,3))
ax = fig.add_subplot(111)
ax2 = ax.twinx()

l1 = ax.hist(x, 100 , label="frequency")
l2 = ax2.plot(x,equation, c='r')

ax2.set_yscale("log")
ax2.legend(handles=[l1,l2])

ax.set_ylabel("Linear axis")
ax2.set_ylabel("Logarithmic axis")
pt.show()
