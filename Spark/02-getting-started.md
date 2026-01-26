# Downloading Apache Spark and Getting Started

Here we will set up the environment, understand the lifecycle of a Spark application, and write our first standalone PySpark program.

## Setting up Spark

There are two primary ways to get Spark running on our machine for learning purposes:

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