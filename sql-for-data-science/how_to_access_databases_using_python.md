# Concepts of the python DB API

**Connection objects**
Used to connect to the database
Mange transactions
**Cursor objects**
Used to run queries on the database
Scroll through result set
Used to retrieve results

# Connection methods

cursor()
Which return a new cursor object using the connection
commit()
Commit any pending transaction to the database
rollback()
roll back to the start of any pending transaction
close()
close database connection

# Cursor methods

Fetch methods
callproc()
execute()
executemany()
fetchone()
fetchall()