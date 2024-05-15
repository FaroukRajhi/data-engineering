The logging capability is required for developers to monitor the status of tasks in DAG runs, and to diagnose and debug issues.
Logs files are store on local filesystem
We can store it on cloud storage.

- Monitoring metrics
- Counters: Metrics that always increase
Total count of task instances failures
Total count of task instances successes

- Gauge: Metrics that may fluctuate
Number of running tasks
DAG bag size

- Timers: Metrics  related to time duration
Milliseconds to finish a task
milliseconds to reach a success or failed state.
