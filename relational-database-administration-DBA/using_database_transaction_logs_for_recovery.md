Transactions logs used to keep track of all transactions that change or modify the database.

# Storing transaction log files

The information stored in these transaction logs can be used for recovery purposes.
Logs file stored in path directory
Isolate logs on different volumes from data.
Log mirroring - store second copy of log files in alternative location.
Log shipping - copy and send logs to replica or standby servers.

# Accessing transaction log files

Logging may or may not be enabled by default
Log settings are usually configurable

See transaction log in MYSQl: SHOW BINARY LOGS.
Typically in binary format