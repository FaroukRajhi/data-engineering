Backup using mysqldump utility:

mysqldump -u root > backup.sql

Restore

mysql  -u root restored employees < backup.sql

Importing data files

Importing using load data infile statements:
load data infile 'file.csv' into table <table_name>
or
mysqlimport <database> file.csn