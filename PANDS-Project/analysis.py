# analysis.py
# This script will take the Iris dataset and analyse it for the Programming and Scripting module project. 
# Author Cathal Redmond 14 April 2025. 

## References
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
# https://www.statology.org/pandas-scatter-plot-multiple-columns/
# https://www.geeksforgeeks.org/get-unique-values-from-a-column-in-pandas-dataframe/
# https://www.w3schools.com/python/matplotlib_scatter.asp
# https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it
# https://python-graph-gallery.com/scatterplot-with-regression-fit-in-matplotlib/
# https://www.geeksforgeeks.org/how-to-select-single-column-of-a-pandas-dataframe/
# https://stackoverflow.com/questions/40892300/set-y-axis-scale-for-pandas-dataframe-boxplot-3-deviations
# 





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
#import scipy.stats as st


## Definitions of variables
path = "../PANDS-Project/"
FILENAME ="iris.data"
FILENAMEOUTPUT = "Summary.txt"

## Subroutine definitions

'''
#Read if output file is present
FILENAME = "Summary.txt"
def readSummary():
    try:
        with open(FILENAME) as f:
            summary = int(f.read())
            return summary
    except IOError:
        # this file will be created when we write back.
        # no file assumes first time running
        # ie no summary performed before this execution
        print ("Summary.txt file does not exist, it will be be created now")
        return null

def writeSummary(summary):
    with open(FILENAME, "wt") as f:
    # write takes a string so we need to convert
        f.write(str(summary))

'''




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
describe = df.groupby('Species').describe(include = 'all')
pd.set_option('display.max_columns', None)
#print (describe)

#Detect unique values in Column and assign those values to a set which will then be used for grouping in the plots. 
uniqueSpecies = df['Species'].unique()
#print(uniqueSpecies)

# split the dataframe into smaller dataframes by column value (species type)
df1 = df[df['Species'] == uniqueSpecies[0]] #Setosa
df2 = df[df['Species'] == uniqueSpecies[1]] #Versicolor
df3 = df[df['Species'] == uniqueSpecies[2]] #Virginicia
#print (df1)
#print (df2)
#print (df3)

