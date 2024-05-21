ACID for Relational Database
BASE for NoSQL databases

Are different consistency models

# ACID

Atomic
Consistency
Isolation
Durable

Ensures a performed transaction is always consistent.
Used by:
Financial institutions
Data warehousing
Databases that can handle many small simultaneous transactions
Fully consistent systems

Use cases:
Money transfers

# BASE

Basically Available: by spreading and replicating it across the nodes of the database cluster.
Soft state: Due the lack of immediate consistency, data values may change overtime.
stores don't have to be write-consistent.
Eventually consistent: The fact BASE model does not enforce immediate consistency does not mean that it until it does, data reads might be inconsistent.

Use cases:
Worldwide online services - users access to services
