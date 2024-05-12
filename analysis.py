#-------------------------------------------------------------------------------------------

# Higher Diploma in Science in Computing - Data Analytics

#-------------------------------------------------------------------------------------------

# Project Fisher's Iris Data Set

# This project was created as part of the Programming ans Scripting assessment
# module for the course in the Higher Diploma in Data Analytics at ATU. 
# This project is using the dataset Iris to demonstrate the skills developed 
# in the course in data analysis and visualization.

#-------------------------------------------------------------------------------------------
# Author: Rodrigo De Martino Ucedo
#-------------------------------------------------------------------------------------------

# LIBRARIES

#-------------------------------------------------------------------------------------------

# Data frames.
import pandas as pd

# Numerical arrays.
import numpy as np

# Plotting.
import matplotlib.pyplot as plt

# Graphic manipulation.
import seaborn as sns

# Ignore FutureWarning.
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#-------------------------------------------------------------------------------------------

# LOAD DATA

#-------------------------------------------------------------------------------------------

#---------------------------
# Load the Iris data set.
#---------------------------
df = pd.read_csv("irisdataset.csv")
print (df)

#      | sepal_length | sepal_width | petal_length | petal_width |     species
# -----|--------------|-------------|--------------|-------------|----------------
# 0    |          5.1 |       3.5   |        1.4   |      0.2    |   Iris-setosa
# 1    |          4.9 |       3.0   |        1.4   |      0.2    |   Iris-setosa
# 2    |          4.7 |       3.2   |        1.3   |      0.2    |   Iris-setosa
# 3    |          4.6 |       3.1   |        1.5   |      0.2    |   Iris-setosa
# 4    |          5.0 |       3.6   |        1.4   |      0.2    |   Iris-setosa
# ..   |          .   |       ...   |        ...   |      ...    |    ...
# 145  |          6.7 |       3.0   |        5.2   |      2.3    | Iris-virginica
# 146  |          6.3 |       2.5   |        5.0   |      1.9    | Iris-virginica
# 147  |          6.5 |       3.0   |        5.2   |      2.0    | Iris-virginica
# 148  |          6.2 |       3.4   |        5.4   |      2.3    | Iris-virginica
# 149  |          5.9 |       3.0   |        5.1   |      1.8    | Iris-virginica
#------|--------------|-------------|--------------|-------------|----------------
# [150 rows x 5 columns]

#-------------------------------------------------------------------------------------------

# INSPECT DATA

#-------------------------------------------------------------------------------------------

#-----------------------------------
# The first 5 rows of the dataset.
#-----------------------------------
first5 = df.head ()
print (first5)

#      | sepal_length | sepal_width | petal_length | petal_width |   species
# -----|--------------|-------------|--------------|-------------|-------------
#   0  |     5.1      |     3.5     |      1.4     |     0.2     | Iris-setosa	
#   1  |     4.9      |     3.0	    |      1.4	   |     0.2	 | Iris-setosa
#   2  |     4.7      |     3.2	    |      1.3	   |     0.2     | Iris-setosa
#   3  |     4.6      |     3.1	    |      1.5	   |     0.2	 | Iris-setosa
#   4  |     5.0      |     3.6	    |      1.4	   |     0.2	 | Iris-setosa
#------|--------------|-------------|--------------|-------------|-------------

#-----------------------------------
# The last 5 rows of the dataset.
#-----------------------------------
last5 = df.tail ()
print (last5)

#      | sepal_length | sepal_width | petal_length | petal_width |    species
# -----|--------------|-------------|--------------|-------------|----------------
#  145 |       6.7    |     3.0     |      5.2     |     2.3     | Iris-virginica
#  146 |       6.3    |     2.5     |      5.0     |     1.9     | Iris-virginica
#  147 |       6.5    |     3.0     |      5.2     |     2.0     | Iris-virginica
#  148 |       6.2    |     3.4     |      5.4     |     2.3     | Iris-virginica
#  149 |       5.9    |     3.0     |      5.1     |     1.8     | Iris-virginica
#------|--------------|-------------|--------------|-------------|----------------

