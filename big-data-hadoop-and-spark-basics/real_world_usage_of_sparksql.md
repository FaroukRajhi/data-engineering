Welcome to "Apache Spark SQL."
After watching this video, you will be able to:
Define Spark SQL
Create a table view in Spark SQL
Explain how to aggregate data using Spark SQL
Explain the various data sources Spark SQL supports
Here is a quick recap of Spark SQL.
Spark SQL Is a Spark module for structured data processing.
Spark SQL is used to run SQL queries on Spark DataFrames and has available APIs in Java,
Scala, Python, and R.
The first step to running SQL queries in Spark SQL
is to create a table view. A table view is a temporary table used to run SQL queries.
Spark SQL supports both temporary and global temporary table views.
A temporary view has local scope.
Local scope means that the view exists only within the current spark session on the current node.
A global temporary view, however, exists within the general Spark application. A
global temporary view is shareable across different Spark sessions.
Here is an example that shows how to create a temporary view in Python using PySpark.
You first create the DataFrame from the JSON file, then create a temporary view called "people."
You can then run a SQL query using this view.
Here is the same example, but this time, you are creating a Global Temporary View.
Note the minor syntax change, including the "Global" prefix to the function name
and the "global temp" prefix to the view name.
Aggregation, a standard Spark SQL process, is generally used to present grouped statistics.
DataFrames come inbuilt with commonly used aggregation functions
such as count, average, max, and others.
You can also perform aggregation programmatically using SQL queries and table views.
First, import your data into a DataFrame.
Then, use pandas on Python to read the CSV file and create a DataFrame.
You can apply the Select function to examine data from a specific column in detail.
This example applies the select function to view the first five rows of the "mpg" column.
Here, you can see the first few rows of the dataset.
In this example, you aggregate and group cars by the number of cylinders they have.
You can perform this action using two methods: The first method is to use the inbuilt
functions of the DataFrame. You have already covered this operation in another lesson.
The second method is to create a temp view for the DataFrame. In this example, you name the temp
view "cars." Then, you run a SQL query to group by cylinders and view the data in descending order.
Although you use different tools and functions, both approaches produce the same results.
Next, let's look at some of the data sources that Spark SQL supports.
Parquet is a columnar format supported by many data processing systems.
Spark SQL supports reading and writing data from Parquet files,
and Spark SQL preserves the data schema.
Similarly, Spark SQL can load and write to JSON datasets by inferring the schema.
Spark SQL also supports reading and writing data stored in Hive.
In this video, you learned that:
Spark modules for structured data processing can run SQL queries on
Spark DataFrames and are usable in Java, Scala, Python, and R.
Spark SQL supports both temporary views and global temporary views.
You can use a DataFrame function or an SQL Query plus Table View for data aggregation.
Spark SQL supports Parquet files, JSON datasets, and Hive tables.