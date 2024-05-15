- Full loading
Loading data in one large batch
Used when organizations want to start tracking transactions in new data warehouse.
Used for porting over transactions history.

- Incremental loading
Data is appended to, not overwritten.

- Scheduled loading
Periodic loading, like daily transactions to database
Task, cron

- On demand loading
Triggered by:
Measures such as data size
Event detection, like motion, sound, or temperature change.

- Batch and stream
Batch: periodic updates using windows of data
Stream  : continuous updates as data arrives

- Push and pull
Client-server model:
Pull - requests for data originate from the client
Push - Server pushes data to clients (Push notifications)

- Parallel loading

Multiple data streams to boost loading efficiency
File partitioning