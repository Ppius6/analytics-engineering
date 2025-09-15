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

## dbt Workflow
1. Create the project using `dbt init <project_name>`.
2. Define data sources in the `profiles.yml` file.
3. Create or use existing models or templates in the `models` directory.
4. Run the models using `dbt run`.
5. Test the models using `dbt test`.
6. Generate and serve documentation using `dbt docs generate` and `dbt docs serve
7. Schedule and automate dbt runs using tools like Airflow or dbt Cloud.

### dbt run 
- It is the subcommand that performs the data transformations and pushes updates to the data warehouse.
- It should be executed whenever there are model changes, or when the data process needs to be materialized.
- Materialized in dbt means to execute the transformations on the source data and place the data into the target tables or views in the data warehouse.

## dbt model
- A dbt model represents the various transformations and data manipulations that are performed on the raw source datasets. They are written in SQL, though newer versions of dbt also support Python models/transformations.
- Each model is defined in a separate SQL file within the `models` directory and are saved in a text file with a `.sql` extension. dbt automatically compiles these SQL files into executable SQL statements that are run against the data warehouse.

### Simple dbt model example
```bash
mkdir models/order
touch models/order/customer_orders.sql
```
```sql
SELECT
    first_name,
    last_name,
    shipping_address,
    item_quantity
FROM source_table
```
```
dbt run
```

### Parquet files
- Parquet is a columnar storage file format optimized for use with big data processing frameworks.
- DuckDB can read and write Parquet files, making it easy to work with large datasets in a structured format.
- Example of loading a Parquet file in DuckDB:
```sql
SELECT * FROM read_parquet('file.parquet'); or
SELECT * FROM 'file.parquet';
```

### Updating dbt models
- dbt helps make changes to a project without writing new queries from scratch.

Updating a workflow involves:
1. Checking out from the source control system (e.g., Git).
2. Finding the model to be updated in the `models` directory.
3. Updating the SQL code in the model file.
4. Regenerating the model with `dbt run` or `dbt run -f` to force a full refresh.

Changes can also be made to the `dbt_project.yml` file to adjust configurations, such as materialization strategies or model paths.

The `model_properties.yml` file should be updated to reflect any changes in model dependencies or descriptions.

## Documentation
- dbt provides built-in documentation features that allow users to document models, sources, and tests

Some commands:
- `dbt docs generate`: Generates the documentation site.
- `dbt docs serve`: Serves the documentation site locally for easy access and sharing.
- `dbt docs -help`: Provides help and usage information for the documentation commands.

To document a model:
1. Add documentation blocks in the model SQL files using Jinja syntax.
2. Use the `dbt run` command to generate the models.
3. Use `dbt docs generate` to generate the documentation files.
4. Copy the content to a hosting service.
5. Access the documentation site via a web browser.

## Jinja templates
- Jinja is a templating engine for Python that allows for dynamic generation of SQL code in dbt models.
- It enables users to create reusable SQL snippets, control flow, and logic within their dbt projects.
- Jinja templates are written using double curly braces `{{ }}` for expressions and `{% %}` for statements.

Example of a Jinja template in a dbt model:
```sql
SELECT
    {{ column_name }},
    COUNT(*) AS count
FROM {{ source('my_source', 'my_table') }}
GROUP BY {{ column_name }}
```

dbt Jinja functions:
- `ref()`: References another dbt model.
- `source()`: References a source table defined in the `sources` section of the project
- `config()`: Configures model properties such as materialization and file paths.
- `var()`: Accesses variables defined in the `dbt_project.yml` file or
in the command line.
- `log()`: Logs messages during dbt runs for debugging purposes.
- `if`, `for`, `else`: Control flow statements for conditional logic and loops.
- `set`: Assigns values to variables within the template.
- `macro`: Defines reusable SQL snippets that can be called within models or other macros.
- `run_query()`: Executes a SQL query and returns the result, useful for dynamic SQL generation.
- `exceptions`: Handles errors and exceptions in Jinja templates.
- `load_result()`: Loads the result of a SQL query into a variable for further processing.
- `return`: Returns a value from a macro or function.
- `do`: Executes a statement without returning a value, useful for side effects.
- `modules`: Imports external Python modules for use in Jinja templates.
- `from`: Imports specific functions or classes from a module.
- `as`: Aliases a module or function for easier reference.

Without Jinja;
```sql
SELECT
    first_name,
    last_name,
    shipping_address,
    item_quantity
