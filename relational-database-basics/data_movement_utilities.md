Back up and restore

Import : insert data from a file into a table
Export : saves table data into a file

Operations available using different interfaces (CLI, API,GUI,third party tools).

# IMPORT/EXPORT file formats

DEL : Delimited ASCII, for data exchange among a wide variety of databases managers and file managers, includes CSV.
And other

Example:
db2 of IBM command line

db2 import from filename of fileformat message messagesfile into table
db2 export to filename of fileformat messages messagefile select * from table