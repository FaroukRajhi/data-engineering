# Objectives

Install a Spark Master and Worker using Docker Compose
Create a python script containing a spark job
Submit the job to the cluster directly from python (Note: you’ll learn how to submit a job from the command line in the Kubernetes Lab)

# Install spark cluster using docker compose

Get the latest code:

1
git clone https://github.com/big-data-europe/docker-spark.git
Copied!Executed!
Change the directory to the downloaded code:

1
cd docker-spark
Copied!Executed!
Start the cluster


docker-compose up
Copied!Executed!
After quite some time you should see the following message:
Successfully registered with master spark://<server address>:7077

# Create Code

Click Terminal from the menu, and click New Terminal to open a new terminal window.

Once the terminal opens up at the bottom of the window, please type in the following command in the terminal to create the Python script.

touch submit.py
Copied!Executed!
A new python file called submit.py is created.

Open the file in the file editor.

Paste the following code to the file and save.

import findspark
findspark.init()
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, IntegerType, StringType
sc = SparkContext.getOrCreate(SparkConf().setMaster('spark://localhost:7077'))
sc.setLogLevel("INFO")
spark = SparkSession.builder.getOrCreate()
spark = SparkSession.builder.getOrCreate()
df = spark.createDataFrame(
    [
        (1, "foo"),
        (2, "bar"),
    ],
    StructType(
        [
            StructField("id", IntegerType(), False),
            StructField("txt", StringType(), False),
        ]
    ),
)
print(df.dtypes)
df.show()
Copied!


# Execute code / submit spark job

Now we execute the python file we saved earlier.

In the terminal, run the following commands to upgrade the pip installer to ensure you have the latest version by running the following commands.
1
2
3
rm -r ~/.cache/pip/selfcheck/
pip3 install --upgrade pip
pip install --upgrade distro-info
Copied!Executed!
rm -r ~/.cache/pip/selfcheck/ removes any previously cached version of pip and allows to install the latest one.

Please enter the following commands in the terminal to download the spark environment.
1
wget https://archive.apache.org/dist/spark/spark-3.3.3/spark-3.3.3-bin-hadoop3.tgz && tar xf spark-3.3.3-bin-hadoop3.tgz && rm -rf spark-3.3.3-bin-hadoop3.tgz
Copied!Executed!
This takes a while. This downloads the spark as a zipped archive and unzips it in the current directory.

Run the following commands to set up the JAVA_HOME which is preinstalled in the environment and SPARK_HOME which you just downloaded.
1
2
export JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64
export SPARK_HOME=/home/project/spark-3.3.3-bin-hadoop3
Copied!Executed!
Install the required packages to set up the spark environment.
1
pip install pyspark
Copied!Executed!
1
python3 -m pip install findspark
Copied!Executed!

Type in the following command in the terminal to execute the Python script.
1
python3 submit.py


# Experiment yourself

Please have a look at the UI of the Apache Spark master and worker.

Click on the button below to launch the Spark Master. Alternatively, click on the Skills Network button on the left, it will open the “Skills Network Toolbox”. Then click the Other, then Launch Application. From there you should be able to enter the port number as 8080 and launch.
 Spark Master


This will take you to the admin UI of the Spark master (if your popup blocker doesn’t prevent it).

Please notice that you can see all registered workers (one in this case) and submitted jobs (also one in this case)
Note: The way how the lab environment works you can’t click on links in the UI - in a real installation, this of course is possible.

Click the button below to open the Spark Worker on 8081. Alternatively, click on the Skills Network button on the left, it will open the “Skills Network Toolbox”. Then click the Other, then Launch Application. From there, you should be able to enter the port number as 8081 and launch.


