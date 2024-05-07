sub-query: Is a query inside (or nested) another query.
Example:
select column1 from table where column2 = (select max(column2 from table).

Lets's we want to retrieve the list of employees who earn more than the average salary:
select * from employees where salary  > AVG(salary)
=> Running this query will result in an error.

We will use sub-select expression:

select EMP_ID, F_NAME, L_NAME, SALARY from employees where salary < 
               (select AVG(salary) from employees)
Called column expression

select EMP_ID, SALARY (select AVG(salary) from employees AS AVG_SALARY from employees))

Called derived tables or table expressions

select * from (select EMP_ID, F_NAME, L_NAME, SALARY from employees) as EMPALL;