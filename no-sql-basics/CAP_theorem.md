Welcome to CAP Theorem. After watching this video, you will be able to:
Define the CAP theorem, describe the characteristics of CAP theorem, and
describe the history and the relevance of CAP theorem.
In the early 2000s big data Hadoop architecture was being created as the first open source,
distributed architecture that can store and process high volumes of data. At this time,
more and more services were developed that required databases to be distributed as well.
Actually, these businesses required not only that their services were active
and accessible in most parts of the world, but also that their services were always available.
For relational databases that rely so much on the consistency of data,
the new concept of availability while having a distributed system seemed impossible,
and this was proven by the CAP Theorem. The CAP Theorem is also called Brewer’s Theorem,
because it was first advanced by Professor Eric A. Brewer during a talk he gave on
distributed computing in the year 2000. Two years later it was revised by MIT
professors Seth Gilbert and Nancy Lynch, and there have been many other contributors since.
The theorem states that there are three essential system requirements necessary for the successful
design, implementation, and deployment of applications in distributed systems. These
are Consistency, Availability, and Partition Tolerance, or CAP.
A distributed system can guarantee delivery of only two of these three desired characteristics.
Now let's see what these three characteristics mean.
Consistency refers to whether a system operates fully or not. Do all nodes within a cluster
see all the data they are supposed to? Availability means just as it sounds.
Does each request get a response outside of failure or success?
Partition Tolerance represents the fact that a given system continues to operate even under
circumstances of data loss or network failure. While consistency and availability seem
straightforward, let’s see what partition tolerance refers to.
A partition is a communications break within a distributed system—a lost or temporarily
delayed connection between nodes. Partition tolerance means that the
cluster must continue to work despite any number of communication breakdowns
between nodes in the system. In distributed systems,
partitions can’t be avoided. Therefore, partition tolerance
becomes a basic feature of native distributed systems such as NoSQL.
In a cluster with eight distributed nodes, a network partition could occur, and communication
will be broken between all the nodes. In our case, instead of one 8-node
cluster we will have two smaller 4-node clusters available. Consistency between
the two clusters will be achieved when network communication is re-established.
Partition tolerance has become more of a necessity than an option in distributed systems. It is made
possible by sufficiently replicating records across combinations of nodes and networks.
For such systems as NoSQL, since partition tolerance is mandatory, a system can
be either Consistent and Partition Tolerant (CP) or Available and Partition Tolerant (AP).
Existing NoSQL systems, like MongoDB or Cassandra, can be classified using CAP Theorem. For example,
MongoDB chooses consistency as the primary design driver of the solution,
and Apache Cassandra chooses availability. This doesn't mean that MongoDB cannot be
available, or that Cassandra cannot become fully consistent. It means that these solutions first
ensure that they are consistent (in the case of MongoDB) or available (in the case
of Cassandra) and the rest is tunable. In this video you have learned that:
CAP theorem can be used to classify NoSQL databases.
NoSQL databases choose between availability and consistency.
Partition Tolerance is a basic feature of NoSQL databases.