**COUNT**

Retrieve the number of rows that match the query criteria.
For example, get the total number of rows in a given table.
SELECT COUNT(*) FROM <table_name>
or
SELECT COUNT(<specified_columns>) FROM <table_name>

**DISTINCT**

Is used to removes duplicate values from a result set.
Example:

To retrieve a unique values in a column:
SELECT DISTINCT <column_name> from <table_name>

Or 
List of unique countries that received GOLD metals:

SELECT DISTINCT <column_name> FROM <table_name> where <column_name> = 'value'

**LIMIT**

Restricting the number of rows retrieved from the database.
Example:

Retrieve just the first 10 rows in a table:

SELECT * FROM <table_name> LIMIT 10

Other example:

Retrieve 5 rows in the table for a particular year:

SELECT * FROM <table_name> where YEAR = 2024 LIMIT 5