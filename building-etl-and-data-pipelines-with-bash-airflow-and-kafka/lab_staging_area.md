# Create Database

Create the database on the data warehouse.

Using the createdb command of the PostgreSQL server, we can directly create the database from the terminal.

Run the command below to create a database named billingDW.

1
createdb -h localhost -U postgres -p 5432 billingDW
Copied!Executed!
In the above command

-h mentions that the database server is running on the localhost
-U mentions that we are using the user name postgres to log into the database
-p mentions that the database server is running on port number 5432

# Create data warehouse

Step 1:
Download the schema files.

The commands to create the schema are available in the file below.

https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Setting%20up%20a%20staging%20area/billing-datawarehouse.tgz
Run the commands below to download and extract the schema files.

1
2
3
4
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Setting%20up%20a%20staging%20area/billing-datawarehouse.tgz
tar -xvzf billing-datawarehouse.tgz
ls *.sql
Copied!Executed!
You should see 4 .sql files listed in the output

Step 2: Create the schema

Run the command below to create the schema in the billingDW database.

1
psql  -h localhost -U postgres -p 5432 billingDW < star-schema.sql
Copied!Executed!
You should see an output similar to the one below.

# Load data into dimension tables

When we load data into the tables, it is a good practice to load the data into dimension tables first.

Step 1: Load data into DimCustomer table

Run the command below to load the data into DimCustomer table in billingDW database.

1
psql  -h localhost -U postgres -p 5432 billingDW < DimCustomer.sql
Copied!Executed!
Step 2: Load data into DimMonth table

Run the command below to load the data into DimMonth table in billingDW database.

1
psql  -h localhost -U postgres -p 5432 billingDW < DimMonth.sql


# Load data into fact table

Load data into FactBilling table

Run the command below to load the data into FactBilling table in billingDW database.

1
psql  -h localhost -U postgres -p 5432 billingDW < FactBilling.sql


# Run a sample query 

Run the command below to check the number of rows in all the tables in the billingDW database.

1
psql  -h localhost -U postgres -p 5432 billingDW < verify.sql
Copied!Executed!
You should see an output similar to the one below.

Screenshot of output

Your data warehouse staging area is now ready.

