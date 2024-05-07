There are several ways to access multiple tables in the same query:
- Sub-queries:
select * from employees where DEP_ID IN (select DEP_ID from departments)
- Implicit JOIN:
Specify 2 tables in the FROM clause:
select * from table_1, table_2.
Use additional operands to limit the result set:
select * from employees, departments where employeeS.DEP_ID = departments.DEP_ID_DEP
- JOIN operators (INNER JOIN, OUTER JOIN, and so on).
