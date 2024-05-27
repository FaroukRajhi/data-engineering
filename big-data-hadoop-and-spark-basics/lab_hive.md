# Objectives

At the end of this lab, you will be able to:

Create a table in Hive
Add data to the table using file
Add data to the table using insert
Query the data in the table using SQL commands

# Get a copy of the CSV file

You will run the commands in the terminal. If you don’t have a terminal open, open a new terminal, by clicking on Terminal and choosing New Terminal from the submenu.
Terminal menu with New Terminal highlighted.

Create a directory named data under /home/project by running the following command.
1
mkdir /home/project/data
Copied!
Change to the /home/project/data directory.
1
cd /home/project/data
Copied!
Run the following command to get the emp.csv, a data file with Employee data, in a comma-separated file which you will use later to infuse data into the table you create.
1
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-BD0225EN-SkillsNetwork/data/emp.csv
Copied!

# Setup hive and bee

You will use the hive from the docker hub for this lab. Pull the hive image into your system by running the following command.
1
docker pull apache/hive:4.0.0-alpha-1
Copied!Executed!
This will take a few seconds, depending on the speed of your internet connection.

Now, you will run the hive server on port 10002. You will name the server instance myhiveserver. We will mount the local data folder in the hive server as hive_custom_data. This would mean that the whole data folder that you created locally, along with anything you add in the data folder, is copied into the container under the directory hive_custom_data.
1
docker run -d -p 10000:10000 -p 10002:10002 --env SERVICE_NAME=hiveserver2 -v /home/project/data:/hive_custom_data --name myhiveserver apache/hive:4.0.0-alpha-1
Copied!Executed!
You can open and take a look at the Hive server with the GUI. Click the button to open the HiveServer2 GUI.
 HiveServer2 GUI

Now run the following command, which allows you to access beeline. This is a SQL cli where you can create, modify, delete table, and access data in the table.
1
docker exec -it myhiveserver beeline -u 'jdbc:hive2://localhost:10000/'

# Create table, add an view data

To create a new table Employee with three columns as in the csv you downloaded - em_id, emp_name and salary, run the following command.
1
create table Employee(emp_id string, emp_name string, salary  int)  row format delimited fields terminated by ',' ;
Copied!
You may notice that there is an explicit mention for the fields delimited by , just as in the csv file.

Run the following command to check if the table is created.
1
show tables;
Copied!
This should list the Employee table that you just created.

Now load the data into the table from the csv file by running the following command.
1
LOAD DATA INPATH '/hive_custom_data/emp.csv' INTO TABLE Employee;
Copied!
Run the following command to list all the rows from the table to check if the data has been loaded from the CSV.
1
SELECT * FROM employee;
Copied!
You can view the details of the commands and the outcome in the HiveServer2 GUI.
 HiveServer2 GUI

To quit from the beehive prompt in the terminal, press ctrl+D.
Hive internally uses MapReduce to process and analyze data. When you execute a Hive query, it generates MapReduce jobs that run on the Hadoop cluster.


