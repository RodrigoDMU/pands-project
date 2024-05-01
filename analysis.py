#-------------------------------------------------------------------------------------------

# Higher Diploma in Science in Computing - Data Analytics

#-------------------------------------------------------------------------------------------

# Project Fisher's Iris Data Set

# This project was created as part of the Programming ans Scripting 
# assessment module for the course in the Higher Diploma in Data Analytics at ATU. 
# This project is using the dataset palmerpenguis to demonstrate the skills developed 
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

# The last 5 rows of the dataset.
df.tail ()
print (df)

# Informations of the dataset.
df.info ()
print (df)

# Count the number of null.
df.isnull().sum()
print (df)

# Descibe the data set.
df.describe()
print (df)

# Count the number of penguins of each specie.
df.value_counts(['species'])
print (df)


#-------------------------------------------------------------------------------------------