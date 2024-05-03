import pandas as pd

# Define a dictionary 'x'
x = {'name': ['Rose', 'John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 'Salary': [100000, 80000, 50000, 60000]}

# casting the dictionary to a DataFrame

df = pd.DataFrame(x)

print (df)

#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]

# Access the value on the first row and the third column

print(df.iloc[0,1])
