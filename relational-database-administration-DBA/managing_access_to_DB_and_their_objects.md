- Database access

GRANT CONNECT TO 'username or group_name'

- Table access

GRANT SELECT ON mydb.mytable TO 'username'
GRANT INSERT ON mydb.mytable TO 'username'
GRANT UPDATE ON mydb.mytable TO 'username'
GRANT DELETE ON mydb.mytable TO 'username'

- Object definition access

GRANT CREATE TABLE TO 'username or group_name'
GRANT CREATE PROCEDURE TO 'username or group_name'

- Object access

GRANT VIEW ON mydb.mytable TO 'username'
GRANT EXECUTE ON mydb.mytable TO 'username'
GRANT ALTER ON mydb.mytable TO 'username'

- Revoke and deny access

GRANT VS revoke