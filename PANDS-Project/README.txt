README.txt for PANDS-Project
This file is a Readme file for the PANDS project, submitted in fulfilment of requirements for the Higher Diploma in Computer Science and Data Analytics at Atlantic Technical University. 
Readme.txt was compiled by Cathal Redmond from March to May 2025. to aid with the comprehension of the work herewithin contained, and to document the development of the code/script solutions put forward to complete the tasks required. 

##Executive Overview: 
The IRIS dataset is a popular educational resource, used as a test dataset to allow students to develop their coding skills. 

##Background:
The Iris dataset was first published in 1936 in the academic Journal 'Annals of Eugenics' (now 'Annals of Human Genetics') by biologist Ronald Fisher, as a demonstration of statistical methods of classification of different species of Iris flower plants(1). The data is an example of a multivariate data set, containing multiple observations & recordings of a test subject, taken simultaneously (2). Edgar Anderson collected the data at the John Innes Horticultural Institution in the UK (3). The dataset is now hosted and maintained by the University of California at Irvine (4).

##Iris Dataset Description:
The Dataset has 150 lines of text, each an instance/ observation of Iris plant measurements. 50 instances of three species are listed in the dataset. The data is available for download from the UC Irvine website, after which it must be unzipped and saved to the location it will be used from. Four files are present in the zipped folder: Iris.data, bezdekIris.data, iris.names, and Indes. The data is organised into 150 lines of text, with 5 distinct text items on each line reading from left to right; 4 floating point values followed by one text string. The iris dataset file does not contain headers, line value indicators, or any other meta-info. 
Information about the Iris dataset is given in the Iris.names file, where the numbers in each of the rows are identified as being measurements; 
1. sepal length (in cm)
2. sepal width (in cm)
3. petal length (in cm)
4. petal width (in cm)
5. class: (Setosa, Versicolour, Virginica)
We can say that after analysis of the Iris dataset that the three species are distinct in their features, Setosa has the shortest and smallest petals by far. While the Setosa sepal is also shorter, Setosa's sepal is actually wider on average than the other two species. The Virginica and Versicolor species overlap on every variable measured, so they are not easily separable. 

##Desired outcome: 
The desired outcomes of this exercise are many; the primary goal is to learn how to source and analyse data using Python tools. The Iris dataset is a good test case on which to perform this task, as it is extensively studied and there exists a good many examples of analysis previously performed on the dataset that are freely available to be found online. 
The secondary, more important intention is that the student will learn how to research the techniques needed to perform the task efficiently and expediently. The student will need to go beyond what has been taught in lectures to achieve this goal; therefore will learn the higher cognitive goals of research and self-directed problem solving, which are essential in the perpetually evolving modern digital landscape. As new tools become available, they bring with them a raft of new compatability and integration issues; This is the norm for rapidly advancing technical fields - by learning the problem solving tools on an extremely popular system using a well documented dataset, a robust framework can be built from which to tackle more intensive or specialist techniques. 

##Project plan 
I will approach this project from a top-down direction - writing the code in working blocks in the sequence they are laid out in the project specification. As i have limited time to complete this project, i will assign 2 weeks of time to complete the main bulk of the code processing, one week for review and editing, and one week of overrun time ahead of the submission deadline in case there are any unforseen delays in the development of the code, or in time availability to complete the code. 

I will plan to tackle the problems as set out in the project assignment by researching the issues on the provided resource websites and general web searches, as they come up in the project. I have made the distinct decision not to use any AI generated code for this module, as i feel i need to develop a strong intuitive sense of the code i am writing and need to be able to explain how it functions, which i feel is the entire point of undertaking the course in the first place. My motivation for learning to code is both intrinsicand extrinsic, as i desire to use it in my professional life as a medical devices engineer to develop my data analysis abilities, but also i want to learn how to code to satisfy a desire i have had for a long time to be able to use custom code to produce custom graphics for analysis of election results & Census data, to understand the relationship between people living in a place and the data collected about them. 

## User instructions
This script is loaded using a terminal or Python environment. The user will trigger the script to run by typing "python analysis.py" while navigating to the repository in which the script is saved. 
The script opens the iris.data file, and parses out the information contained within into a 'master' dataframe. 
The dataframe is then sliced into three sub-dataframes using the unique species names as the argument for selecting what to include in each file. 
From there, the data is used to define several types of graphic plots in sequenced groups 
  - First, the 4 variable types are displayed as a histogram for each species, after which these plots are saved as .png image files. 
  - Second, the data is again sliced, this time displaying each of the three species together on a histogram for each variable type - Petal length, petal width, sepal length, and sepal width. 
  - Third, a scatter plot is generated of the data, with data for each recorded flower cast into a scatterplot that uses the paired variables as X-Y coordinates of a length-width Cartesian plane (petal length and petal width are used together to form one point). Each species has a different colour for both petals and sepals for six groups total. 
  - Fourth, is Boxplots for each species and variable. Box plots are a very good one-dimensional graphic representation that can show the distribution of a set: The max, mean, minimum, 25% and 75%, and outlier are plotted in this intuitive graph. This is a powerful tool for directly comparing each subset of the data, and allows the user to quickly and visually compare the data without any need to perform any numerical calculations.
  - Lastly, a pairplot showing the relationship interactions of each data subset against each other subset - take, for instance, petal length vs sepal width for each species. This allows for a dense visual plot that may be used for the display of exhaustive interactions between datasets. 

The script outputs a text file summarising the descriptive statistics of the datasets as a text file. 
The script also outputs data to the terminal window: the entire dataset is displayed, along with various summaries and calculation results, which are not saved to the text file that is output. 
I have programmed the script to perform 2 comparative tests for indication purposes only: T-tests, which compare 2 selected sets of the data, and ANOVA, which can compare more than 2 sets at a time. These tests are not exhaustive in their comparison as I have only performed the comparison once per type, only to display that it is possible to perform this analysis. 

I am disappointed with my project planning that I did not leave more time to develop each of the scripts as callable modules that would cycle through the data as while loops that would cycle through the data, instead, I have them 'manually' programmed. I feel with a little more time and better time management, I could reduce the explicit code into a smarter formulation that would loop through each variable for each of the calculations and plots without the need to manually program them. This would also improve the robustness of the code and improve its editability for use on future datasets. 
While i am disappointed with myself for not developing some of the more advanced features of the file that i initially had in my vision from the outset, i also recognise i have learned significant amounts of skill and technique to be able to produce this output. 

(1) https://en.wikipedia.org/wiki/Iris_flower_data_set
(2) https://en.wikipedia.org/wiki/Multivariate_statistics
(3) https://en.wikipedia.org/wiki/Edgar_Anderson
(4) https://archive.ics.uci.edu/dataset/53/iris

