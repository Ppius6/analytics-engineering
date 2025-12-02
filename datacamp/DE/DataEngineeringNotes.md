# General Data Engineering Notes
Data engineers lay the groundwork for data collection.
Most of this data exist as big data, which can be from sensors and devices, social media, enterprise data, and VoIP.

Big data is categorized into:
- Volume - How much data is it?
- Variety - What kind of data is it?
- Velocity - How frequent is the data generated? 
- Veracity - How accurate is the data being generated?
- Value - How useful is the data

Data engineers configure pipelines to get the data from the sources to a data lake then to data warehouses.

## Storing data

Data exists in various structures
- Structured data - SQL
- Unstructured data - which is quite difficult to search and organize, is stored in data lakes, sometimes data warehouses, or data lakes.
- Semi-structured data which exists as JSON, XML, or YAML. It has a consistent model with less rigid implementation, different data types, easier to search and organize.

Some differences between data lakes and data warehouse include:

| Data Lake                                     | Data Warehouse                              |
|-----------------------------------------------|---------------------------------------------|
| Stores all the raw data                       | Specific data for specific use              |
| Can be petabytes (1 million GBs)              | Relatively small                            |
| Stores all data structures                    | Stores mainly structured data               |
| Cost-effective                                | More costly to update                       |
| Difficult to analyze                          | Optimized for data analysis                 |
| Requires an up-to-date data catalog           | Also used by data analysts and business analysts |
| Used by data scientists                       | Ad-hoc, read-only queries                   |
| Big data, real-time analytics                 |                                             |

## Moving and Processing Data

Data engineers do the following:

- Data manipulation, cleaning, and tidying tasks
    - that can be automated
    - that will always need to be done
- Rejecting corrupt song files
- Deciding what happens with missing metadata
- Separate artists and albums tables...
- ... but provide view combining them
- Store data in a sanely structured database
- Create views on top of the database tables
- Indexing
- Optimizing the performance of the database

### ETL
ETL stands for Extract, Transform, Load, and it's a fundamental process in data engineering that involves moving data from one or more sources into a destination system, which is typically a data warehouse. 

Here are examples illustrating the differences involved in each step of the ETL process:

#### Extract
- Extracting sales data from a single CRM system.
- Extracting customer data from various sources, such as CRMs, customer support platforms, and social media analytics tools.

#### Transform
- Converting date formats to a standardized form for reporting purposes.
- Aggregating sales data, calculating running totals or averages, and joining it with inventory data to analyze sales performance against stock levels.

#### Load
- Loading extracted and transformed data into a data warehouse in a single batch operation during off-peak hours.
- Loading data in real-time or near-real-time as new data is available, using a CDC (Change Data Capture) mechanism to update only changed rows.

### Scheduling 

Data is sent manually or scheduled. 

It can be updated automatically at a specific time, or when a specific condition is met, something known as sensor scheduling. 

### Batches and Streams

In batch processing, data is sent in groups at specific intervals. It is cheaper as it can be configured to run when resources are not being used.

In stream processing, records are sent in real-time. For instance, new users signing in, online vs offline listening music. 

Scheduling tools include Apache Airflow or luigi. 

## Parallel Computing

It forms the basis of modern data processing tools. It saves memory and need for reducing processing power.

### An analogy
Imagine you have a large laundry task of washing 100 shirts. In a traditional, sequential computing scenario, this would be like having one washing machine and one person to do all the work. That person would have to wash, dry, and fold each shirt one after another. It would take a lot of time to complete the entire task because only one shirt is processed at a time.

Instead of one person and one washing machine, you have 10 washing machines and 10 people, each responsible for washing, drying, and folding 10 shirts. All of these mini-laundry stations operate simultaneously. While one person is washing their batch of shirts, another might be drying theirs, and yet another might be folding. This distribution of tasks greatly reduces the overall processing time because multiple shirts are being processed at the same time across different stages.

This saves:
- Processing power
- Reduces memory footprint

However, there are costs involved, much more communication time. 

### Cloud Computing

Cloud has many benefits as compared to servers on premises.
| Servers on Premises                       | Servers on the Cloud                  |
|-------------------------------------------|---------------------------------------|
| Bought                                    | Rented                                |
| Need space                                | Don't need space                      |
| Electrical and maintenance cost           | Use just the resources we need        |
| Enough power for peak moments             | When we need them                     |
| Processing power unused at quieter times  | The closer to the user the better     |

It serves the purpose of database reliability by duplicating the databases to other locations.

The top cloud platforms are AWS, Microsoft Azure, and Google Cloud. 

| Service Type | AWS                | Azure                 | Google Cloud         |
|--------------|--------------------|-----------------------|----------------------|
| File Storage | AWS S3             | Azure Blob Storage    | Google Cloud Storage |
| Computation  | AWS EC2            | Azure Virtual Machines| Google Compute Engine|
| Databases    | AWS RDS            | Azure SQL Database    | Google Cloud SQL     |

For the fictional company at Spotflix, upon choosing AWS, they would need S3 to store cover albums, EC2 for processing songs and RDS for storing employee information.

Multicloud helps:
- To reduce reliance on a single vendor.
- Cost-efficiencies.
- Local laws requiring certain data to be physically present within the country. 
- Disasters mitigation.

However, it may lead to incompatibility, customer lock-in by the cloud provider, and hard management of security and governance. 