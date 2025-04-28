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