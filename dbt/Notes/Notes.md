# dbt (data build tool) Notes

## Overview
- dbt is a command-line tool that enables data analysts and engineers to transform data in their warehouse more effectively.
- It allows users to write modular SQL queries, which are then compiled into raw SQL and run against the data warehouse.

## Key Concepts
- **Models**: SQL files that define transformations. Each model corresponds to a table or view in the data warehouse.
- **Sources**: External tables in the data warehouse that dbt can reference.
- **Seeds**: CSV files that can be loaded into the data warehouse as tables.
- **Snapshots**: Point-in-time copies of tables that allow for auditing and historical analysis.
- **Macros**: Reusable SQL snippets that can be called within models or other macros.
- **Tests**: Assertions that validate data quality and integrity.

## Best Practices
- Use version control (e.g., Git) to manage dbt projects.
- Write tests for models to ensure data quality.
- Document models and their relationships using dbt's built-in documentation features.
- Leverage dbt's Jinja templating capabilities to create reusable SQL snippets.

## Resources
- [dbt Documentation](https://docs.getdbt.com/docs/introduction)
- [dbt GitHub Repository](https://github.com/dbt-labs/dbt)

## Sample commands
- Initialize a new dbt project:
    ```dbt init my_project```
- Run all models:
    ```dbt run```
- Test models:
    ```dbt test```
- Generate documentation:
    ```dbt docs generate```
- Serve documentation locally:
    ```dbt docs serve```    
- Debug a model:
    ```dbt debug```

## Creating a dbt Project

- **Projects**: A collection of models, tests, and configurations that define a dbt workflow.
- The project structure typically includes directories for models, tests, macros, and configurations.
- Data sources and destinations are defined in a `profiles.yml` file, which contains connection details for the data warehouse.
- To create a new dbt project, use the command `dbt init <project_name>`, which sets up the necessary directory structure and configuration files.
- A profile represents a set of connection configurations for different environments (e.g., development, production). Each profile can contain multiple targets, allowing users to switch between different databases or schemas easily. They are defined in the `profiles.yml` file, which is typically located in the user's home directory under the `.dbt` folder.
- Example `profiles.yml` structure:
    ```yaml
    marketing_campaign_results:
      outputs:
        dev:
          type: duckdb
          path: dbt.duckdb
        prod:
          type: snowflake
          ...
        target: dev

- **YAML (Yet Another Markup Language)** is a text based file format, where whitespace and indentation is important. It is used in dbt for configuration files, such as `dbt_project.yml` and `profiles.yml`. YAML files are human-readable and easy to write, making them suitable for defining settings and parameters in a structured way.

### DuckDB
- DuckDB is an open-source, serverless database, like SQLite, but optimized for analytical query workloads. It is designed to be embedded in applications and can run complex queries on large datasets efficiently.
- DuckDB is fact due to its vectorized nature. It workes well with dbt.