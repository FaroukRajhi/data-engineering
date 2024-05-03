"""
**Pandas** is a popular library for data analysis built on top of the Python programming language. Pandas generally provide two data structures for manipulating data, They are:

*   DataFrame
*   Series

A **DataFrame** is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.

*   A Pandas DataFrame will be created by loading the datasets from existing storage.
*   Storage can be SQL Database, CSV file, an Excel file, etc.
*   It can also be created from the lists, dictionary, and from a list of dictionaries.

**Series** represents a one-dimensional array of indexed data.
It has two main components :

1.  An array of actual data.
2.  An associated array of indexes or data labels.

The index is used to access individual data values. You can also get a column of a dataframe as a **Series**. You can think of a Pandas series as a 1-D dataframe.

"""
import pandas as pd

csv_path = 'exercise03_car_sales_data.csv'

df = pd.read_csv(csv_path)

#print(df)
#print(df.head())
print(df['year']) # print specified column
