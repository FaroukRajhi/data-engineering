Task A: Create a database
To get started with this lab, launch PostgreSQL using the Cloud IDE. You can do this by following these steps:

Click the Skills Network extension button on the left side of the window.

Open the DATABASES menu and click PostgreSQL.

Click Start. PostgreSQL may take a few moments to start.

Start PostgreSQL

Open a new command terminal by clicking New Terminal.

Open terminal

Copy the command below by clicking the little copy button on the right of the code block and then paste it into the terminal using Ctrl + V (Mac: ⌘ + V) to fetch the sakila_pgsql_dump.sql file to the Cloud IDE.

1
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/sakila/sakila_pgsql_dump.sql
Copied!
wget

Now, open the PostgreSQL Command Line Interface (CLI) by clicking PostgreSQL CLI.

Open PostgreSQL CLI

Create a new database named sakila using the following command in the terminal:

1
create database sakila;
Copied!
create database sakila;

Note: You are using the create database command to create a new database within the PostgreSQL CLI. To create a new database named sakila outside the command line interface, you can use the following command directly in a terminal window: createdb --username=postgres --host=localhost --password sakila after quitting the psql command prompt session with the command \q.

Task B: Restore the structure and data of a table
To connect to the newly created empty sakila database, use the following command in the terminal and enter your PostgreSQL service session password:

1
\connect sakila;
Copied!
\connect sakila;

Restore the sakila PostgreSQL dump file (containing the sakila database table definitions and data) to the newly created empty sakila database by using the following command in the terminal:

1
\include sakila_pgsql_dump.sql;
Copied!
\include sakila_pgsql_dump.sql;

Note: You are using the \include command to restore the database dump file within the PostgreSQL CLI. To restore the database dump file outside of the Command Line Interface, you can use the command pg_restore --username=postgres --host=localhost --password --dbname=sakila < sakila_pgsql_dump.tar after quitting the CLI prompt session with the command \q. Non-text format .tar dumps are restored using the pg_restore command. So, before using the pg_restore command, first, fetch the .tar version of this dump file using the command wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0110EN-SkillsNetwork/datasets/sakila/sakila_pgsql_dump.tar

Repeat Step 1 to reconnect to the sakila database after restoring the dump file.

Task C: Explore and query tables
To list all the table names from the sakila database, use the following command in the terminal:

1
\dt
Copied!
\dt

Explore the structure of the store table using the following command in the terminal:

1
\d store;
Copied!
\d store;

Retrieve all the records from the store table using the following command in the terminal:

1
SELECT * FROM store;
Copied!
SELECT * FROM store;

Quit the PostgreSQL command prompt session using the following command in the terminal.

1
\q
Copied!
sakila=#

Task D: Dump/backup tables from a database
Finally, to dump/backup the store table from the database, use the following command in the terminal and enter your PostgreSQL service session password:

1
pg_dump --username=postgres --host=localhost --password --dbname=sakila --table=store --format=plain > sakila_store_pgsql_dump.sql
Copied!
Note: To only dump/backup the table store from the database in non-text format .tar, you can use the command pg_dump --username=postgres --host=localhost --password --dbname=sakila --table=store --format=tar > sakila_store_pgsql_dump.tar

To view the dump file within the terminal, use the following command:

1
cat sakila_store_pgsql_dump.sql
Copied!
dumpfile

Conclusion
Congratulations! You have completed this lab, and now you have learned how to create a database, restore the structure and data of a table, explore and query tables, and dump/backup tables from a database.


