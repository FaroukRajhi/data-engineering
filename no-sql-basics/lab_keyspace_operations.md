# Create key space

The below command creates a keyspace called training, using SimpleStrategy and a replication_factor of 3.

SimpleStrategy is used when all the nodes in your cassandra cluster exist in a single data center.

On cqlsh run the below command.


CREATE KEYSPACE training  
WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};
Copied!
List all keyspaces.


describe keyspaces

# Describe keyspaces

In the previous exercise you have created a keyspace named training.
Let us print more details of it using the describe command.

Describe a keyspace.



describe training

# Alter a keyspace

In a previous exercise, you created a keyspace named training using SimpleStrategy.
Let's change that to use NetworkTopologyStrategy.

NetworkTopologyStrategy is used when all the nodes in your cassandra cluster are spread across multiple data centers.

Alter a keyspace.

1
2
ALTER KEYSPACE training
WITH replication = {'class': 'NetworkTopologyStrategy'};
Copied!
Verify the changes using the describe command.

1
describe training

# Drop a keypace

To use a keyspace run the below command.

1
use training;
Copied!
List all tables in this keyspace.

1
describe tables

