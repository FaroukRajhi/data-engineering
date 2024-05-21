Welcome to Column-Based NoSQL Databases This video describes the column-based
NoSQL database category, including its architecture and primary use cases.
Column-based databases spawned from an architecture that Google created called Bigtable.
These databases are therefore also commonly referred to as Bigtable clones,
or Columnar databases, or Wide-Column databases.
As you can tell from the name, these databases focus on columns and groups of
columns when storing and accessing data. Column ‘Families’ are several rows,
each with a unique key or identifier, that belong to one or more columns.
These columns are grouped together in families because they are often accessed together.
It's also important to point out that rows in a column family are not required to share
any of the same columns. They can share all,
a subset, or none of the columns and columns can be added to any number of rows and not to others.
Let’s look at some typical use cases for a Column-based NoSQL database.
Column-based databases are great for when you're dealing with
large amounts of sparse data. When compared to row-oriented databases, Column-based databases
can better compress data and save storage space. In addition, these databases continue the trend
of horizontal scalability. As with Key-Value and Document databases, Column-based databases can
handle being deployed across clusters of nodes. Similar to document databases, a Column-based No
SQL database could be used for event logging and blogs, but the data would be stored in a different
fashion. For enterprise logging, every application can write to its own set of columns and have
each row key formatted in such a way to promote easy lookup based on application and timestamp.
Counters are a unique use case for Column-based databases. You may come across applications that
need an easy way to count or increment as events occur. Some Column-based databases,
like Cassandra, have special column types that allow for simple counters.
In addition, columns can have a time-to-live parameter,
making them useful for data with an expiration date or time, like trial periods or ad timing.
On the other hand, Column-based databases should be avoided if you require
traditional ACID transactions provided by relational databases.
Reads and writes are only atomic at the row level. And, early into development, query patterns
may change and require numerous changes to the column-based designs.
This can be costly and slow down the production timeline.
Some examples of the more popular implementations of Column-based NoSQL databases are:
Cassandra, HBASE, Hypertable, and accumulo. In this video, you learned that:
Column-based databases spawned from the architecture of Google’s Bigtable storage system.
Column-based databases store data in columns or groups of columns.
Column ‘families’ are several rows, with unique keys, belonging to one or more columns.
The primary use cases for Column-based NoSQL databases are
event logging and blogs, counters, data with expiration values.