#--------------------------------
# Informations of the dataset.
#--------------------------------
info = df.info ()
print (info)

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 150 entries, 0 to 149
# Data columns (total 5 columns):
#        Column     |   Non-Null Count  |    Dtype  
#-------------------|-------------------|-------------
#  0   sepal_length |   150 non-null    |   float64
#  1   sepal_width  |   150 non-null    |   float64
#  2   petal_length |   150 non-null    |   float64
#  3   petal_width  |   150 non-null    |   float64
#  4   species      |   150 non-null    |   object 
#-----------------------------------------------------
# dtypes: float64(4), object(1)

#----------------------------
# Count the number of null.
#----------------------------
isnull = df.isnull().sum()
print (isnull)

#     Species    | Freq
# ---------------|------
#  sepal_length  |  0
#  sepal_width   |  0
#  petal_length  |  0
#  petal_width   |  0
#  species       |  0
# ---------------|------
# dtype: int64

#-------------------------
# Descibe the data set.
#-------------------------
describe = df.describe()
print (describe)

#        | sepal_length | sepal_width | petal_length | petal_width 
# -------|--------------|-------------|--------------|-------------
#  count |  150.000000	|  150.000000 |	150.000000   |  150.000000
#  mean	 |  5.843333	|  3.057333   |  3.758000    |   1.199333
#  std	 |  0.828066	|  0.435866   |  1.765298    |   0.762238
#  min	 |  4.300000	|  2.000000   |  1.000000    |   0.100000
#  25%	 |  5.100000	|  2.800000   |  1.600000    |   0.300000
#  50%	 |  5.800000	|  3.000000   |  4.350000    |   1.300000
#  75%	 |  6.400000	|  3.300000   |  5.100000    |   1.800000
#  max	 |  7.900000	|  4.400000   |  6.900000    |   2.500000
#--------|--------------|-------------|--------------|-------------

#-----------------------------------
# Descibe the data set by Species. 
#-----------------------------------
describe_species = df.groupby('species').describe().transpose()
print (describe_species)

#              | species | Iris-setosa | Iris-versicolor |	Iris-virginica
#--------------|---------|-------------|-----------------|-------------------
# sepal_length | count   | 50.000000   |   50.000000     |   50.000000
#              | mean    | 5.006000    |   5.936000      |   6.588000
#              | std     | 0.352490    |   0.516171      |   0.635880
#              | min     | 4.300000    |   4.900000      |   4.900000
#              | 25%     | 4.800000    |   5.600000      |   6.225000
#              | 50%     | 5.000000    |   5.900000      |   6.500000
#              | 75%     | 5.200000    |   6.300000      |   6.900000
#              | max     | 5.800000    |   7.000000      |   7.900000
#--------------|---------|-------------|-----------------|-------------------
# sepal_width  | count   | 50.000000   |   50.000000     |   50.000000
#              | mean    | 3.418000    |   2.770000      |   2.974000
#              | std     | 0.381024    |   0.313798      |   0.322497
#              | min     | 2.300000    |   2.000000      |   2.200000
#              | 25%     | 3.125000    |   2.525000      |   2.800000
#              | 50%     | 3.400000    |   2.800000      |   3.000000
#              | 75%     | 3.675000    |   3.000000      |   3.175000
#              | max     | 4.400000    |   3.400000      |   3.800000
#--------------|---------|-------------|-----------------|-------------------
# petal_length | count   | 50.000000   |   50.000000     |   50.000000
#              | mean    | 1.464000    |   4.260000      |   5.552000
#              | std     | 0.173511    |   0.469911      |   0.551895
#              | min     | 1.000000    |   3.000000      |   4.500000
#              | 25%     | 1.400000    |   4.000000      |   5.100000
#              | 50%     | 1.500000    |   4.350000      |   5.550000
#              | 75%     | 1.575000    |   4.600000      |   5.875000
#              | max     | 1.900000    |   5.100000      |   6.900000
#--------------|---------|-------------|-----------------|-------------------
# petal_width  | count   | 50.000000   |   50.000000     |   50.000000
#              | mean    | 0.244000    |   1.326000      |   2.026000
#              | std     | 0.107210    |   0.197753      |   0.274650
#              | min     | 0.100000    |   1.000000      |   1.400000
#              | 25%     | 0.200000    |   1.200000      |   1.800000
#              | 50%     | 0.200000    |   1.300000      |   2.000000
#              | 75%     | 0.300000    |   1.500000      |   2.300000
#              | max     | 0.600000    |   1.800000      |   2.500000
#--------------|---------|-------------|-----------------|-------------------

