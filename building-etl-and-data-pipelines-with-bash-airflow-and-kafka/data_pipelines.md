Pipeline is a series of connected processes.
Output of one process is input of the next

Performance is latency

Throughput
How much data can be fed through the pipe per unit of time.

- Use cases 
Applications of data pipeline

Backing up files
Integrating disparate raw data sources into data lake
Moving transactional records to a data warehouse
Streaming data from IoT devices to dashboards

# Key data pipeline processes

Stages of data pipeline processes:
Data extraction from sources
Data ingestion into the pipeline
Transformation stages
Loading data into destination facilities
Scheduling
Monitoring latency, throughput, and errors, warnings and failures, logging and alerting system, utilization rate.

- Load balanced pipelines:
Just-in-time data packet relays
No upstream data flow bottleneck
Uniform packet throughput for each stage

- Handling unbalanced loads
Pipelines typically contain bottleneck
Slower stages may be parallelized to speed up throughput

- Stage synchronization

I/O buffers can help synchronize stages
Holding are for data between processing stages
Buffers regulate the flow of data, may improve throughput
I/O buffers used to distribute loads on parallelized stages.
