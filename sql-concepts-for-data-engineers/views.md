Is an alternative way of representing data that exists in one or more tables or views.

view statement

CREATE VIEW <view name> (column_alias_1, column_alias_2, ..) FROM <table_name> WHERE <predicate>

Example

CREATE VIEW EMPINFO (EMP_ID,FIRST_NAME, LAST_NAME, ADDRESS, JOB_ID),MANAGER_ID, DEP_ID AS SELECT column_1, column_2 FROM EMPLOYEES


SELECT * FROM EMPINFO