Welcome to Replication & Sharding. Replication and Sharding are very important concepts in MongoDB.
The scale and availability we see with MongoDB is achieved using these two concepts.
After watching this video, you will be able to: Describe what replication is,
Explain how it helps with high availability, And explain how sharding helps to scale a database
A typical MongoDB cluster is made of three data bearing nodes. All three nodes have the
same data, hence the name ‘replica set’. Data is written to the Primary node.
Which then gets replicated to the Secondary nodes.
Having multiple copies of the data by the means of replication creates redundancy,
so that if one piece of server hardware fails, you still have multiple copies of the data present.
This provides you with a highly available database during such failures or during
periods of planned maintenance. Such planned maintenance should be
done in a rolling fashion, taking one node out for operating system, security, hardware, or
software updates, or for upgrading MongoDB itself. A common misconception about replication is that
it can save you from disasters, such as accidently deleting your database. Since it is a replica set,
what happens on the Primary will be replicated over to the Secondaries.
For disaster recovery scenarios, we rely on backups and restores.
After using MongoDB for some time, you will probably outgrow your hardware. For example,
you need to store even more data, or you want to improve on your read and write performance.
Naturally, you will invest in bigger and faster hardware to increase capacity,
But sometimes that is not feasible. In those situations, you can scale
horizontally by implementing Sharding, Which is the partitioning of your
biggest collections. Sharding your biggest or
most demanding collections has many benefits. When you partition your data across shards,
you increase your throughput by directing your queries only to relevant shards.
You are also then able to store more data, which previously you couldn’t fit on a single node.
You can also split data across shards based on regions
So, data for US customers will only live on shards running in the US, while European customers have
their data on European-based shards. As a global application, you get one
view of your database to manage. In this video, you learned that:
Replication is duplication of data and any changes made to the data.
Replication provides fault tolerance, redundancy, and high availability for your data.
Replication will not prevent a disaster such as the deletion of documents,
collections, or even databases. For those human errors, we have backups.
For growing data sets, you can use Sharding to scale horizontally.