FROM source_table
```

With Jinja;
```sql
SELECT
    {{ first_name }},
    {{ last_name }},
    {{ shipping_address }},
    {{ item_quantity }}
FROM {{ source('my_source', 'source_table') }}
```

## Hierarchical models
- A hierarchy represents the dependencies between models in a dbt project; the relationship between source and transformed data.
- Models can depend on other models, creating a directed acyclic graph (DAG) of transformations.
- Hierarchies are defined using the Jinja template language within the model definition files. The `ref()` function is used to reference other models, establishing dependencies.
- To define a dependency, we replace the table name in the query with two opening curly braces, then the `ref()` function, and finally the model name in single quotes, followed by two closing curly braces.

```sql
SELECT
    customer_id,
    order_id,
    order_date
FROM {{ ref('stg_orders') }}
```

## Testing in dbt
- A test is an assertion or validation of various dbt objects such as models, seeds, sources. Tests verify that the data is as expected.
- Built-in tests include; `unique` to verify all values are unique, `not_null` to verify all values are not null, `accepted_values` to verify all values are within a specific list, `relationships` to verify a connection to a specific table / column. 
- Model tests are defined in a YAML file within the models directory while other tests are defined in their respective directories. An example of the YAML structure for model tests:
```yaml
version: 2
models:
    - name: my_model
        description: "This is my model"
        columns:
            - name: id
            description: "The unique identifier for each record"
            tests:
                - unique
                - not_null
            - name: status
            description: "The status of the record"
            tests:
                - accepted_values:
                    values: ['active', 'inactive', 'pending']
            - name: foreign_key_id
            description: "The foreign key to another table"
            tests:
                - relationships:
                    to: ref('another_model')
                    field: id
```
- To run tests, use the command `dbt test`, which executes all defined tests and reports any failures or issues or `dbt test --select model_name` to run tests for a specific model.

### Finding failing tests
- When a test fails, dbt provides detailed information about the failure, including the model name. To find the specific issues in our data, we need to use the complied SQL code. This normally resides in the `target/compiled/<project_name>/models/model_properties.yml` directory.

### Singular test
A singular test is a custom data test within dbt, written as a SQL query, which returns the failing rows. 

An example of a singular test:
```sql
SELECT *
FROM {{ ref('my_model') }}
WHERE id IS NULL
```

Test debugging can be done using a SQL editor to create the initial test query, place the query in a `.sql` file in the `tests` directory, and run the test using `dbt test --select test_name`. Finally, check any errors and update the test as needed.

### Reusable tests
Reusable tests are custom tests that can be defined once and applied to multiple models or columns. It is created using Jinja templates and stored in the `tests/generic` directory.

A reusable test must be defined for each model that uses it in the `model_properties.yml` file.

```yaml
{% test check_gt_0(model, column_name) %}
    SELECT *
    FROM {{ model }}
    WHERE {{ column_name }} > 0
{% endtest %}
```

A reusable test can be applied to a model column as follows:
```yaml
version: 2
models:
    - name: my_model
        columns:
            - name: amount
            tests:
                - check_gt_0
```

Additional parameters can be passed to the reusable test as follows:
```yaml
{% test check_columns_unequal(model, column_a, column_b) %}

    SELECT *
    FROM {{ model }}
    WHERE {{ column_a }} = {{ column_b }}
    
{% endtest %}
```