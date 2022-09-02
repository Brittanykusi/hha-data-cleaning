# Data Cleaning

## First Steps
- make sure python is installed in the environment of use 
- import pandas
- import numpy

### Loads the data into python


### Prints the count of columns and rows


### Provides aprint out of the column names


### Cleans the column names


### Cleans the strings that might exist within each column


### Assesses white space or special characters


### Converts the column types to the correct types (e.g., DOB field is datetime and not
object)


### Look for duplicate rows and remove duplicate rows


### Assess missingness (count of missing values per column)


### New data field: attempt to create a new column called modality_inperson.  This
column should contain a binary value of true or false. Try to write a function that takes in the old column
name (learning modality), and recodes the value for a specific row to true, if
the learning modality value is ‘in-person’, and recodes it to false if the value
is either ‘remote’ or ‘hybrid’
