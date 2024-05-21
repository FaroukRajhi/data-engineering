Welcome to Introduction to the Cassandra Query Language Shell
After watching this video, you will be able to: Describe the Cassandra Query Language.
Explain the different options for running CQL queries.
Describe the CQL Shell. Use some of the key command-line
options for the CQL shell. Describe the special commands
available for the CQL shell. Cassandra Query Language,
referred to as CQL, is the primary language for communicating with Apache Cassandra clusters.
CQL has a simple and intuitive, SQL-like syntax that allows the creation of keyspaces, tables,
inserts, updates, deletes, and select queries. While CQL syntax has similarities to SQL,
there are many differences as well between what you can do in CQL vs. SQL. One of the most notable
differences is that CQL does not support JOIN statements. In Cassandra, if you need a join,
then you store the data already joined. Also, although, syntax-wise, some operations
seem similar to SQL, their behavior in Cassandra is different; for example, inserts, updates,
and deletes are done in memory directly, without prior reads to locate the data.
You will see, as you go through the lab exercises, that CQL keywords are case insensitive.
Identifiers are also case insensitive, unless they are enclosed in double quotation marks.
For example, ‘Select’ in sentence case, and ‘SELECT’ in uppercase are treated the same.
If you enter names for identifiers, for example a table name, using uppercase letters, Cassandra
will just store the names in lowercase anyway. As you can see in the examples, commented text,
denoted by a double forward slash, will be ignored by CQL.
To run CQL queries, you can do one of the following:
Run them programmatically using a licensed Cassandra client
driver. There are many options available, including Java, Python,
and Scala. The default driver is the open source Datastax Java Driver.
Alternatively, you can run them on the CQL Shell client (referred to as ‘cqlsh’)
that is provided with the Cassandra package. CQLSH is a python-based command line shell that uses CQL
for communicating with a Cassandra cluster. The software is shipped with every Cassandra package.
CQLSH connects to a single node – either the one that the command is run on (default), or the one
specified as an option in the command line. There are also other CQL editors on the market
that communicate with Cassandra using CQL. Using CQL shell you can:
Create, alter, and drop keyspaces Create, alter, and drop tables
Insert, update, and delete data Execute queries using SELECT
But before we look at some cqlsh examples, when launching cqlsh, there are a number of
command line options you should know about. Let’s just mention a few of them here:
help – shows help about the options of CQLSH commands
version – in order to check the cqlsh version being used
user and password – for authentication keyspace – keyspace to authenticate to
file – enables execution of commands from a given file
request timeout – you can set a timeout for your queries; the default being 10 seconds
Let’s see the cqlsh output for a simple example: Here we're just using the ‘intro_cassandra’
keyspace, and we select only the users from groupid 12. Then we insert a new record
into the groups table for groupid 12, and finally select only the users from groupid 12,
and also view the inserted data. And this would be the resulting output.
CQLSH also has some special commands, so let’s take a quick look at some of them:
CAPTURE − Captures the output of a command and adds it to a file.
CONSISTENCY − Shows the current consistency level and sets a new one.
COPY − Copies data to and from Cassandra. DESCRIBE − Describes the current cluster
of Cassandra and its objects. EXIT − Terminates the cqlsh session.
PAGING − Enables or disables the paging of query results.
TRACING − Enables or disables request tracing.
While in your hands-on sessions you will get to experience
some of these. We will now look in a bit more detail at the CONSISTENCY and COPY commands.
Let’s take a detailed look at the CONSISTENCY command.
Cassandra is tunable consistent. But what does this mean? Well,
it means you have the ability to set Cassandra consistency at an operations level. Consistency
in Cassandra means the number of nodes (out of the total replicas) that need to answer a request
(write/read) in order for the operation to be considered successful.
Amongst the options available for the Consistency command are: ONE, TWO, or THREE nodes,
QUORUM — which is a majority of nodes out of all replicas in the cluster,
ALL replicas, and finally LOCAL_QUORUM — which is a majority of nodes from the local data center
(according to the specified data center set replication for the keyspace).
So, for example, if we have a Cassandra cluster of 8 nodes and 2 Data Centers,
one data center with replication factor 2 and the other one with replication
factor 3, then overall, replication is 5. If we set CONSISTENCY QUORUM on a write operation:
first of all, QUORUM means a majority of nodes out of the replicas, so a majority here would be 3
Write operations will go to all 5 replicas but a minimum 3 nodes (from both data centers)
out of the 5 replicas need to answer in order for the operation to be successful.
Another important command in cqlsh is the COPY command.
While bulk copy in Cassandra should be done through special procedures, if you would like
to just test your model or you're working with a smaller, text delimited dataset, then you can
use COPY FROM or COPY TO operations to bring data in, and export data out, of Cassandra.
COPY TO exports data from a table into a CSV file. Each row is written to a line in the target file
with fields separated by the delimiter. COPY FROM imports data from a
CSV file into an existing table. Each line in the source file is imported as a row.
All rows in the dataset must contain the same number of fields and have
values in the PRIMARY KEY fields. The process verifies the PRIMARY
KEY and imports data accordingly. In this video, you learned that:
CQL is the primary language for communicating with Apache Cassandra clusters.
CQL keywords and identifiers are case-insensitive. CQL queries can be run programmatically using
a licensed Cassandra client driver, or they can be run on the Python-based CQL
shell client provided with Cassandra. Using the CQL shell, you can create, alter,
and drop keyspaces and tables, insert, update, and delete data, and execute queries using SELECT.
CQL shell has several special commands including the CONSISTENCY and COPY commands.
The CONSISTENCY command can be used to tune the consistency of your data.
The COPY command can be used to import data into, and export data out of, Cassandra.