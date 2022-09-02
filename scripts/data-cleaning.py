import pandas as pd
import numpy as np 

## 1.load dataset into python
df = pd.read_csv('/Users/brittanykusi-gyabaah/Desktop/AHI/School_Learning_Modalities.csv')
# print table
df



## 2.print the count of columns and rows
# assign variable for row count and column count
countR, countC = df.shape
# print count of rows
countR
# print count of columns
countC



## 3.print out of column names
# assign variable for column names
list(df)



## 4&6.clean column names/ assesses white space or special characters
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_') 
# change all column names to lowercase
df.columns = df.columns.str.lower()
list(df) 



## 5.cleans the strings that might exist within each column
strings = df.select_dtypes(include=['object']).columns
strings ## strings seem to be fine



## 7.convert columns types to the correct types 
strings = df.select_dtypes(include=['object']).columns
strings
numbers = df.select_dtypes(include=['int64', 'float64']).columns
numbers 
dates = df.select_dtypes(include=['datetime64[ns]']).columns
dates
booleans = df.select_dtypes(include=['bool']).columns
booleans
objects = df.select_dtypes(include=['object']).columns
objects
df.dtypes ## all columns are already in the correct data types



## 8.look for and remove duplicate rows
# see which columns contain duplicates
print(df.duplicated())
# count of how many duplicates exist
print(df.duplicated().sum())
## this df has no duplicates

## 9.assess the amount of missing values in each column
df.isnull().sum()



## 10.New datafield: attempt to create a new column called modality_inperson. 
## This column should contain a binary value of true or false. 
## Try to write a function that takes in the old column name (learning modality), 
## and recodes the value for a specific row to true, if the learning modality value is ‘in-person’, 
## and recodes it to false if the value is either ‘remote’ or ‘hybrid’



df['modality_inperson'] = pd.np.where(df.learning_modality.str.contains("In Person"), "true", "false")
df['learning_modality'] 
df['modality_inperson']
print(df.head(50))
