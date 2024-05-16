# Loading frequency

Populating the warehouse is an ongoing process:
- Initial load + periodic incremental loads
- Full refreshes due to schema changes or catastrophic failure are rare.
- Facts tables need more frequent updating than dimension tables

# Typical ways of loading data

Many tools can help you automate the ongoing loading process

Db2
You can automate loading as part of your ETL pipeline using tools like Apache Airflow and kafka
You can use tools like bash, Python, and SQL, to build your data pipeline and schedule it with cron.
InfoSphere

Welcome to “Populating a Data Warehouse.”
After watching this video, you will be able to:
Describe populating a data warehouse as an ongoing process.
List the main steps for populating a data warehouse.
List methods for change detection and incremental loading.
Manually create and populate tables for a sales star schema.
Recall the periodic maintenance required to keep your data warehouse running smoothly.
Populating the enterprise data warehouse is an ongoing process.
You have an initial load followed by periodic incremental loads. For example, you may load
new data every day or every week.
Rarely, a full refresh may be required in case of major schema changes or catastrophic
failures.
Generally, fact tables are dynamic and require frequent updating while dimension tables don’t
change often.
For example, lists of cities or stores are quite static, but sales happen every day.
Many tools are available to automate the ongoing process of keeping your data warehouse current.
Databases like Db2 have a Load utility that is faster than inserting a row at a time,
and
loading your Warehouse can also be a part of your ETL data pipeline that is automated
using tools like Apache Airflow and Apache Kafka.
You can also write your own scripts, combining lower-level tools like Bash, Python, and SQL,
to build your data pipeline and schedule it with cron.
And InfoSphere DataStage allows you to compile and run jobs to load your data.
Before populating your data warehouse, ensure that:
Your schema has already been modeled.
Your data has been staged in tables or files.
And, you have mechanisms for verifying the data quality.
Now you are ready to set up your data warehouse and implement the initial load.
You first instantiate the data warehouse and its schema, then create the production tables.
Next, establish relationships between your fact and dimension tables,
and finally, load your transformed and cleaned data into them from your staging tables or
files.
Now that you’ve gone through the initial load, it’s time to set up ongoing data loads.
You can automate subsequent incremental loads using a script as part of your ETL data pipeline.
You can also schedule your incremental loads to occur daily or weekly, depending on your
needs.
You will also need to include some logic to determine what data is new or updated in your
staging area.
Normally, you detect changes in the source system itself.
Many relational database management systems have mechanisms for identifying any new, changed,
or deleted records since a given date.
You might also have access to timestamps that identify both when the data was first written
and the date it might have been modified.
Some systems might be less accommodating and you might need to load the entire source
to your ETL pipeline for subsequent brute-force comparison to the target, which is fine if
the source data isn’t too large.
Data warehouses need periodic maintenance, usually monthly or yearly, to archive data
that is not likely to be used.
You can script both the deletion of older data and its archiving to slower, less costly
storage.
Let’s illustrate the process with a simplified example of manually populating a data warehouse
with a star schema called ‘sales.’ We’ll assume that you’ve already instantiated
the data warehouse and the ‘sales’ schema.
Here’s a sample of some auto sales transaction data from a fictional company called Shiny
Auto Sales.
You can see several foreign key columns, such as
“sales ID,” which is a sequential key identifying the sales invoice number,
“emp no,” which is the employee number, and
“class ID,” which encodes the type of car sold, such as “small SUV.”
Each of these keys represents a dimension that points to a corresponding dimension table
in the star schema.
The “date” column is a dimension that indicates the sale date.
The “amount” column is the sales amount, which happens to be the fact of interest.
This table is already close to the form of a fact table. The only exception is the date
column, which is not yet represented by a foreign “date ID” key.
Let’s use PSQL, the terminal-based front end for PostGreSQL, to illustrate how you
can create your dimension tables using the salesperson dimension as an example.
Use the CREATE TABLE clause to create the “DimSalesPerson” table with the “sales”
schema, along with
“SalesPersonID” as a serial primary key,
“SalespersonAltID”, as the salesperson’s employee number,
and finally, a column for the salesperson’s name.
Now you can start populating the “DimSalesPerson” table, row by row.
You use an “insert into” clause on the “sales dot DimSalesPerson” table,
specifying the “SalesPersonAltID” and “SalesPersonName” columns,
and begin inserting values such as employee number 680, “Cadillac Jack.”
You would similarly create and populate tables for the remaining dimensions.
You can enter the SQL statement:
“SELECT star FROM sales dot dim salesperson LIMIT 5” to view your salesperson dimension
table,
and see that everything seems to be correctly populated, such as record 1, employee number
617, and salesperson name “Go-cart Joe.”
Now it’s time to create your sales fact table, using “CREATE TABLE” with “sales
dot FactAutoSales” as the table name,
“TransactionID“ as the primary key, with “big serial” type and the various
foreign keys, such as “SalesID” and “AutoClassID”,
and finally the fact of interest, “amount” as type “money.”
Next, you proceed with setting up the relations between the fact and dimension tables of the
sales schema.
For example, you can apply the ALTER TABLE statement and the ADD CONSTRAINT clause to
the “sales dot FactAutoSales” fact table to add “KVAutoClassID” as a foreign key relating
“AutoClassID” to the same column name in the “sales dot DimAutoCategory” table
using the REFERENCES clause.
You would then use the same method to set up the relations for the remaining dimension
tables.
After defining all the tables and setting up the corresponding relations, it’s finally
time to start populating your fact table using the sales data that you started with.
You can use the INSERT INTO statement on “sales dot FactAutoSales,” specifying the column
names “SalesID,” "Amount," “SalesPersonID,” “AutoClassID,” and “SalesDateKey,” and entering rows
of values such as 1629, 42000, 2, 1, and 4, which you would obtain using the auto sales
data.
You can view the auto sales fact table by entering the SQL statement “select star"
from “sales dot FactAutoSales Limit 5” to display its first 5 rows.
Here you see the dollar amounts for individual auto sales, the primary key called “transactionID,”
and the remaining columns, which are the foreign keys that you set up.
In this video, you learned that:
Populating an enterprise data warehouse includes initial creation of fact and dimension tables
and their relations and loading of clean data into tables.
Populating the enterprise data warehouse is an ongoing process that starts with an initial
load, followed by periodic incremental loads.
Fact tables are dynamic and require frequent updating while dimension tables are more static
and don’t change often.
And you can automate incremental loading and periodic maintenance of your data warehouse
using scripting or built-for-purpose data pipeline tools.