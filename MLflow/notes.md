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

A typical experiment process starts by formulating a hypothesis, then gathering and preparing the data, defining the experiments i.e., type of model, hyperparameters, datasets, then setting up experiment tracking for logging, and finally running the experiments and analyzing the results. Once we have identified the best-performing model, we can register it, along with all associated experiment details, visualize the results, and share them with stakeholders

### Preparing Model for Deployment

To avert the issues that may arise when deploying a model, it is important to containerize the model. Containerization is the process of packaging an application and its dependencies into a single, portable unit called a container. It allows us to run the application consistently across different environments, such as development, testing, and production.

Containerization helps to ensure that the model runs consistently across different environments, reducing the risk of compatibility issues and making it easier to deploy and manage the model in production.

Containerization tools such as Docker and Kubernetes are commonly used in MLOps to create, manage, and orchestrate containers. They provide a consistent and scalable way to deploy and manage machine learning models in production.

### ML Deployment Architecture

In traditional software development, applications are built in a monolithic architecture, where all components are tightly coupled and deployed as a single unit. However, in MLOps, a microservices architecture is often preferred, where different components of the machine learning system are developed, deployed, and scaled independently. 

The benefit of a microservices architecture is that in the event an application component fails, it does not bring down the entire system. It also allows for more flexibility and scalability, as different components can be updated or scaled independently. 

It is common practice to deploy the machine learning model as a microservice which allows the model to make predictions based on new, unseen data. This process is also known as inferencing.

To provide communication between microservices, it is common practice to develop an application programming interface (API). An API is a set of predefined input and output combinations that allow different software components to communicate with each other.

### CI/CD for MLOps

CI/CD stands for Continuous Integration and Continuous Deployment/Delivery. It is a set of practices that aim to automate the process of building, testing, and deploying software applications. 

Continuous Integration (CI) is the practice of automatically integrating code changes into a shared repository. It involves automatically building and testing the code whenever changes are made, ensuring that the codebase remains stable and functional.

Continuous Deployment/Delivery (CD) is the practice of automatically deploying code changes to production environments. It involves automatically deploying code changes whenever they pass the necessary tests and validations, ensuring that new features and bug fixes are delivered to users quickly and reliably.

Once a model is ready to be deployed, there are different deployment strategies to consider: `basic`, `shadow`, and `canary`. `Basic` deployment involves replacing the old model with the new model in production. All new input data will be sent to the new model instead of the old model. `Shadow` deployment involves sending new data to the new model, as well as the old model. The result of both models will be tested in order to ensure the new model works as expected. `Canary` deployment involves using the new model in production, but only for a small part of new incoming data. In this way, we do use the new model right away, but in case the new model fails, only a small number of users will be affected.

### Automation and scaling

While the machine learning lifecycle is an experimental process, automation can greatly help to speed up the lifecycle. Automation can be applied to various stages of the lifecycle, such as data preprocessing, feature engineering, model training, and deployment.

The design phase can remain to be a manual process, but templates can be created to help speed up the process. The development phase can be automated by creating pipelines that automate the data preprocessing, feature engineering, and model training steps. The deployment phase can be automated by creating scripts that automate the deployment of the model to production environments.

### Monitoring ML Models

After model deployment, it is important to monitor the model's performance in production. Monitoring helps to ensure that the model continues to perform well over time and that any issues are detected and addressed promptly.

There are different types of monitoring; 

- `statistical monitoring` focuses on the input and output data, including its predictions. An example is customer X has a 72% probability of churning, customer Y has a 31% probability of churning.

- `computational monitoring` focuses on the technical metrics of the model such as number of incoming requests that are made, network usage of the model, or the number of resources a server uses to keep the model running.

A feedback loop is essential to find out when and why the model was wrong, especially when we get the actual outcome. For example, if a model predicts that a customer will churn, but the customer does not churn, we need to find out why the model was wrong. This feedback can be used to improve the model and make it more accurate.

### Model re-training

Inherent to data is that it changes over time. It is given that the world is changing, and since our model depends on data, these changes also impact the model. Therefore, the model may need to be re-trained over time to ensure that it continues to perform well.

Data drift is a change in the distribution of the input data over time. It can occur due to various reasons, such as changes in customer behavior, market trends, or external factors. Data drift can lead to a decrease in model performance, as the model may no longer be able to accurately predict outcomes based on the new data.

Concept drift is a change in the relationship between the input data and the target variable over time. It can occur due to changes in the underlying process that generates the data, such as changes in customer preferences or market conditions. Concept drift can also lead to a decrease in model performance, as the model may no longer be able to accurately predict outcomes based on the new relationship between the input data and the target variable.

Retraining a model depends on the business environment (how volatile the data is), cost of retraining, and business requirements (e.g., acceptable levels of performance degradation, the required model performance). The retraining methods include fully retraining the model from scratch, incremental training (updating the model with new data), or using online learning (continuously updating the model as new data arrives).

### Levels of MLOps Maturity

The MLOps maturity is about the automation, collaboration, and monitoring within machine learning and operations processes in a business. These levels mostly apply to the development and deployment stages of the MLOps lifecycle. The design phase cannot be fully automated, as it requires human input and creativity.

We can distinguish 3 levels of MLOps maturity: 

# Levels of MLOps Maturity

| Aspect | Level 1 | Level 2 | Level 3 |
|--------|---------|---------|---------|
| **Automation** | Manual processes | Automated development (CI) | Full automation |
| **Collaboration** | Distinction machine learning and operations | Collaboration during handover from development | Close collaboration |
| **Monitoring** | No monitoring | Development tracking (experiments, feature store) | Full monitoring |

In Level 1, the processes are mostly manual, with little to no automation and the machine learning and operations teams work in isolation.

In Level 2, there is automation in the development of machine learning models, and machine learning and operations teams collaborate together when a new model is ready for deployment.

In level 3, the ML lifecycle is fully automated throughout the development and deployment phases.

### MLOps Tools

For the feature store, we can use tools such as `Feast`, `Tecton`, or `Hopsworks`. These tools help manage and serve features for machine learning models, making it easier to maintain and update features over time.

For experiment tracking, we can use tools such as `MLflow`, `ClearML`, or `Weights & Biases`. These tools help track and manage machine learning experiments, making it easier to reproduce and compare results.

For containerization, we can use tools such as `Docker` and `Kubernetes`. These tools help create, manage, and orchestrate containers, making it easier to deploy and manage machine learning models in production.

For CI/CD, we can use tools such as `Jenkins`, `GitLab CI/CD`, or `GitHub Actions`. These tools help automate the process of building, testing, and deploying machine learning models, making it easier to deliver new features and updates quickly and reliably.

Monitoring tools separate into either statistical monitoring or computational monitoring. For statistical monitoring, we can use tools such as `Evidently AI`, `Fiddler`, or `WhyLabs`. These tools help monitor the performance of machine learning models in production, making it easier to detect and address issues promptly. For computational monitoring, we can use tools such as `Prometheus`, `Grafana`, or `Datadog`. These tools help monitor the technical metrics of machine learning models in production, making it easier to ensure that the models are running smoothly and efficiently.

