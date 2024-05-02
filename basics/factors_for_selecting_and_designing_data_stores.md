A data store or data repository, refers to data that has been collected, organized, and isolated so that it can be:
Reporting and data analysis.
Used for business operations.
A repository can be data lake, data warehouse, or data mart, big data stores.

# Primary considerations for designing a data store

- Volume of data or scale of data.
- Type of data
- Intended use of data: include number of transactions, Frequency of updates, Types of operations, Response Time, and backup and recovery.
-> Transactional systems: Used for capturing high-volume transactions, need to be designed for high-speed read, write and update operations
-> Analytical systems: needs complex queries to be applied to large amounts of historical data aggregated from transactional systems. They need faster response times to complex queries.
-> Schema design, indexing, and partitioning.

- Storage considerations: From perspective of storage: performance, Availability, Integrity, and Recoverability of data
-> Integrity: Data must be safe from corruption, loss, and outside attacks.

- Privacy, Security, and governance needs: It includes access control, multi-zone encryption, data management, and monitoring systems.

