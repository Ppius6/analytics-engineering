# Introduction to Apache Spark

## What is Apache Spark?

Spark is defined as a unified engine designed for large-scale distributed data processing. Its design philosophy relies on four pillars:

1. Speed

    Spark optimizes performance by running computations in memory. It constructs a `Directed Acyclic Graph (DAG)` of computations to schedule tasks efficiently. Its engine, `Tungsten` generates compact code to execute tasks efficiently across the cluster.

2. Ease of Use

    Spark provides a simple logical data structure called a `Resilient Distributed Dataset (RDD)`. Upon this, it builds higher-level abstractions like DataFrames. It offers transformations and actions as simple operations, allowing you to build big data apps in familiar languages (Python, Scala, Java, etc.)

3. Modularity

    Spark supports many workloads (SQL, ML, Streaming) under a single engine. You can write a single application that does it all without needing distinct engines for different tasks.

4. Extensibility

    Spark decouples storage from compute. It can read data from Hadoop, Cassandra, HBase, MongoDB, and S3, processing it all in memory. It focuses on the computation engine rather than storage.

## Unified Analytics

The concept of `unification` is central to Spark. It replaces separate engines (like `Storm` for streaming or `Impala` for SQL) with a single stack.

1. `Spark SQL`

    This module works with structured data. It allows one to read data from RDBMS tables or file formats (CSV, JSON, Parquet) into DataFrames. It is ANSI SQL:2003-compliant, meaning one can run standard SQL queries against your distributed data.

2. `Spark MLlib`

    The library contains common Machine Learning (ML) algorithms which allows for extracting features, building pipelines, and persisting models. It leverages Spark's speed for iterative model training.

3. `Spark Structured Streaming`

    This allows developers to process real-time data streams as if they were static tables. The engine handles late data and fault tolerance automatically.

4. `GraphX`

    A library for manipulating graphs (i.e., social networks) and performing graph-parallel computations like `PageRank`

## Apache Spark's Distributed Execution

Here, we will understand how code runs on a cluster. The components include:

1. `Spark Driver`

    This is the __brain__ of the application. It orchestrates operations, communicates with the cluster manager, requests resources, and transforms your code into a DAG of tasks to be distributed.

2. `SparkSession`

    Introduced in Spark 2.0, this is the unified entry point for all Spark functionality. It replaced older context objects (like __SparkContext__ or __SQLContext__). One uses the __SparkSession__ to create DataFrames, read data, and issue SQL queries.

3. `Cluster Manager`

    It is responsible for managing and allocating resources (CPU, memory) for the cluster. Spark supports four types: the built-in Standalone manager, Apache Hadoop YARN, Apache Mesos, and Kubernetes.

4. `Spark Executor`

    These run on worker nodes. They receive tasks from the Driver and execute them. They are responsible for the actual work.

Spark can run in different modes depending on where the Driver and Executors sit

- `Local Mode`: Here, everything runs in a single JVM on the machine, which is great for learning.
- `Standalone`: Uses Spark's built-in cluster manager.
- `YARN/Kubernetes`: It is widely used in production to manage resources across many applications.

Physical data is distributed across the cluster as `partitions`. Spark treats these partitions as a high-level logical data abstraction (like a DataFrame) in memory. `Partitioning` allows for efficient parallelism. Ideally, each executor core is assigned its own data partition to work on. For example, if you have 8 partitions, each executor can read a partition into its memory and process it in parallel.

## The Developer's Experience

Spark provides a set of composable APIs across languages (Scala, Java, Python, SQL, and R).

Data scientists use Spark for data exploration and model building. They often use the Spark shell for interactive queries. 

Data engineers build pipelines to transform raw, dirty data into clean data for consumption. They use Spark because it handles the complexity of distribution and fault tolerance, allowing them to focus on business logic.

