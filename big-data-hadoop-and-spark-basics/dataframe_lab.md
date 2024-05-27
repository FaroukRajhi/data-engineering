
For this lab, we are going to be using Python and Spark (PySpark). These libraries should be installed in your lab environment or in SN Labs.

Pandas is a popular data science package for Python. In this lab, we use Pandas to load a CSV file from disc to a pandas dataframe in memory. PySpark is the Spark API for Python. In this lab, we use PySpark to initialize the spark context.

# Installing required packages
!pip install pyspark
!pip install findspark
!pip install pandas
import findspark
findspark.init()
import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
Exercise 1 - Spark session
In this exercise, you will create and initialize the Spark session needed to load the dataframes and operate on it

Task 1: Creating the spark session and context
​
# Creating a spark session
spark = SparkSession \
    .builder \
    .appName("Python Spark DataFrames basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
This will give an output similar to:

23/10/17 08:29:37 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Task 2: Initialize Spark session
To work with dataframes we just need to verify that the spark session instance has been created.

spark
Exercise 2 - Load the data and Spark dataframe
In this section, you will first read the CSV file into a Pandas DataFrame and then read it into a Spark DataFrame. Pandas is a library used for data manipulation and analysis. Pandas offers data structures and operations for creating and manipulating Data Series and DataFrame objects. Data can be imported from various data sources, e.g., Numpy arrays, Python dictionaries, and CSV files. Pandas allows you to manipulate, organize and display the data. To create a Spark DataFrame we load an external DataFrame, called mtcars. This DataFrame includes 32 observations on 11 variables:

colIndex	colName	units/description
[, 1]	mpg	Miles per gallon
[, 2]	cyl	Number of cylinders
[, 3]	disp	Displacement (cu.in.)
[, 4]	hp	Gross horsepower
[, 5]	drat	Rear axle ratio
[, 6]	wt	Weight (lb/1000)
[, 7]	qsec	1/4 mile time
[, 8]	vs	V/S
[, 9]	am	Transmission (0 = automatic, 1 = manual)
[,10]	gear	Number of forward gears
[,11]	carb	Number of carburetors
Task 1: Loading data into a Pandas DataFrame
# Read the file using `read_csv` function in pandas
mtcars = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/labs/data/mtcars.csv')
# Preview a few records
mtcars.head()
Task 2: Loading data into a Spark DataFrame
# We use the `createDataFrame` function to load the data into a spark dataframe
sdf = spark.createDataFrame(mtcars) 
# Let us look at the schema of the loaded spark dataframe
sdf.printSchema()
Exercise 3: Basic data analysis and manipulation
In this section, we perform basic data analysis and manipulation. We start with previewing the data and then applying some filtering and columwise operations.

Task 1: Displays the content of the DataFrame
We use the show() method for this. Here we preview the first 5 records. Compare it to a similar head() function in Pandas.

sdf.show(5)
We use the select() function to select a particular column of data. Here we show the mpg column.

sdf.select('mpg').show(5)
Task 2: Filtering and Columnar operations
Filtering and Column operations are important to select relevant data and apply useful transformations.

We first filter to only retain rows with mpg > 18. We use the filter() function for this.

sdf.filter(sdf['mpg'] < 18).show(5)
Operating on Columns

Spark also provides a number of functions that can be directly applied to columns for data processing and aggregation. The example below shows the use of basic arithmetic functions to convert the weight values from lb to metric ton. We create a new column called wtTon that has the weight from the wt column converted to metric tons.

sdf.withColumn('wtTon', sdf['wt'] * 0.45).show(5)
Task 3: Rename the existing column name "vs" to "versus" and assign the new result DataFrame to a variable, "sdf_new".
The function "withColumnRenamed()" renames the existing column names.

sdf_new = sdf.withColumnRenamed("vs", "versus")
The execution of the above function doesn’t modify the original DataFrame "sdf"; instead, a new DataFrame "sdf_new" is created with the renamed column.

Task 4: Filter the records based on the condition
The function "where()" filters the Dataframe rows based on the given condition. It returns a new DataFrame containing the rows that satisfy the given condition.

sdf.where(sdf['mpg'] < 18).show(3) 
Note: Both filter() and where() functions are used for the same purpose.

Task 5: Combining DataFrames based on a specific condition.
The function "join()"combines the DataFrames based on a specific condition.

See the below examples.

# define sample DataFrame 1 
​
data = [("A101", "John"), ("A102", "Peter"), ("A103", "Charlie")] 
​
columns = ["emp_id", "emp_name"] 
​
dataframe_1 = spark.createDataFrame(data, columns) 
# define sample DataFrame 2 
​
data = [("A101", 1000), ("A102", 2000), ("A103", 3000)]
​
columns = ["emp_id", "salary"]
​
dataframe_2 = spark.createDataFrame(data, columns)
# create a new DataFrame, "combined_df" by performing an inner join
​
combined_df = dataframe_1.join(dataframe_2, on="emp_id", how="inner")
Task 6: Filling the missing values
"fillna()" or "fill()" function fill the missing values with a specified value.

# define sample DataFrame 1
​
data = [("A101", 1000), ("A102", 2000), ("A103",None)]
​
columns = ["emp_id", "salary"]
​
dataframe_1 = spark.createDataFrame(data, columns)
Note that the third record of the DataFrame "dataframe_1", the column “salary”, contains null("na") value. It can be filled with a value by using the function "fillna()".

# fill missing salary value with a specified value 
​
filled_df = dataframe_1.fillna({"salary": 3000}) 
filled_df.head(3)
Exercise 4: Grouping and Aggregation
Spark DataFrames support a number of commonly used functions to aggregate data after grouping. In this example we compute the average weight of cars by their cylinders as shown below.

sdf.groupby(['cyl'])\
.agg({"wt": "AVG"})\
.show(5)
We can also sort the output from the aggregation to get the most common cars.

car_counts = sdf.groupby(['cyl'])\
.agg({"wt": "count"})\
.sort("count(wt)", ascending=False)\
.show(5)
​
Practice Questions
Question 1 - DataFrame basics
Display the first 5 rows of all cars that have atleast 5 cylinders.

# Code block for learners to answer
Question 2 - DataFrame aggregation
Using the functions and tables shown above, print out the mean weight of a car in our database in metric tons.

# Code block for learners to answer
Question 3 - DataFrame columnar operations
In the earlier sections of this notebook, we have created a new column called wtTon to indicate the weight in metric tons using a standard conversion formula. In this case we have applied this directly to the dataframe column wt as it is a linear operation (multiply by 0.45). Similarly, as part of this exercise, create a new column for mileage in kmpl (kilometer-per-liter) instead of mpg(miles-per-gallon) by using a conversion factor of 0.425.

Additionally sort the output in decreasing order of mileage in kmpl.