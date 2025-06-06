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
# https://stackoverflow.com/questions/14762181/adding-a-y-axis-label-to-secondary-y-axis-in-matplotlib
# https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it

# imports
import matplotlib.pyplot as pt
import numpy as np

# define number of points in series
size = 1000
# define standard deviation
stdDev= 2
# define the mean
mean = 5

# Sample data
x = np.linspace(0,10, 1000)
data1 = equation = pow(x,3)
data2 = np.random.normal(mean, stdDev, size)

# Create figure and primary axes
fig, ax_main = pt.subplots()

# Create a parasite axes
ax_par = ax_main.twinx()

# Plot histograms
ax_main.hist(data2, bins=100, alpha=0.8, label='Histogram')
ax_par.plot(x, equation, c = 'r', label='Equation')

# Add labels and limits
ax_main.set_xlabel('X-Value')
ax_main.set_ylabel('Frequency for histogram')
ax_par.set_ylabel('Y-Values for Equation')

# Add legends
ax_main.legend()
ax_par.legend()

# save the plots as a .png
pt.savefig('Histogram & Equation.png')
# Display the plot
pt.show()