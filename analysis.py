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

#-------------------------------------------------------------------------------------------

# LOAD DATA

#-------------------------------------------------------------------------------------------

# Load the Iris data set.
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

# The first 5 rows of the dataset.
df.head ()
print (df)

#      | sepal_length | sepal_width | petal_length | petal_width |   species
# -----|--------------|-------------|--------------|-------------|-------------
#   0  |     5.1	  |     3.5	    |      1.4	   |     0.2	 |    setosa
#   1  |     4.9	  |     3.0	    |      1.4	   |     0.2	 |    setosa
#   2  |     4.7      | 	3.2	    |      1.3	   |     0.2	 |    setosa
#   3  |     4.6	  |     3.1	    |      1.5	   |     0.2	 |    setosa
#   4  |     5.0	  |     3.6	    |      1.4	   |     0.2	 |    setosa
#------|--------------|-------------|--------------|-------------|-------------
# The last 5 rows of the dataset.
df.tail ()
print (df)

#	sepal_length	sepal_width	petal_length	petal_width	species
#145	6.7	3.0	5.2	2.3	virginica
#146	6.3	2.5	5.0	1.9	virginica
#147	6.5	3.0	5.2	2.0	virginica
#148	6.2	3.4	5.4	2.3	virginica
#149	5.9	3.0	5.1	1.8	virginica

# Informations of the dataset.
df.info ()
print (df)

#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 150 entries, 0 to 149
#Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
#---  ------        --------------  -----  
# 0   sepal_length  150 non-null    float64
# 1   sepal_width   150 non-null    float64
# 2   petal_length  150 non-null    float64
# 3   petal_width   150 non-null    float64
# 4   species       150 non-null    object 
#dtypes: float64(4), object(1)

# Count the number of null.
df.isnull().sum()
print (df)

# ---------------|-----
#  sepal_length  |  0
#  sepal_width   |  0
#  petal_length  |  0
#  petal_width   |  0
#  species       |  0
# ---------------|-----
# dtype: int64

# Descibe the data set.
df.describe()
print (df)

#	sepal_length	sepal_width	petal_length	petal_width
#count	150.000000	150.000000	150.000000	150.000000
#mean	5.843333	3.057333	3.758000	1.199333
#std	0.828066	0.435866	1.765298	0.762238
#min	4.300000	2.000000	1.000000	0.100000
#25%	5.100000	2.800000	1.600000	0.300000
#50%	5.800000	3.000000	4.350000	1.300000
#75%	6.400000	3.300000	5.100000	1.800000
#max	7.900000	4.400000	6.900000	2.500000

# Count the number of penguins of each specie.
df.value_counts(['species'])
print (df)

#      species      |  Freq
# ------------------|---------
#       setosa      |   50
#     versicolor    |   50
#     virginica     |   50
# ----------------------------
# Name: count, dtype: int64






#-------------------------------------------------------------------------------------------
# End
# last commit on 20/05/2024