Is a collection of multiple interconnected databases.
Spread physically across various locations
Fragmentation (Partitioning , sharding) and replication.

# Distributed Databases challenges

Bring availability, fast scaling, and global reach capabilities.
Concurrency control => consistency of data:
WRITE/READ to single node per fragment of data => data is synchronized in the background.
WRITE operations go to all nodes holding a fragment of data, READ to a subset of nodes per consistency.
