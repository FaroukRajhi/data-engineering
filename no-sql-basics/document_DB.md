Welcome to Document-Based NoSQL Databases This video describes the document-based NoSQL
database category, including its architecture and primary use cases.
Document databases build off the Key-Value model by making the value visible and able
to be queried.
Each piece of data is considered a document and typically stored in either JSON or XML
format.
One of the benefits of document databases is that each document truly offers a flexible
schema, where no two documents need to be the same or contain the same information.
Document databases typically offer the ability to index and query the contents of the documents,
offering key and value range lookups and search ability, or perhaps analytical queries via
paradigms like MapReduce.
Document databases are horizontally scalable and allow for sharding across multiple nodes,
typically sharded by some unique key in the document.
Document stores also typically only guarantee atomic transactions on single document operations.
What are some use cases for a document type NoSQL database?
The first example would be for event logging for an application or process.
Each instance would constitute a new document or aggregate, containing all of the information
corresponding to the event.
Another use case would be online blogging.
Each user would be represented as a document; each post a document; and each comment, like,
or action would be a document.
All documents would contain information pertaining to the type of data, such as username, post
content, or timestamp when the document was created.
More generally speaking, document stores work well with operational datasets for Web and
mobile applications.
They were designed with the internet in mind – thinking JSON, RESTful API, and unstructured
data.
Document type NoSQL databases would not be suitable for use cases that require ACID transactions.
It's not possible for a document store to handle a transaction that operates over multiple
documents and a relational database may be a better choice in this instance.
Secondly, document databases may not be the right choice if you find yourself forcing
your data into an aggregate-oriented design.
If it naturally falls into a normalized/tabular model, this would be another time to research
relational databases instead.
Document databases are currently the most widespread of the NoSQL database categories
in use today, and some examples of the more popular implementations of document NoSQL
databases are: IBM Cloudant, MongoDB, Apache CouchDB, Terrastore,
OrientDB, Couchbase, and RavenDB In this video, you learned that:
Document-based NoSQL databases use documents to make values visible and able to be queried.
Each piece of data is considered a document and typically stored in either JSON or XML
format.
Each document offers a flexible schema.
The primary use cases for document-based NoSQL databases are event logging for apps and processes,
online blogging, and operational datasets or metadata for web and mobile apps.