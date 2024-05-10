Types od database indexes

- primary key
Always unique, non-nullable, one per table
Clustered - data stored in table in order by primary key

- indexes
Non-clustered , single or multiple columns.
Unique or non-unique.

- column ordering is important
ascending or descending order

Check out the best practices to create index

**Creating indexes**

CREATE INDEX index_name ON table_name (column_name_1, column_name_2,...)

Unique index

CREATE UNIQUE INDEX index_name ON table_name (column_name)

**Dropping indexes**

DROP INDEX index_name;

Primary key / unique key indexes cannot be explicitly dropped using this method.
=> use ALTER TABLE statement instead.


# Considerations when creating indexes

Major source of database bottlenecks is poorly designed or insufficient indexes.
Storage requirements
