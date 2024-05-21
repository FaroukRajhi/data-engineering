Welcome to Key-Value NoSQL Databases This video lists the four main categories
of NoSQL databases available and describes the Key-Value NoSQL database category,
including its architecture and primary use cases. We have already learned that there are four
major categories of NoSQL databases: Key-Value, Document, Column, and Graph.
All have unique characteristics that make them great fits for different
types of applications or parts of applications. So, let’s look at each of these NoSQL database
types in a bit more depth, discussing both the architecture and use cases for each one in turn.
We will start with Key-Value databases. In Key-Value databases, all data is stored
with a key and an associated value blob. They are the least complex of the NoSQL
databases architecturally speaking. Because Key-Value stores are represented
as a hashmap, they're powerful for basic Create-Read-Update-Delete operations,
and Key-Value databases typically scale quite well and shard easily across 'x' number of nodes.
Each shard would contain a range of keys and their associated values.
However, these databases are usually not meant for complex queries attempting to
connect multiple pieces of data, and are atomic for single key operations only.
The value blob is opaque and therefore typically will have less flexibility
when it comes to indexing and querying the data than other database types.
What are some typical use cases for a Key-Value type NoSQL database?
Well, anytime you need quick performance for basic Create-Read-Update-Delete
operations and your data is not interconnected. For example, storing and retrieving session
information for a Web application. Each user session would receive some sort of unique key
and all data would be stored together in the opaque value blob. Plus, there would be no need to
query based on the information in the value blob. All transactions would be based on the unique key.
Similar use cases would be for storing user profiles and preferences within an application
or even storing shopping cart data for online stores or marketplaces.
In these cases, complex queries or handling relationships between
different keys would be few and far between.
Key-Value type NoSQL databases would not be suitable for use
cases that require just the opposite. When your data is interconnected with a
number of many-to-many relationships in the data, such as social networking or
recommendation engine scenarios, a Key-Value NoSQL database is likely to exhibit poor performance.
Also, if your use case requires a high level of consistency for multi-operation transactions,
involving multiple keys, you may want to look more towards databases that provide
Atomicity, Consistency, Isolation, and Durability, (or ACID), transactions.
Lastly, if you expect the need to query based on value versus key,
it may be wise to consider the ‘Document’ category of NoSQL databases, which we will cover shortly.
Some examples of the more popular implementations of key-value NoSQL databases are:
Amazon DynamoDB, Oracle NoSQL Database, Redis, Aerospike, Riak KV, MemcacheDB,
and Project Voldemort. In this video, you learned that:
The four main categories of NoSQL database are Key-Value, Document, Wide Column, and Graph.
Key-Value NoSQL databases are the least complex architecturally speaking;
the data is stored with a key and corresponding value blob and is represented by a hashmap.
The primary use cases for the Key-Value NoSQL database category are for quick CRUD operations;
for example, storing and retrieving session information, storing in-app user profiles,
and storing shopping cart data in online stores.