#--------------------------------------------------
# Count the number of iris flower of each specie.
#--------------------------------------------------
value_counts = df.value_counts(['species'])
print (value_counts)

#      species      |  Freq
# ------------------|---------
#       setosa      |   50
#     versicolor    |   50
#     virginica     |   50
# ----------------------------
# Name: count, dtype: int64

#-------------------------------
# Correlation of the data set.
#-------------------------------
correlation = df.corr(method='pearson', numeric_only=True)
print (correlation)

#                | sepal_length | sepal_width | petal_length | petal_width 
# ---------------|--------------|-------------|--------------|-------------
#  sepal_length	 |   1.000000   |  -0.117570  |    0.871754  |   0.817941
#  sepal_width   |  -0.117570   |   1.000000  |   -0.428440  |  -0.366126
#  petal_length  |   0.871754   |  -0.428440  |    1.000000  |   0.962865
#  petal_width   |   0.817941   |  -0.366126  |    0.962865  |   1.000000
#----------------|--------------|-------------|--------------|-------------

#------------------------------------------
# Correlation of the data set by Species.
#------------------------------------------
correlation_species = df.groupby('species').corr(method='pearson', numeric_only=True)
print (correlation_species)

#     species     |              | sepal_length | sepal_width | petal_length | petal_width 
# ----------------|--------------|--------------|-------------|--------------|---------------					
#    Iris-setosa  | sepal_length |   1.000000   |   0.742547  |   0.267176   |   0.278098
#                 | sepal_width  |   0.742547   |   1.000000  |   0.177700   |   0.232752
#                 | petal_length |   0.267176   |   0.177700  |   1.000000   |   0.331630
#                 | petal_width  |   0.278098   |   0.232752  |   0.331630   |   1.000000
#-----------------|--------------|--------------|-------------|--------------|---------------
# Iris-versicolor | sepal_length |   1.000000   |   0.525911  |   0.754049   |   0.546461
#                 | sepal_width  |   0.525911   |   1.000000  |   0.560522   |   0.663999
#                 | petal_length |   0.754049   |   0.560522  |   1.000000   |   0.786668
#                 | petal_width  |   0.546461   |   0.663999  |   0.786668   |   1.000000
#-----------------|--------------|--------------|-------------|--------------|---------------
# Iris-virginica  | sepal_length |   1.000000   |   0.457228  |   0.864225   |   0.281108
#                 | sepal_width  |   0.457228   |   1.000000  |   0.401045   |   0.537728
#                 | petal_length |   0.864225   |   0.401045  |   1.000000   |   0.322108
#                 | petal_width  |   0.281108   |   0.537728  |   0.322108   |   1.000000
#-----------------|--------------|--------------|-------------|------------------------------

#-------------------------------------------------------------------------------------------

# VISUALIZATION DATA

#-------------------------------------------------------------------------------------------

#---------------------------
# Bar Chart
#---------------------------
# Add figure size.
plt.figure(figsize = (12,10))
# Count the number of penguins for each specie.
ax = sns.countplot(x='species', data=df, edgecolor = "black", palette=['royalblue','blueviolet','mediumslateblue'])
# Add title.
plt.title('Number of Iris Flowers by Species')
# Add labels (X and Y).
plt.xlabel('Species')
plt.ylabel('Number of Iris Flowers')
# Add total count on top of bar.
for container in ax.containers:  # Container with all the bars and optionally error bars, likely returned from bar
    ax.bar_label(container) # bar_label = add labels to bars
