# MLflow

## Introduction

MLflow is an open-source platform designed to manage the machine learning lifecycle, including experimentation, reproducibility, and deployment. It provides tools for tracking experiments, packaging code into reproducible runs, and sharing and deploying models.

MLflow consists of four main components: 
1. **Mlflow Tracking**: For logging and querying experiments.
2. **Mlflow Models**: For packaging models in a standard format, building custom models, and deploying them to various platforms.
3. **Mlflow Registry**: For managing the lifecycle of models, including versioning and stage transitions.
4. **Mlflow Projects**: For packaging data science code in a reusable and reproducible format.

Working with experiments; `MLflow Client` and `MLflow module` are two primary ways to interact with MLflow.

`MLflow Client`: It is a lower-level API for interacting directly with different aspects of MLflow.

creating experiments;

```python
client.create_experiment("Name")
```

Tagging experiments;

```python
client.set_experiment_tag("name", k, v)
```

deleting experiments;

```python
client.delete_experiment("name")
```

`MLflow module`: It provides a higher-level API for managing experiments, runs, and models.

creating experiments;

```python
mlflow.create_experiment("Name")
```

Tagging experiments;

```python
mlflow.set_experiment_tag("name", k, v)
```

deleting experiments;

```python
mlflow.delete_experiment("name")
```

setting experiment;

```python
mlflow.set_experiment("name")
```

For example, interacting with experiments using the MLflow module. When starting a new ML application, 

```python
import mlflow
# Create an experiment
mlflow.create_experiment("My Experiment")
# Tag new experiment
mlflow.set_experiment_tag("My Experiment", "owner", "user1")
# Set the current experiment
mlflow.set_experiment("My Experiment")
```

## MLflow Tracking

MLflow Tracking is a component of MLflow that allows you to log and query experiments. It provides a way to record and query parameters, metrics, and artifacts associated with machine learning runs through an API.

Mlflow uses the term "logging" when data or an artifact is saved to MLflow Tracking.

MLflow Tracking is organized around the concept of `runs`. A new run means new model training and information about the model is logged to MLflow. Each run is also placed within an `experiment`, which is a collection of runs that share a common purpose or goal.

When a training run is started, the mlflow module sets the run as active. When a run is active, all metrics, parameters, and artifacts will be logged under the current active run. The mlflow module will continue logging to the active run until the code exits or the end_run function is called.

When logging to mlflow tracking, we save metrics, parameters, and artifacts for an active run. The mlflow module provides functions to log these items.

For a single metric, we can use the `log_metric` function. For multiple metrics, we can use the `log_metrics` function. The same applies to parameters and artifacts; we can use `log_param` and `log_params` for parameters, and `log_artifact` and `log_artifacts` for artifacts.

To log a run;

```python
import mlflow
mlflow.set_experiment("My Experiment")
mlflow.start_run()
lr = LogisticRegression(n_jobs=-1)
lr.fit(X, y)
score = lr.score(X, y)
mlflow.log_metric("score", score)
mlflow.log_param("n_jobs", 1)
mlflow.log_artifact("model.py")
mlflow.end_run()
```

Opening the MLflow UI;

```bash
mlflow ui
```
This command starts the MLflow UI server, which you can access in your web browser at `http://localhost:5000`. The UI allows you to visualize and compare runs, view metrics, parameters, and artifacts, and manage experiments.

When seeking to get information about a run, we use the `run1 = run.info` function. This function returns a RunInfo object, which contains metadata about the run, such as its ID, experiment ID, start time, end time, and status.

After experimenting with different models, we can compare the results of different runs. The MLflow UI provides a convenient way to visualize and compare runs based on their metrics and parameters.

`mlflow.search_runs` is a function that allows you to query runs based on various criteria. You can filter runs by experiment, status, and other attributes. For example, to get all runs from a specific experiment, you can use:

```python
runs = mlflow.search_runs(experiment_ids=["0"])
```

A search run example;

```python
import mlflow
f1_score_filter = "metrics.f1_score > 0.8"
mlflow.search_runs(
    experiment_names = ["My Experiment"],
    filter_string = f1_score_filter,
    order_by = ["metrics.precision_score DESC"]
)
```
