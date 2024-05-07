from dbmodule import connect

# Create connection object

Connection = connect('database_name','username','password')

# Create a cursor object

Cursor = Connection.cursor()

# Run queries

Cursor.execute('select * from my_table')
Result = cursor.fetall()

# Free resources
Cursor.close()