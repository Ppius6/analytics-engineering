# Big Data Processing

## Background

### The Genesis (2003 - 2004)

In the early 21st century, the internet began exploding. Google had indexed the web but needed a way to calculate rankings (PageRank) across petabytes of data. However, traditional servers could not handle that. 

- In 2003, Google published the __GFS (Google File System)__ paper which described how to store massive files by breaking them into chunks and spreading them across thousands of cheap computers. 

- In 2004, Google published the __MapReduce__ paper which described a programming model to process that data.
    - __Map__: Split the data and apply a function (e.g., count words).
    - __Reduce__: Aggregate the results
This moved the computation to the data, rather than moving data to the computer.

### The Hadoop Era (2006-2009)

So, the world wanted what Google had. 

- In 2006, __Doug Cutting__ at __Yahoo!__ created __Apache Hadoop__ based on Google's papers. It had two parts: `HDFS` - The file system (Storage), and `MapReduce` - the processing engine (Compute). 

Hadoop MapReduce was revolutionary but slow:
1. It was "Disk-based", so after every tiny step (Map), it wrote the result to the Hard Disk before starting the next step (Reduce).

2. It was fine for simple counting, but terrible for __Machine Learning__, which needs to loop over data hundreds of times (iterative processing).

### The Birth of Spark (2009-2010)

It began in 2009 as a research project at __UC Berkeley’s AMPLab (now RISELab)__. It was created by __Matei Zaharia__ to address the limitations of MapReduce.

__Matei Zaharia__, then a PhD student, was trying to win a Netflix machine learning contest using Hadoop. He got frustrated by the slowness of disk I/O. MapReduce was evolutionary for batch processing but inefficient for `iterative algorithms (like machine learning)` and `iteractive data mining`. It forced systems to write intermediate results to the disk after every step, causing massive I/O latency.

The idea came from the question of: As RAM prices were dropping, why not keep the data in the computer's __RAM (Memory)__ between steps instead of writing it to the hard disk. 

When Spark was born, it introduced `RDDs (Resilient Distributed Datasets)` which allowed data to be "cached" in memory. `RDDs` were a read-only collection of objects partitioned across machines. Crucially, RDDs allowed data to be kept `in memory` between steps, making Spark 10 - 100x faster than Hadoop MapReduce for certain workloads.

In 2013, Spark was donated to the __Apache Software Foundation (ASF)__, and its original creators founded `Databricks` to support the enterprise ecosystem.

### The Transition to DataFrames

Early Spark was powerful but difficult. Working with `RDDs` required verbose, complex code in Java or Scala. It was a tool for software engineers, not data analysts.

In 2015, Spark introduced `DataFrames` inspired by R and Pandas and the `Catalyst Optimizer`. This changed the user base as instead of telling Spark how to process data (low-level coding), analysts could describe what they wanted (SQL-like commands). Then, the `Catalyst Optimizer` would then translate that simple code into highly optimized low-level instructions automatically.

As Python began overtaking Java in the data world, the PySpark API matured. This allowed data scientists to use Spark's power without needing to learn Scala. 

In 2016, Spark unified these APIs, introducing `Structured Streaming`. This treated streaming data as an __infinite table__ that is continously appended to, allowing developers to use the same code for batch and streaming.

### The Lakehouse Era and Modern Performance

By 2019, Spark was the best engine for _processing_, but companies struggled with _storage_. `Data Lakes` like `AWS S3 or Azure Blob` were messy, prone to errors, and lacked `undo` buttons

`Databricks` open-sourced `Delta Lake`. This layer sits on top of the data lake and brings `ACID transactions (reliability)`, schema enforcement, and `Time Travel (version history)` to Spark.

Released in 2020, Spark 3.0 focused on bridging Data Engineering and Data Science. It introduced `Adaptive Query Execution (AQE)` to optimize queries on the fly and better support for GPUs, making deep learning on Spark efficient.

### Today

As of today, we are in the `Spark 4.x` era and the focus has shifted to decoupling:

- `Spark Connect`: This architecture allows thin clients (like a laptop running VS Code) to connect to massive remote clusters seamlessly, feeling `serverless`.
- Today, one rarely installs Spark manually. It is the invisible engine powering massive platforms like Microsoft Fabric, Databricks, and AWS EMR. It has become the standard dialect for distributed computing.

A summary of the evolution of big data processing from Google's innovations to the modern Spark ecosystem can be seen as follows:

| Era | Core Tech | The "Unlock" | Key Bottleneck Solved |
| :--- | :--- | :--- | :--- |
| __2004__ | __MapReduce__ | Distributed Processing | __Scale:__ Allowed processing data larger than one server. |
| __2010__ | __Spark (RDD)__ | In-Memory Processing | __Speed:__ Solved Disk I/O latency (100x faster). |
| __2015__ | __DataFrames__ | Catalyst Optimizer | __Usability:__ Solved complexity. Allowed Analysts to use SQL/Python. |
| __2019__ | __Delta Lake__ | ACID Transactions | __Reliability:__ Solved "messy" Data Lakes (The Lakehouse). |
| __Today__ | __Spark 4.x__ | Spark Connect / AI | __Access:__ Solved connectivity; "Serverless" feel & GPU native. |