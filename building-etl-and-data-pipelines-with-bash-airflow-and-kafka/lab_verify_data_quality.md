# Getting the testing framework ready

You can perform most of the data quality checks by manually running sql queries on the data warehouse.

It is a good idea to automate these checks using custom programs or tools. Automation helps you to easily

create new tests,
run tests,
and schedule tests.
We will be using a python based framework to run the data quality tests.

Step 1: Download the framework.

Run the commands below to download the framework

1
2
3
4
5
6
7
8
9
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Verifying%20Data%20Quality%20for%20a%20Data%20Warehouse/dataqualitychecks.py
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Verifying%20Data%20Quality%20for%20a%20Data%20Warehouse/dbconnect.py
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Verifying%20Data%20Quality%20for%20a%20Data%20Warehouse/mytests.py
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Verifying%20Data%20Quality%20for%20a%20Data%20Warehouse/generate-data-quality-report.py
ls
Copied!Executed!
Step 2: Install the python driver for Postgresql.

Run the command below to install the python driver for Postgresql database

1
python3 -m pip install psycopg2
Copied!Executed!
Step 3: Test database connectivity.

Now we need to check

if the Postgresql python driver is installed properly.
if Postgresql server is up and running.
if our micro framework can connect to the database.
The command below to check all the above cases.

1
python3 dbconnect.py
Copied!Executed!
If all goes well, you should a message Successfully connected to database.

The command also disconnects from the server with a message Connection closed.

# Create a sample data quality report

Run the command below to install pandas.

1
python3 -m pip install pandas tabulate
Copied!Executed!
Run the command below to generate a sample data quality report.

1
python3 generate-data-quality-report.py
Copied!Executed!
You should see a list of tests that were run and their status.

Previous

# Explore the data quality tests

The file mytests.py contains all the data quality tests.

It provides a quick and easy way to author and run new data quality tests.

The testing framework provides the following tests:

check_for_nulls - this test will check for nulls in a column
check_for_min_max - this test will check if the values in a column are with a range of min and max values
check_for_valid_values - this test will check for any invalid values in a column
check_for_duplicates - this test will check for duplicates in a column
Each test can be authored by mentioning a minimum of 4 parameters.

testname - The human readable name of the test for reporting purposes
test - The actual test name that the testing micro framework provides
table - The table name on which the test is to be performed
column - The table name on which the test is to be performed

