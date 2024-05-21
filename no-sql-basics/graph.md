Welcome to Graph NoSQL Databases This video describes the Graph NoSQL database
category, including its architecture and primary use cases.
Graph databases, are the last NoSQL category variation we will discuss.
This database category stands apart from the previous three types covered because it doesn't
follow a few of the common traits previously seen.
From a high level, graph databases store information in entities (or nodes), and relationships
(or edges).
Graph databases are impressive when your data set resembles a graph-like data structure.
Traversing all of the relationships is quick and efficient, but these databases tend not
to scale as well horizontally.
Sharding a graph database is not recommended since traversing a graph with nodes split
across multiple servers can become difficult and hurt performance.
Graph databases are also ACID transaction compliant, very much unlike the other NoSQL
databases previously discussed.
This prevents any dangling relationships between nodes that don't exist.
Now let’s look at some typical use cases for a Graph NoSQL database.
Graph databases can be very powerful when your data is highly connected and related
in some way.
Social networking sites can benefit by quickly locating friends, friends of friends, likes,
and so on.
And routing, spatial, and map applications may use graphs to easily model their data
for finding close locations or building shortest routes for directions.
Lastly, recommendation engines can leverage the close relationships and links between
products to easily provide other options to their customers.
As far as unsuitable use cases for a Graph database is concerned.
Graph databases are not a good fit when you're looking for some of the advantages offered
by the other NoSQL database categories.
When an application needs to scale horizontally, you're going to quickly reach the limitations
associated with these types of data stores.
Another general negative surfaces when trying to update all or a subset of nodes with a
given parameter.
These types of operations can prove to be difficult and non-trivial.
Some examples of the more popular implementations of Graph NoSQL databases are:
Neo4j, OrientDB, ArangoDB, Amazon Neptune (part of Amazon Web Services), Apache Giraph,
and JanusGraph In this video, you learned that:
Graph databases store information in entities (or nodes), and relationships (or edges).
Graph databases are impressive when your data set resembles a graph-like data structure.
Graph databases do not shard well but are ACID transaction compliant.
The primary use cases for the Graph NoSQL database category are for highly connected
and related data, for social networking sites, for routing, spatial and map applications,
and for recommendation engines.