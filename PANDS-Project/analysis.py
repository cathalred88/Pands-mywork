# analysis.py
# This script will take the Iris dataset and analyse it for the Programming and Scripting module project. 
# Author Cathal Redmond 14 April 2025. 

## References
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
# https://www.statology.org/pandas-scatter-plot-multiple-columns/
# https://www.geeksforgeeks.org/get-unique-values-from-a-column-in-pandas-dataframe/



## Project plan / Design intent 
# I have started this project late as i was busy with work first, then i was away on holiday with no access to my laptop, so i now have 4 weeks to complete this project. 
# I will manage this project timeline in the Burn-down approach, where my submission date is the endpoint and i need to allot my time backwards from there to achieve the program fucntionality. 
# I intend to have the main program functionally complete by the end of week 2, which allows for a week of clean up / improvements, and a week of overshoot mitigation. 
# This approach should peform 2 main objectives: primary goal to set a SMART goal in which i am timebound to copmlete the project by a certain date (* deadlines help my ADHD brain), and secondly to allow for the inevetable delays and interruptions that are a frequent feaure of my life!

## Import libraries & Functions
#import numpy as np
#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
import matplotlib.patches as mpatches

## Definitions of variables
path = "../PANDS-Project/"
FILENAME ="iris.txt"

## Subroutine definitions

#def readDict():
    # this will throw an error if the file does not exist
    # it should readly just return an empty dict
    # we can do this later
    #with open(FILENAME) as f:
        #return json.load(f)

## Main Program
df = pd.read_fwf(FILENAME, indexcol = 0, delimiter =',', names=["Sepal Length","Sepal Width","Petal Length","Petal Width","Species"])
pd.options.display.max_rows = 150
#print(df)
#print(df.groupby('Species').describe())

#Get Description of dataset using Describe function
describe = df.groupby('Species').describe()
print (describe)

#Detect unique values in Column and assign those values to a set which will then be used for grouping in the plots. 
uniqueSpecies = df['Species'].unique()
print(uniqueSpecies)

# define plot parameters
colors = ['r','g','b','y', ]
df["color"] = df.apply(lambda x: colors[x["group"]], axis=1)
ax1=df.plot(kind = 'scatter', x = 'Sepal Length', y = 'Sepal Width', marker = '.', c=df["color"], label = 'Sepal')
ax2=df.plot(kind = 'scatter', x = 'Petal Length', y = 'Petal Width', marker = ',', label = 'Petal', ax = ax1, legend =True)

# define plot labels
ax1.set_xlabel('Length')
ax1.set_ylabel('Width')
# command to show plot 
pt.show()


# Display Correlation between variables. 
print (df.corr(numeric_only=True))
