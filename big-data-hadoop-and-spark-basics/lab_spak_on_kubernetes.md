# SetUp

On the right hand side to this instructions you’ll see the Theia IDE. Select the Lab tab. On the menu bar select Terminal>New Terminal.

Please enter the following command in the terminal to get the latest code.
1
git clone https://github.com/ibm-developer-skills-network/fgskh-new_horizons.git
Copied!Executed!
Change the directory to the downloaded code.
1
cd fgskh-new_horizons
Copied!Executed!
Add an alias to kubectl. This will help you just type k instead of kubectl.
1
alias k='kubectl'
Copied!Executed!
Save the current namespace in an environment variable that will be used later
1
my_namespace=$(kubectl config view --minify -o jsonpath='{

# Deploy the apache in k8s

Install the Apache Spark POD
1
k apply -f spark/pod_spark.yaml
Copied!
Now it is time to check the status of the Pod by running the following command.
1
k get po
Copied!
If you see the following output it means that the Pod is not yet available and you need to wait a bit.

1
2
NAME   READY   STATUS              RESTARTS   AGE
spark  0/2     ContainerCreating   0          29s
Copied!
Wait for a few second and issue the command again after some time.
1
k get po
Copied!
Please repeat the step 2 until you have a STATUS that reflects that it is Running.

You should see an output as given below. The AGE attribute might be different, depending on how long it took you to get it running.
1
2
NAME  READY   STATUS    RESTARTS   AGE
spark 2/2     Running   0          10m
Copied!
In case you see the following status you need to delete the pod and start over again later as this usually happens when the image registry is unreliable or offline.

1
2
NAME   READY   STATUS              RESTARTS   AGE
spark  0/2     ImagePullBackOff    0          29s
Copied!
Just in this case please delete the pod:
1
k delete po spark
Copied!
Then start over:

1
k apply -f spark/pod_spark.yaml
Copied!
Again, regularly check status:

1
k get po

# Submit apache jobs to k8s

Now it is time to run a command inside the spark container of this Pod.
The command exec is told to provide access to the container called spark (-c). With – we execute a command, in this example we just echo a message.

1
k exec spark -c spark  -- echo "Hello from inside the container"
Copied!
You just ran a command in spark container residing in spark pod inside Kubernetes. We will use this container to submit Spark applications to the Kubernetes cluster. This container is based on an image with the Apache Spark distribution and the kubectl command pre-installed.

If you are interested you can have a look at the Dockerfile to understand what’s really inside.

You can also check out the pod.yaml. You’ll notice that it contains two containers. One is Apache Spark, another one is providing a Kubernetes Proxy - a so called side car container - allowing to interact with the Kubernetes cluster from inside a Pod.

Inside the container you can use the spark-submit command which makes use of the new native Kubernetes scheduler that has been added to Spark recently.

The following command submits the SparkPi sample application to the cluster. SparkPi computes Pi and the more iterations you run, the more precise it gets:

k exec spark -c spark -- ./bin/spark-submit \
--master k8s://http://127.0.0.1:8001 \
--deploy-mode cluster \
--name spark-pi \
--class org.apache.spark.examples.SparkPi \
--conf spark.executor.instances=1 \
--conf spark.kubernetes.container.image=romeokienzler/spark-py:3.1.2 \
--conf spark.kubernetes.executor.request.cores=0.2 \
--conf spark.kubernetes.executor.limit.cores=0.3 \
--conf spark.kubernetes.driver.request.cores=0.2 \
--conf spark.kubernetes.driver.limit.cores=0.3 \
--conf spark.driver.memory=512m \
--conf spark.kubernetes.namespace=${my_namespace} \
local:///opt/spark/examples/jars/spark-examples_2.12-3.1.2.jar \
10
Copied!
You should see output like below, please ignore the WARNINGS. Unless you don’t see ERRORS all is fine:

# Understanding the spark-submit command

So let’s have a look what’s going on here:

./bin/spark-submit is the command to submit applications to a Apache Spark cluster
–master k8s://http://127.0.0.1:8001 is the address of the Kubernetes API server - the way kubectl but also the Apache Spark native Kubernetes scheduler interacts with the Kubernetes cluster
–name spark-pi provides a name for the job and the subsequent Pods created by the Apache Spark native Kubernetes scheduler are prefixed with that name
–class org.apache.spark.examples.SparkPi provides the canonical name for the Spark application to run (Java package and class name)
–conf spark.executor.instances=1 tells the Apache Spark native Kubernetes scheduler how many Pods it has to create to parallelize the application. Note that on this single node development Kubernetes cluster increasing this number doesn’t make any sense (besides adding overhead for parallelization)
–conf spark.kubernetes.container.image=romeokienzler/spark-py:3.1.2 tells the Apache Spark native Kubernetes scheduler which container image it should use for creating the driver and executor Pods. This image can be custom build using the provided Dockerfiles in kubernetes/dockerfiles/spark/ and bin/docker-image-tool.sh in the Apache Spark distribution
–conf spark.kubernetes.executor.limit.cores=0.3 tells the Apache Spark native Kubernetes scheduler to set the CPU core limit to only use 0.3 core per executor Pod
–conf spark.kubernetes.driver.limit.cores=0.3 tells the Apache Spark native Kubernetes scheduler to set the CPU core limit to only use 0.3 core for the driver Pod
–conf spark.driver.memory=512m tells the Apache Spark native Kubernetes scheduler to set the memory limit to only use 512MBs for the driver Pod
–conf spark.kubernetes.namespace=${my_namespace} tells the Apache Spark native Kubernetes scheduler to set the namespace to my_namespace environment variable that we set before.
local:///opt/spark/examples/jars/spark-examples_2.12-3.1.2.jar indicates the jar file the application is contained in. Note that the local:// prefix addresses a path within the container images provided by the spark.kubernetes.container.image option. Since we’re using a jar provided by the Apache Spark distribution this is not a problem, otherwise the spark.kubernetes.file.upload.path option has to be set and an appropriate storage subsystem has to be configured, as described in the documentation
10 tells the application to run for 10 iterations, then output the computed value of Pi
Please see the documentation for a full list of available parameters.


