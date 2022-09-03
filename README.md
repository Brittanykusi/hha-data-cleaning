# Data Cleaning

## First Steps
- make sure python is installed in the environment of use 
- import pandas
- import numpy

### Load the datafile into python
- in this case we are loading a csv file || df = pd.read_csv('df_name_here')


### Print the count of columns and rows
- count the number of columns and rows || df.shape
- you can assign names to the values || countRows, countColumns = df.shape


### Provide a print out of the column names
- to print out column names || list(df)


### Cleans the column names by getting rid of white space and special characters
- this command replaces spaces and special characters with and '_' || df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_') 
- use this to make all letter of column names lower case || df.columns = df.columns.str.lower() 


### Cleans the strings that might exist within each column
-


### Converts the column types to the correct types (e.g., DOB field is datetime and not object)
- to display all columns and variable type || df.dtypes
- to convert variable type || df['column_name'] = df['column_name'].astype(str)
df['column_name'] = str(df['column_name'])


### Look for duplicate rows and remove duplicate rows
- see which columns contain duplicates || print(df.duplicated())
- count of how many duplicates exist || print(df.duplicated().sum())


### Assess missingness (count of missing values per column)
- df.isnull().sum()


### New datafield: attempt to create a new column called modality_inperson. 
- create a new column and use where to place a boolean value on learning modality type - true if inperson and false if otherwise || df['modality_inperson'] = pd.np.where(df.learning_modality.str.contains("In Person"), "true", "false")
- view learning modality to cross check with modality inperson values || df['learning_modality'] 
- print modality_inperson || df['modality_inperson']
- print the first 50 rows of the table || print(df.head(50))
