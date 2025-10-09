# MLflow Notes

## (Machine Learning Operations) MLOps 

It is a set of practices to design, deploy, and maintain machine learning in production continuously, reliably, and efficiently. It originates from Development Operations (DevOps) in software engineering.

Through MLOps, we can automate and streamline the machine learning lifecycle, including data preparation, model training, deployment, monitoring, and maintenance.

### MLOps Lifecycle

The MLOps lifecycle consists of three key stages:

`Design` → `Development` → `Deployment`

1. **Design**: This stage involves defining the problem, gathering requirements, and planning the machine learning project. It includes data collection, data exploration, and feature engineering.

2. **Development**: In this stage, data scientists and engineers build and train machine learning models. It includes selecting algorithms, tuning hyperparameters, and validating models using cross-validation techniques.

3. **Deployment**: This stage involves deploying the trained models into production environments. It includes setting up infrastructure, monitoring model performance, and managing model versions.

### Roles in MLOps

A typical machine learning lifecycle involves the following steps

`Problem definition & requirements` → `EDA & data preprocessing` → `Implementation design` → `Feature engineering` → `Experiment design` → `Model training & evaluation` → `Set up CI/CD` → `Model deployment` → `Monitoring & maintenance`

While integrating these steps into our three key stages, step 1 to step 3 are part of the `Design` stage, step 4 to step 6 are part of the `Development` stage, and step 7 to step 9 are part of the `Deployment` stage.

The main roles are business roles and technical roles. For the business roles, we have the `business stakeholder` or `product owner` who will be part of the `Problem definition & requirements` step, `Model training & evaluation` step, and the `Monitoring & maintenance` step. They are mostly involved throughout the lifecycle, defining business requirements, evaluating model performance, and monitoring the impact of the deployed models on business outcomes.

Still in the business roles, we have the `subject matter expert (SME)` who will be part of the `EDA & data preprocessing` step, `Feature engineering` step, the `Model training & evaluation` step, and the `Monitoring & maintenance` step. They provide domain expertise, help interpret data, and ensure that the models align with business goals.

The technical roles include the `data engineer` and the `data scientist`. The `data scientist` is part of the `EDA & data preprocessing` step, `Implementation design` step, `Feature engineering` step, `Experiment design` step, and the `Model training & evaluation` step. They are responsible for data analysis, model development, and evaluation. They are mostly involved in the overall development of the machine learning models lifecycle.

The `data engineer` is part of the `Implementation design` step, `Feature engineering` step, `Model training & evaluation` step, and `Monitoring & maintenance` step. They focus on collecting, storing, and processing the data, data quality checks, and tests to ensure the quality is maintained throughout the process. 

The `ML engineer` is a relatively new role that has emerged with the rise of MLOps. It is quite a versatile role and is designed specifically to have expertise over the entire machine learning lifecycle. 

### Design and Development Stage

For every machine learning project, we have to estimate the value it will bring into our business, as machine learning development is experimental and uncertain.

We must also consider the business requirements, such as the expected accuracy, latency, transparency, and throughput of the model. Transparency is essential for understanding how the model makes decisions, why it is wrong, and how to improve it. 

We must also consider other issues such as data privacy, security, and compliance with regulations. For example, if we are working with healthcare data, we must ensure that we comply with HIPAA regulations. In Finance, the law requires us to explain how the model makes decisions.

To see if the ML Lifecycle progresses as expected, it is often wise to track the performance of the model. The data scientist will look at the accuracy of a model, how many times the algorithm predicted the right outcome. The subject matter expert will look at the business metrics, how much revenue the model generates, or how much cost it saves. The business stakeholder will look at the overall impact of the model on the business, monetary or non-monetary.

### Data quality and ingestion

Data quality is a measure of how well data serves its intended purpose. Poor data quality can lead to inaccurate models, which can have significant consequences for businesses.

We focus on the following dimensions of data quality: `accuracy`, `completeness`, `consistency`, and `timeliness`.

An example of data quality dimensions:


| Dimension | Example Question to Answer | Example of Dimension Quality |
|-----------|---------------------------|------------------------------|
| **Accuracy** | Does our data correctly describe the customer? | The customer's age in the data is 18, but is actually 32. |
| **Completeness** | Is there any customer data missing? | For 80% of the customers, we don't have a last name. |
| **Consistency** | Is the definition of the customer synchronized throughout the company? | The customer is stated as active in one database but not active in another. |
| **Timeliness** | When is the customer ordering data available? | The customer orders are synchronized at the end of the day but are not available in real-time. |

### Feature Engineering

It is the process of selecting, manipulating, and transforming raw data into features (a variable such as a column in a table) that can be used to train machine learning models. It is a crucial step in the machine learning lifecycle, as the quality of the features can significantly impact the performance of the models.

The goal of feature engineering is to enhance model performance by identifying the most informative features, reducing noise, and improving the model's ability to generalize to new data.

Leveraging domain-specific knowledge is essential in feature engineering. It helps identify relevant features, understand their relationships, and create new features that capture important patterns in the data.

A feature store is a centralized repository for storing, managing, and sharing features used in machine learning models. It allows data scientists and engineers to access and reuse features across different projects, improving efficiency and consistency in feature engineering.

Data versioning is the process of tracking and managing changes to datasets over time. It allows data scientists and engineers to maintain a history of dataset versions, enabling them to reproduce experiments, compare results, and collaborate effectively.

### Experiment Tracking

Experiment tracking is the process of recording and managing information about machine learning experiments, including model configurations, hyperparameters, datasets, and evaluation metrics. It helps data scientists and engineers keep track of their experiments, compare results, and reproduce findings.

It helps us to compare results, reproduce experiments, and collaborate effectively. It also helps us to identify the best-performing models and understand the impact of different configurations and hyperparameters on model performance.

A typical experiment process starts by formulating a hypothesis, then gathering and preparing the data, defining the experiments i.e., type of model, hyperparameters, datasets, then setting up experiment tracking for logging, and finally running the experiments and analyzing the results. Once we have identified the best-performing model, we can register it, along with all associated experiment details, visualize the results, and share them with stakeholders.