# Display the figure.
plt.show() 

#  _______________________________
# |                               |
# |     Fig. 1 - Bar Chart        |
# |_______________________________|

#-----------------------------
# Histogram of Iris Flowers.
#-----------------------------
slength = df['sepal_length']
sdwidth = df['sepal_width']
plength = df['petal_length']
pwidth = df['petal_width']

# Add figure size.
plt.figure(figsize = (12,10))

# Subplot position.
plt.subplot(2,2,1) # subplot (row, column, position)
plt.hist(slength, bins=20, color = "mediumslateblue",  alpha=0.7, edgecolor = 'black') # bins = number of bars, alpha = transparency
# Add labels (X and Y).
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')

# Subplot position.
plt.subplot(2,2,2)
plt.hist(sdwidth, bins=20, color = "mediumslateblue", alpha=0.7, edgecolor = 'black')
# Add labels (X and Y).
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')

# Subplot position.
plt.subplot(2,2,3)
plt.hist(plength, bins=20, color = "mediumslateblue", alpha=0.7, edgecolor = 'black')
# Add labels (X and Y).
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')

# Subplot position.
plt.subplot(2,2,4)
plt.hist(pwidth, bins=20, color = "mediumslateblue", alpha=0.7, edgecolor = 'black')
# Add labels (X and Y).
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')

# Display the figure.
plt.show()

#  _______________________________
# |                               |
# |     Fig. 2 - Histogram        |
# |_______________________________|

#----------------------------------------
# Histogram of Iris Flowers by Species.
#----------------------------------------

# Add figure size.
plt.figure(figsize = (12,10))