'''
#Scatterplot
# define plot parameters - 
# come back to this because i should be able to run this in a for loop to select the different species names automatically from Unique Species array. 
colors = ['r','g','b','y', ]
ax1=df1.plot(kind = 'scatter', x = 'Sepal Length', y = 'Sepal Width', marker = '.', c = 'red' , label = 'Setosa Sepal')
ax2=df1.plot(kind = 'scatter', x = 'Petal Length', y = 'Petal Width', marker = 'x', c = 'magenta', label = 'Setosa Petal', ax = ax1)
ax3=df2.plot(kind = 'scatter', x = 'Sepal Length', y = 'Sepal Width', marker = '.', c = 'blue' , label = 'Versicolor Sepal',ax = ax1)
ax4=df2.plot(kind = 'scatter', x = 'Petal Length', y = 'Petal Width', marker = 'x', c = 'cyan', label = 'Versicolor Petal', ax = ax1)
ax5=df3.plot(kind = 'scatter', x = 'Sepal Length', y = 'Sepal Width', marker = '.', c = 'yellow' , label = 'Virginica Sepal',ax = ax1)
ax6=df3.plot(kind = 'scatter', x = 'Petal Length', y = 'Petal Width', marker = 'x', c = 'orange', label = 'Virginica Petal', ax = ax1, legend =True)

#calculate the straight line best fits for each dataset pair
b1, a1 = np.polyfit(df1['Sepal Length'], df1['Sepal Width'], deg=1)
b2, a2 = np.polyfit(df1['Petal Length'], df1['Petal Width'], deg=1)
b3, a3 = np.polyfit(df2['Sepal Length'], df2['Sepal Width'], deg=1)
b4, a4 = np.polyfit(df2['Petal Length'], df2['Petal Width'], deg=1)
b5, a5 = np.polyfit(df3['Sepal Length'], df3['Sepal Width'], deg=1)
b6, a6 = np.polyfit(df3['Petal Length'], df3['Petal Width'], deg=1)
# set upper and lower limits for lines to start and finish at 
xseq1 = np.linspace(min(df1['Sepal Length']), max(df1['Sepal Length']), num=100)
xseq2 = np.linspace(min(df1['Petal Length']), max(df1['Petal Length']), num=100)
xseq3 = np.linspace(min(df2['Sepal Length']), max(df2['Sepal Length']), num=100)
xseq4 = np.linspace(min(df2['Petal Length']), max(df2['Petal Length']), num=100)
xseq5 = np.linspace(min(df3['Sepal Length']), max(df3['Sepal Length']), num=100)
xseq6 = np.linspace(min(df3['Petal Length']), max(df3['Petal Length']), num=100)

#print a & b pairs for each pair
print(b1,a1)
print(b2,a2)
print(b3,a3)
print(b4,a4)
print(b5,a5)
print(b6,a6)

# add straight line regression lines to each scatterplot pair
ax22=pt.plot(xseq1, a1 + b1 * xseq1, c = 'red', label = 'Setosa Sepal')
ax23=pt.plot(xseq2, a2 + b2 * xseq2, c = 'magenta', label = 'Setosa Petal')
ax24=pt.plot(xseq3, a3 + b3 * xseq3, c = 'blue' , label = 'Versicolor Sepal')
ax25=pt.plot(xseq4, a4 + b4 * xseq4, c = 'cyan', label = 'Versicolor Petal')
ax26=pt.plot(xseq5, a5 + b5 * xseq5, c = 'yellow' , label = 'Virginica Sepal')
ax27=pt.plot(xseq6, a6 + b6 * xseq6, c = 'orange', label = 'Virginica Petal')

# define plot labels
ax1.set_xlabel('Length')
ax1.set_ylabel('Width')
# command to show plot 

#pt.savefig('scatterplotsummary.png')
#pt.show()


# Display Correlation between variables. 
print (df.corr(numeric_only=True))


# Histograms for Petal and Sepal length each species
ax7 = df1.plot(kind = 'hist', title ='Histogram of Setosa Measurments', xlabel = 'Length (cm)', ylabel = 'Frequency')
ax8 = df2.plot(kind = 'hist', title ='Histogram of Versicolor Measurments', xlabel = 'Length (cm)', ylabel = 'Frequency')
ax9 = df3.plot(kind = 'hist', title ='Histogram of Virginicia Measurments', xlabel = 'Length (cm)', ylabel = 'Frequency')

pt.savefig('histogramSetosa.png')
#pt.show()


# Now i want to slice the historams the other way, showing 1 variable: (length of petal etc) for each species for comparison
# Histogram for petal length: 
ax10 = df1.plot(kind = 'hist', label = 'Iris-Setosa', column =["Petal Length","Species"], title = 'Petal lengths for each species', xlabel = 'Petal length in cm', ylabel = 'Frequency',edgecolor = "black")
ax11 = df2.plot(kind = 'hist', label = 'Iris-Versicolor', column =["Petal Length","Species"], xlabel = 'Petal length in cm', ylabel = 'Frequency',edgecolor = "black", ax = ax10)
ax12 = df3.plot(kind = 'hist', label = 'Iris-Virginica', column =["Petal Length","Species"], xlabel = 'Petal length in cm', ylabel = 'Frequency', edgecolor = "black", ax = ax10)
labels = "Iris-Setosa", "Iris-Versicolor", "Iris-Virginica"
pt.legend(labels)
pt.savefig('HistogramPetalLenght.png')
#pt.show()

# Histogram for petal width:
ax13 = df1.plot(kind = 'hist', label = 'Iris-Setosa', column =["Petal Width","Species"], title = 'Petal widths for each species', xlabel = 'Petal width in cm', ylabel = 'Frequency',edgecolor = "black")
ax14 = df2.plot(kind = 'hist', label = 'Iris-Versicolor', column =["Petal Width","Species"], xlabel = 'Petal width in cm', ylabel = 'Frequency',edgecolor = "black", ax = ax13)
ax15 = df3.plot(kind = 'hist', label = 'Iris-Virginica', column =["Petal Width","Species"], xlabel = 'Petal width in cm', ylabel = 'Frequency', edgecolor = "black", ax = ax13)
pt.legend(labels)
pt.savefig('HistogramPetalWidth.png')
#pt.show()

# Histogram for sepal length:
ax16 = df1.plot(kind = 'hist', label = 'Iris-Setosa', column =["Sepal Length","Species"], title = 'Sepal lengths for each species', xlabel = 'Sepal length in cm', ylabel = 'Frequency',edgecolor = "black")
ax17 = df2.plot(kind = 'hist', label = 'Iris-Versicolor', column =["Sepal Length","Species"], xlabel = 'Sepal length in cm', ylabel = 'Frequency',edgecolor = "black", ax = ax16)
ax18 = df3.plot(kind = 'hist', label = 'Iris-Virginica', column =["Sepal Length","Species"], xlabel = 'Sepal length in cm', ylabel = 'Frequency', edgecolor = "black", ax = ax16)
pt.legend(labels)
pt.savefig('HistogramSepalLenght.png')
#pt.show()

# Histogram for sepal width:
ax19 = df1.plot(kind = 'hist', label = 'Iris-Setosa', column =["Sepal Width","Species"], title = 'Sepal Widths for each species', xlabel = 'Sepal Width in cm', ylabel = 'Frequency',edgecolor = "black")
ax20 = df2.plot(kind = 'hist', label = 'Iris-Versicolor', column =["Sepal Width","Species"], xlabel = 'Sepal Width in cm', ylabel = 'Frequency',edgecolor = "black", ax = ax19)
ax21 = df3.plot(kind = 'hist', label = 'Iris-Virginica', column =["Sepal Width","Species"], xlabel = 'Sepal Width in cm', ylabel = 'Frequency', edgecolor = "black", ax = ax19)
pt.legend(labels)
pt.savefig('HistogramSepalWidth.png')
#pt.show()
'''


