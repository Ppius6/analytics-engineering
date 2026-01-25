# Introduction to Apache Spark

## What is Apache Spark?

Spark is defined as a "unified engine designed for large-scale distributed data processing. Its design philosophy relies on four pillars:

1. Speed

    Spark optimizes performance by running computations in memory. It constructs a `Directed Acyclic Graph (DAG)` of computations to schedule tasks efficiently. Its engine, `Tungsten` generates compact code to execute tasks efficiently across the cluster.

2. Ease of Use

    Spark provides a simple logical data structure called a `Resilient Distributed Dataset (RDD). Upon this, it builds higher-level abstractions like DataFrames. It offers transformations and actions as simple operations, allowing you to build big data apps in familiar languages (Python, Scala, Java, etc.)

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