# Subplot position.
plt.subplot(2,2,1) # subplot (row, column, position)
sns.histplot(data=df, x="sepal_length", hue = "species", multiple="stack", bins = 20, edgecolor = "black", palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')

# Subplot position.
plt.subplot(2,2,2)
sns.histplot(data=df, x='sepal_width', hue = "species", multiple="stack", bins = 20, edgecolor = "black", palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')

# Subplot position.
plt.subplot(2,2,3)
sns.histplot(data=df, x='petal_length', hue = "species", multiple="stack", bins = 20, edgecolor = "black", palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')

# Subplot position.
plt.subplot(2,2,4)
sns.histplot(data=df, x='petal_width', hue = "species", multiple="stack", bins = 20, edgecolor = "black", palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')

# Display the figure.
plt.show()

#  _________________________________________
# |                                         |
# |     Fig. 3 - Histogram by Species       |
# |_________________________________________|

#---------------------------------------
# Boxplot of Iris Flowers by Species.
#---------------------------------------

# Add figure size.
plt.figure(figsize = (12,10))

# Subplot position.
plt.subplot(2,2,1) # subplot (row, column, position)
sns.boxplot(x='species',y='sepal_length',data=df, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')
# Subplot position.

plt.subplot(2,2,2)
sns.boxplot(x='species',y='sepal_width',data=df, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Species')
plt.ylabel('Sepal Width (cm)')

# Subplot position.
plt.subplot(2,2,3)
sns.boxplot(x='species',y='petal_length',data=df, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')

# Subplot position.
plt.subplot(2,2,4)
sns.boxplot(x='species',y='petal_width',data=df, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Species')
plt.ylabel('Petal Width (cm)')

# Display the figure.
plt.show()

#  ___________________________
# |                           |
# |     Fig. 4 - Boxplot      |
# |___________________________|

#---------------------------------------
# Correlation Heatmap of the data set.
#---------------------------------------

sns.heatmap(correlation, cmap = "Purples", annot=True, fmt='.2g')
# Add title.
plt.title('Correlation Heatmap of Iris Flowers')
# Add labels (X and Y).
plt.xlabel('Features')
plt.ylabel('Features')

# Display the figure.
plt.show()

#  ___________________________
# |                           |
# |     Fig. 5 - Heatmap      |
# |___________________________|

#-------------------------------------------------
# Correlation Heatmap of the data set by Species. 
#-------------------------------------------------

sns.heatmap(correlation_species, cmap = "Purples", annot=True, fmt='.2g')
# Add title.
plt.title('Correlation Heatmap of Iris Flowers by Species')
# Add labels (X and Y).
plt.xlabel('Features')
plt.ylabel('Species')

# Display the figure.
plt.show()

#  _____________________________________
# |                                     |
# |     Fig. 6 - Heatmap by Species     |
# |_____________________________________|

#-------------------------------------------
# Scatter plot of Iris Flowers by Species.
#-------------------------------------------

# Add figure size.
plt.figure(figsize = (20,20))

# Subplot position.
plt.subplot(4,3,1) # subplot (row, column, position)
sns.scatterplot(x='sepal_length', y='sepal_width', data=df, hue ='species', size= 50, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')

# Subplot position.
plt.subplot(4,3,2)
sns.scatterplot(x='sepal_length', y='petal_length', data=df, hue ='species', size= 50, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')

# Subplot position.
plt.subplot(4,3,3)
sns.scatterplot(x='sepal_length', y='petal_width', data=df, hue ='species', size= 50, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Width (cm)')

plt.subplot(4,3,4) 
sns.scatterplot(x='sepal_width', y='sepal_length', data=df, hue ='species', size= 50, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Sepal Length (cm)')

# Subplot position.
plt.subplot(4,3,5)
sns.scatterplot(x='sepal_width', y='petal_length', data=df, hue ='species', size= 50, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Petal Length (cm)')

# Subplot position.
plt.subplot(4,3,6)
sns.scatterplot(x='sepal_width', y='petal_width', data=df, hue ='species', size= 50, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Petal Width (cm)')

plt.subplot(4,3,7) 
sns.scatterplot(x='petal_length', y='sepal_length', data=df, hue ='species', size= 50, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Petal Length (cm)')
plt.ylabel('Sepal Length (cm)')

# Subplot position.
plt.subplot(4,3,8)
sns.scatterplot(x='petal_length', y='sepal_width', data=df, hue ='species', size= 50, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Petal Length (cm)')
plt.ylabel('Sepal Width (cm)')

# Subplot position.
plt.subplot(4,3,9)
sns.scatterplot(x='petal_length', y='petal_width', data=df, hue ='species', size= 50, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')

plt.subplot(4,3,10) 
sns.scatterplot(x='petal_width', y='sepal_length', data=df, hue ='species', size= 50, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Petal Width (cm)')
plt.ylabel('Sepal Length (cm)')

# Subplot position.
plt.subplot(4,3,11)
sns.scatterplot(x='petal_width', y='sepal_width', data=df, hue ='species', size= 50, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Petal Width (cm)')
plt.ylabel('Sepal Width (cm)')

# Subplot position.
plt.subplot(4,3,12)
sns.scatterplot(x='petal_width', y='sepal_length', data=df, hue ='species', size= 50, palette=['royalblue','blueviolet','mediumslateblue'])
# Add labels (X and Y).
plt.xlabel('Petal Width (cm)')
plt.ylabel('Petal Length (cm)')

# Display the figure.
plt.show()

#  ____________________________________________
# |                                            |
# |     Fig. 7 - Scatter plot by Species       |
# |____________________________________________|

#----------------------------------------
# Pair plot of Iris Flowers by Species.
#----------------------------------------

sns.pairplot(df, hue="species", height=3,  palette=['royalblue','blueviolet','mediumslateblue'])
# Display the figure.
plt.show()

#  _________________________________________
# |                                         |
# |     Fig. 8 - Pair plot by Species       |
# |_________________________________________|

#-------------------------------------------------------------------------------------------
# End
# last commit on 20/05/2024