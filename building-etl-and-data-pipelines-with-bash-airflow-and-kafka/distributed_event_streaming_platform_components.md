# What is an event

Events describe an entity's observable state updates over time.
For example:
The GPS coordinates of moving car.


# Common event formats
An event, as a special type of data, has different formats.

- Primitive type:
Such as plain text, number, or date.

- Key-value formats

Complex data type like like, tuple, JSON, XML, or even bytes

# One source to one destination

Event streaming from one event source to one destination.
The continuous event transportation between an event source and an event destination is called "event streaming".

# Many source to many destinations

Event streaming from multiple events sources to multiple destinations.

# Event streaming platform (ESP)

Acts as a middle layer among various events sources and destinations and provides
a unified interface for handling event-based ETL.
All event sources only need to send events to ESP instead of sending them to destination.

The destination needs only to subscribe to events.

- Common components of a ESP

Event broker: Designed to receive and consume events.
Event Storage: Event storage, which used for storing events received from events sources.
Analytic and query engine: Used for querying and analyzing the stored events