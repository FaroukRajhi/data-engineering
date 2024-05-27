Welcome to Overview of Apache Spark Cluster Modes!
After watching this video, you will be able to
Identify the different modes of running Apache Spark on a cluster
Describe the components and benefits of each cluster mode
Describe how to run Spark to connect with each cluster mode
Describe how and when to setup a local Spark instance.
The Spark Cluster Manager communicates with a cluster to acquire resources for an application
to run.
It runs as a service outside the application and abstracts the cluster manager type.
While an application is running, the Spark Context creates tasks and communicates to
the cluster manager what resources are needed.
Then the cluster manager reserves executor cores and memory resources.
Once the resources are reserved, tasks can be transferred to the executor processes to
run.
Spark has built-in support for several cluster managers.
A Standalone cluster manager is included with the Spark installation.
It’s best for setting up a simple cluster.
Apache Hadoop YARN, or Yet Another Resource Negotiator, is a cluster manager from the
Hadoop project.
Apache Mesos is a general-purpose cluster manager that Spark can run with additional
benefits.S
Finally, Kubernetes is an open-source system for running containerized applications.
Spark Standalone comes packaged with the Spark installation, so there are no additional dependencies
required to configure and deploy.
Spark Standalone is specifically designed to run Spark and is often the fastest way
to get a cluster up and running applications.
A Spark Standalone cluster has two main components: Workers and the Master.
The workers run on cluster nodes.
They start an executor process with one or more reserved cores.
There must be one master available which can run on any cluster node.
It connects workers to the cluster and keeps track of them with heartbeat polling.
However, if the master is together with a worker, do not reserve all the node’s cores
and memory for the worker.
To manually set up a Spark Standalone cluster, start the Master.
The Master is assigned a URL with a hostname and port number.
After the master is up, you can use the Master URL to start workers on any node using bi-directional
communication with the master.
Once the master and the workers are running, you can launch a Spark application on the
cluster by specifying the master URL as an argument to connect them.
To see additional configuration options, refer to the Apache Spark documentation on the spark.apache.org
website.
Apache Hadoop YARN is a general-purpose cluster manager.
It’s popular in the big data ecosystem and supports many other frameworks besides Spark.
YARN clusters have their own dependencies, set-up and configuration requirements so deploying
them is more complex than Spark Standalone.
To run Spark on an existing YARN cluster, use the ‘--master’ option with the keyword
YARN.
When Spark sees that the cluster manager type is YARN, it will look for the standard Hadoop
configuration files to decide how to connect with the YARN cluster.
No other configuration from Spark is needed.
Apache Mesos is another general-purpose cluster manager supported by Spark.
Using Mesos has some advantages.
It can provide dynamic partitioning between Spark and other big data frameworks and scalable
partitioning between multiple Spark instances.
However, running Spark on Apache Mesos might require some additional setup depending on
your configuration requirements.
More details are provided on the spark.apache.org website at the link shown here.
A Kubernetes cluster runs containerized applications.
This makes Spark applications more portable and helps automate deployment, simplify dependency
management and scale the cluster as needed.
Spark uses a built-in native Kubernetes scheduler.
To run Spark on Kubernetes, use the example call shown.
Local mode runs a Spark application as a single process locally on the machine.
The process calls ‘spark-submit’ and runs the executors as separate threads in the main
process.
Local mode does not connect to any cluster or require configuration outside a basic Spark
installation.
Local mode can be run on a laptop.
That’s useful for testing or debugging a Spark application, for example, testing a
small data subset to verify correctness before running the application on a cluster.
However, being constrained by a single process means local mode is not designed for optimal
performance.
To run in local mode, use the ‘--master’ option with the keyword ‘local’ followed
by a number to indicate how many cores the Spark application can use for the executor.
To use all available cores, replace the number with an asterisk wildcard.
Keep in mind not all configuration for a cluster will be valid in local mode.
In this video, you learned that:
Cluster managers acquire resources and run as an abstracted service outside the application
Spark can run on Spark Standalone, Apache Hadoop YARN, Apache Mesos or Kubernetes cluster
managers, with specific set-up requirements
Choosing a cluster manager depends on your data ecosystem and factors such as ease of
configuration, portability, deployment or data partitioning needs
Spark can run in local mode, useful for testing or debugging an application.