# Boxplots - show a variable's mean & spread for each species, makes for easy visual comparisons 
# I will display these as a 2x2 subplot to make visualising these easier. 
# Boxplot for Sepal Width
fig, axes = pt.subplots(nrows=1, ncols=4, sharex = True, sharey = True)

ax22 = df1.plot(kind = 'box', column = ["Sepal Width"], positions = [1] ,title = 'Sepal Widths', xlabel= 'Setosa', ylabel = 'Sepal Width in cm', patch_artist=True, color = 'red', ax=axes[0] )
ax23 = df2.plot(kind = 'box', column = ["Sepal Width"], positions = [2] , xlabel= 'Versicolor', patch_artist=True, color = 'green', ax = ax22)
ax24 = df3.plot(kind = 'box', column = ["Sepal Width"], positions = [3] , xlabel= 'Virginica', patch_artist=True, color = 'blue', ax = ax22 )
ax22.set_ylim(0.0, 8.0)

# Boxplot for Petal Width
ax25 = df1.plot(kind = 'box', column = ["Petal Width"], positions = [1] ,title = 'Petal Widths', xlabel= 'Setosa', ylabel = 'Petal Width in cm', patch_artist=True, color = 'red',ax=axes[1] )
ax26 = df2.plot(kind = 'box', column = ["Petal Width"], positions = [2] , xlabel= 'Versicolor', patch_artist=True, color = 'green', ax = ax25)
ax27 = df3.plot(kind = 'box', column = ["Petal Width"], positions = [3] , xlabel= 'Virginica', patch_artist=True, color = 'blue', ax = ax25 )
ax25.set_ylim(0.0, 8.0)

# Boxplot for Sepal Length
ax28 = df1.plot(kind = 'box', column = ["Sepal Length"], positions = [1] , title = 'Sepal Length', ylabel = 'Sepal Length in cm', patch_artist=True, color = 'red', ax=axes[2] )
ax29 = df2.plot(kind = 'box', column = ["Sepal Length"], positions = [2] , patch_artist=True, color = 'green', ax = ax28)
ax30 = df3.plot(kind = 'box', column = ["Sepal Length"], positions = [3] , patch_artist=True, color = 'blue', ax = ax28)
ax28.set_ylim(0.0, 8.0)

# Boxplot for Petal Length
ax31 = df1.plot(kind = 'box', column = ["Petal Length"], positions = [1] , title = 'Petal Length', xlabel= 'Setosa', ylabel = 'Petal Length in cm', patch_artist=True, color = 'red', ax=axes[3] )
ax32 = df2.plot(kind = 'box', column = ["Petal Length"], positions = [2] , xlabel= 'Versicolor', patch_artist=True, color = 'green', ax = ax31)
ax33 = df3.plot(kind = 'box', column = ["Petal Length"], positions = [3] , xlabel= 'Virginica', patch_artist=True, color = 'blue', ax = ax31)
ax31.set_ylim(0.0, 8.0)
pt.xticks(rotation=90)


#handles, labels = ax22.get_legend_handles_labels()
#fig.legend(handles, labels, loc='upper center')
boxplotLabels = ['Setosa','Versicolor','Virginca']
fig.legend(labels=boxplotLabels, loc = 'upper left')
fig.set_size_inches(18.5, 10.5)

pt.savefig('SubplotBoxplots.png')
pt.show()

# Subplot definition
'''
fig, axes = pt.subplots(nrows=2, ncols=2,)

axes[0, 0].
axes[0, 1].
axes[1, 0].
axes[1, 1].
'''







# Perform a 2-sample t test on the variables
#st.ttest_ind(a=df1("Petal Length"), b=df2("Petal Length"), equal_var=True)


# print description on screen
#print(describe)

with open(FILENAMEOUTPUT, "wt") as f:
    f.write(str(describe))
print (f"Description saved in Summary.txt file") 
