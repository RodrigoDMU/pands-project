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

#-------------------------------------------------------------------------------------------

# LOAD DATA

#-------------------------------------------------------------------------------------------

#---------------------------
# Load the Iris data set.
#---------------------------
df = pd.read_csv("irisdataset.csv")
print (df)

#      | sepal_length | sepal_width | petal_length | petal_width |   species
# -----|--------------|-------------|--------------|-------------|-------------
# 0    |          5.1 |       3.5   |        1.4   |      0.2    |   setosa
# 1    |          4.9 |       3.0   |        1.4   |      0.2    |   setosa
# 2    |          4.7 |       3.2   |        1.3   |      0.2    |   setosa
# 3    |          4.6 |       3.1   |        1.5   |      0.2    |   setosa
# 4    |          5.0 |       3.6   |        1.4   |      0.2    |   setosa
# ..   |          .   |       ...   |        ...   |      ...    |    ...
# 145  |          6.7 |       3.0   |        5.2   |      2.3    |  virginica
# 146  |          6.3 |       2.5   |        5.0   |      1.9    |  virginica
# 147  |          6.5 |       3.0   |        5.2   |      2.0    |  virginica
# 148  |          6.2 |       3.4   |        5.4   |      2.3    |  virginica
# 149  |          5.9 |       3.0   |        5.1   |      1.8    |  virginica
#------|--------------|-------------|--------------|-------------|-------------
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
#   0  |     5.1      |     3.5     |      1.4     |     0.2     |    setosa
#   1  |     4.9      |     3.0	    |      1.4	   |     0.2	 |    setosa
#   2  |     4.7      |     3.2	    |      1.3	   |     0.2     |    setosa
#   3  |     4.6      |     3.1	    |      1.5	   |     0.2	 |    setosa
#   4  |     5.0      |     3.6	    |      1.4	   |     0.2	 |    setosa
#------|--------------|-------------|--------------|-------------|-------------

#-----------------------------------
# The last 5 rows of the dataset.
#-----------------------------------
last5 = df.tail ()
print (last5)

#      | sepal_length | sepal_width | petal_length | petal_width |   species
# -----|--------------|-------------|--------------|-------------|-------------
#  145 |       6.7    |     3.0     |      5.2     |     2.3     |  virginica
#  146 |       6.3    |     2.5     |      5.0     |     1.9     |  virginica
#  147 |       6.5    |     3.0     |      5.2     |     2.0     |  virginica
#  148 |       6.2    |     3.4     |      5.4     |     2.3     |  virginica
#  149 |       5.9    |     3.0     |      5.1     |     1.8     |  virginica
#------|--------------|-------------|--------------|-------------|-------------

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

#-----------------------------------------------
# Count the number of penguins of each specie.
#-----------------------------------------------
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

#  species     |              | sepal_length | sepal_width | petal_length | petal_width 
# -------------|--------------|--------------|-------------|--------------|---------------					
#    setosa    | sepal_length |   1.000000   |   0.742547  |   0.267176   |   0.278098
#              | sepal_width  |   0.742547   |   1.000000  |   0.177700   |   0.232752
#              | petal_length |   0.267176   |   0.177700  |   1.000000   |   0.331630
#              | petal_width  |   0.278098   |   0.232752  |   0.331630   |   1.000000
#--------------|--------------|--------------|-------------|--------------|---------------
#  versicolor  | sepal_length |   1.000000   |   0.525911  |   0.754049   |   0.546461
#              | sepal_width  |   0.525911   |   1.000000  |   0.560522   |   0.663999
#              | petal_length |   0.754049   |   0.560522  |   1.000000   |   0.786668
#              | petal_width  |   0.546461   |   0.663999  |   0.786668   |   1.000000
#--------------|--------------|--------------|-------------|--------------|---------------
#   virginica  | sepal_length |   1.000000   |   0.457228  |   0.864225   |   0.281108
#              | sepal_width  |   0.457228   |   1.000000  |   0.401045   |   0.537728
#              | petal_length |   0.864225   |   0.401045  |   1.000000   |   0.322108
#              | petal_width  |   0.281108   |   0.537728  |   0.322108   |   1.000000
#--------------|--------------|--------------|-------------|------------------------------

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
plt.show ()    

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
plt.subplot(2,2,1) # plt.subplot(row, column, position)
plt.hist(slength, bins=20, color = "mediumslateblue",  alpha=0.7, edgecolor = 'black') # bins = number of bars, alpha = transparency
# Add labels (X and Y).
plt.xlabel('Frequency')
plt.ylabel('Sepal Length (cm)')
# Subplot position.
plt.subplot(2,2,2)
plt.hist(sdwidth, bins=20, color = "mediumslateblue", alpha=0.7, edgecolor = 'black')
# Add labels (X and Y).
plt.xlabel('Frequency')
plt.ylabel('Sepal Width (cm)')
# Subplot position.
plt.subplot(2,2,3)
plt.hist(plength, bins=20, color = "mediumslateblue", alpha=0.7, edgecolor = 'black')
# Add labels (X and Y).
plt.xlabel('Frequency')
plt.ylabel('Petal Length (cm)')
# Subplot position.
plt.subplot(2,2,4)
plt.hist(pwidth, bins=20, color = "mediumslateblue", alpha=0.7, edgecolor = 'black')
# Add labels (X and Y).
plt.xlabel('Frequency')
plt.ylabel('Petal Width (cm)')
plt.show()

#  _______________________________
# |                               |
# |     Fig. 2 - Histogram        |
# |_______________________________|


#-------------------------------------------------------------------------------------------
# End
# last commit on 20/05/2024