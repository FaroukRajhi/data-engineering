# Database management system (DBMS) Provides:

Efficient, reliable, convenient, and safe multi-user storage of and access to massive amounts of persistent data.

Massive: terabytes
Persistent: the data in the database is not ephemeral.
Safe: guarantees that the data state does not change. Hardware, software, power, users
Multi-user: Multiples users works on same database: Concurrency control, nut the operating on different individual data items.
Convenient: Physical data independence, High-level query languages declarative.
Efficient: Thousands of queries/updates per second.
Reliability: 99.9999% uptime, is the type of guarantee that the database management system are making for their applications.

# Key concepts

* Data model: Is a description of, in general, how the data is structured (set of records, XML documents captures data, graph).
* Scheme versus data: 
  - Schema is like types and data like variables in programming language.
  - The schema sets the structure of the database, where the data is the actual data stored within the schema.
* Data definition language (DDL): Used in general to set up a schema or structure for a particular database.
* Data manipulation or query language (DML): Start querying and modifying the database.

# Key people

* DBMS implementer: The person who builds the system.
* Database designer: The person who establishes the schema for a database.
* Database application developer: Programs that operate on the database.
* Database administrator: The person who loads the data, sort of gets the whole thing running and keeps it running smoothly.