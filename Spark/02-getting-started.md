# Downloading Apache Spark and Getting Started

Here we will set up the environment, understand the lifecycle of a Spark application, and write our first standalone PySpark program.

## Setting up Spark

There are two primary ways to get Spark running on our machine for learning purposes:

- Download the `tarball (i.e., park-3.x.x-bin-hadoop2.7.tgz)` from the official Spark website. This gives us the full distribution, including Scala, Java, R, and Python shells, as well as the Hadoop binaries needed to run locally.

- If we only care about Python, we can simply run `pip install pyspark` which installs the PySpark binaries from PyPI

If we download the full distribution, the following directories are included:

1. `bin`: Contains executables to interact with Spark, such as Pyspark (the shell) and `spark-submit` (to run programs).

2. `sbin`: Contains administrative scripts to start/stop clusters.

3. `examples`: Contains helpful sample code in Java, Python, R, and Scala.

## The Interactive Shell

Spark provides an interactive shell for rapid prototyping. In our terminal, running `pyspark` launches the Python shell.

`The spark Variable`: When the shell starts, it automatically creates a `SparkSession` objects for us, assigned to the variable spark. We use this object to read data and execute queries.

The example below is for reading a file locally:

```spark

# Read a text file into a DataFrame
strings = spark.read.text("README.md")

# Trigger an action to show the first 10 rows without truncating
strings.show(10, truncate=False)

# Count the total number of lines
strings.count()

```

## The Execution Hierarchy

To write PySpark code, we must understand how Spark breaks down the code into units of work. This hierarchy is critical:

- `Application`: A user program consisting of a `Driver` program and `Executors` on the cluster.

- `Job`: A parallel computation triggered by a `Spark Action` (e.g., save(), collect(), count())

- `Stage`: A job is divided into stages. Stages are created based on operations that can be performed serially versus those that require a data shuffle.

- `Task`: The smallest unit of work. A task is sent to one executor. Each task maps to a single core and works on a single `partition` of data.

## Transformation, Actions, and Lazy Evaluation

Spark operations fall into two categories. 

`Transformations (Lazy)`: Transformations transform a DataFrame into a new DataFrame without altering the original (immutability). Examples include `select(), filter(), groupBy()`

- `Lazy Evaluation`: Spark does not execute these commands immediately. Instead, it records them as a `lineage` of instructions to be executed later. This allows Spark to look at the entire chain of transformations and optimize the execution plan.

`Actions (Eager)`: Actions trigger the lazy evaluation. They tell spark, "Okay, I am done defining the plan; now compute the result."

Examples include `show(), count(), collect(), save()`

`Narrow vs Wide Transformations`: Spark optimizes based on dependencies between transformations.

- `Narrow Dependencies`: Each input partition contributes to only one output partition. No data movement is required across the network.

Examples include `filter(), select()`

- `Wide Dependencies`: Input partitions contribute to many output partitions. This forces a `Shuffle`, where data is written to disk and exchanged across the cluster network. 

Examples include `groupBy(), orderBy()`

## The Spark UI

When we run a Spark application, the driver launches a web UI (defaulting to `http://localhost:4040` in local mode). This UI is our primary debugging tool. It lets one visualize the Directed Acyclic Graph (DAG) of our jobs, inspect how long stages take, and see if tasks are failing or if data is being shuffled excessively.

## Our First Standalone Application: Counting M&Ms

To move beyond the shell, we write standalone applications (Python scripts) and submit them to Spark. The book provides an example script (mnmcount.py) that reads a CSV of M&M color counts by state and aggregates them.

The code structure:

- Initialize sPARK
- Read Data
- Transform (Lazy)
- Action (Execute)

When submitting the job, we do not run this script with the standard python command. Instead, one use `spark-submit`, which sets up the Spark environment and dependencies: `$SPARK_HOME/bin/spark-submit mnmcount.py data/mnm_dataset.csv`
