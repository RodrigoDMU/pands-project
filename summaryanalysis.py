#-------------------------------------------------------------------------------------------

# Higher Diploma in Science in Computing - Data Analytics

#-------------------------------------------------------------------------------------------

# Project Fisher's Iris Data Set

# This project was created as part of the Programming and Scripting assessment
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

#-------------------------------------------------------------------------------------------

# LOAD DATA

#-------------------------------------------------------------------------------------------

#---------------------------
# Load the Iris data set.
#---------------------------
df = pd.read_csv("irisdataset.csv")
print (df)

#-------------------------------------------------------------------------------------------

# SUMMARY ANALYSIS

#-------------------------------------------------------------------------------------------

# Creating and opening a new text file for summary.
with open("analysissummary.txt", "wt") as file: #[1]

    # Writing the introduction.
    file.write("Higher Diploma in Science in Computing - Data Analytics\n\n")
    file.write("Project Fisher's Iris Data Set\n")
    file.write("This project was created as part of the Programming ans Scripting assessment\n")
    file.write("module for the course in the Higher Diploma in Data Analytics at ATU.\n")
    file.write("This project is using the dataset Iris to demonstrate the skills developed\n")
    file.write("in the course in data analysis and visualization.\n\n")
    file.write("Author: Rodrigo De Martino Ucedo\n\n\n")

    # Writing the Load Data.

    file.write("LOAD DATA\n\n\n")

    file.write("Load the Iris data set.\n\n")
    file.write("df = pd.read_csv('irisdataset.csv')\n")
    file.write("print (df)\n\n")
    file.write(str(df) + "\n\n\n")

    # Writing the Inspect Data.

    file.write("INSPECT DATA\n\n\n")

    file.write("The first 5 rows of the dataset.\n\n")
    file.write("first5 = df.head()\n")
    file.write("print (first5)\n\n")
    file.write(str(df.head ()) + "\n\n")

    file.write("The last 5 rows of the dataset.\n\n")
    file.write("last5 = df.tail()\n")
    file.write("print (last5)\n\n")
    file.write(str(df.tail ()) + "\n\n")

    file.write("Informations of the dataset.\n\n")
    file.write("info = df.info ()\n")
    file.write("print (info)\n\n")
    file.write(str(df.info(buf=file)) + "\n\n") #[2] Output .info using buffer

    file.write("Count the number of null.\n\n")
    file.write("isnull = df.isnull().sum()\n")
    file.write("print (isnull)\n\n")
    file.write(str(df.isnull().sum()) + "\n\n")

    file.write("Describe the data set.\n\n")
    file.write("describe = df.describe()\n")
    file.write("print (describe)\n\n")
    file.write(str(df.describe()) + "\n\n")

    file.write("Describe the data set by Species.\n\n")
    file.write("describe_species = df.groupby('species').describe().transpose()\n")
    file.write("print (describe_species)\n\n")
    file.write(str(df.groupby('species').describe().transpose()) + "\n\n")

    file.write("Count the number of iris flower of each specie.\n\n")
    file.write("value_counts = df.value_counts(['species'])\n")
    file.write("print (value_counts)\n\n")
    file.write(str(df.value_counts(['species'])) + "\n\n")   
    
    file.write("Correlation of the data set.\n\n")
    file.write("correlation = df.corr(method='pearson', numeric_only=True)\n")
    file.write("print (correlation)\n\n")
    file.write(str(df.corr(method='pearson', numeric_only=True)) + "\n\n")   
    
    file.write("Correlation of the data set by Species.\n\n")
    file.write("correlation_species = df.groupby('species').corr(method='pearson', numeric_only=True)\n")
    file.write("print (correlation_species)\n\n")
    file.write(str(df.groupby('species').corr(method='pearson', numeric_only=True)) + "\n\n\n")   

    # Writing Visualization Data.

    file.write("VISUALIZATION DATA\n\n\n")

    file.write("Bar Chart.\n\n")
    file.write("Fig. 1 - Bar Chart\n\n")

    file.write("Histogram of Iris Flowers.\n\n")
    file.write("Fig. 2 - Histogram\n\n")

    file.write("Histogram of Iris Flowers by Species.\n\n")
    file.write("Fig. 3 - Histogram by Species\n\n")

    file.write("Boxplot of Iris Flowers by Species.\n\n")
    file.write("Fig. 4 - Boxplot\n\n")

    file.write("Correlation Heatmap of the data set.\n\n")
    file.write("Fig. 5 - Heatmap\n\n")

    file.write("Correlation Heatmap of the data set by Species.\n\n")
    file.write("Fig. 6 - Heatmap by Species\n\n")

    file.write("Scatter plot of Iris Flowers by Species.\n\n")
    file.write("Fig. 7 - Scatter plot by Species\n\n")

    file.write("Pair plot of Iris Flowers by Species.\n\n")
    file.write("Fig. 8 - Pair plot by Species \n\n\n")

    # Writing End.

    file.write("End\n")
    file.write("last commit on 19/05/2024.\n\n")

#-------------------------------------------------------------------------------------------

# REFERENCES

#-------------------------------------------------------------------------------------------

# [1] Reading and Writing to text files in Python. Availible in: https://www.geeksforgeeks.org/reading-writing-text-files-python/. [Accessed 14 May 2024].

# [2] Output .info using buffer. Availible in: https://stackoverflow.com/questions/59228983/store-df-info-method-output-in-dataframe-or-csv. [Accessed 14 May 2024].

#-------------------------------------------------------------------------------------------
# End
# last commit on 19/05/2024