A view is an alternative way of representing data from one or more tables or other views.
Can interact with views in the same way as interact with tables.
use to:
-> Limit access to sensitive data
-> Simplify data retrieval
=> Access a portion of table not all all rows and columns.

Creating a view using CLI:

SELECT first_name, last_name, email FROM employee_details INNER JOIN employee_contact_info ON employee_details.empid = employee_contact_info.empid 