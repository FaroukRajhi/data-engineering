# Aggregate or Column functions

Input: Collection of values (e.g entire column)
Output: Single value

Examples of aggregate functions
SUM(), MIN(), MAX(), AVG(),etc.

SUM(column_name)
MIN(column_name)
MAX(column_name)
AVG(column_name): select AVG(column_name / other_column) from table where column = 'column_name'

# SCALAR and STRING FUNCTIONS

SCALAR: Perform operations on every input value.
Examples: ROUND(), LENGTH(), UCASE(),LCASE()

SELECT ROUND(column_name) from table