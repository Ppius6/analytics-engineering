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

### Jinja Types
Jinja `statements` are enclosed in `{% %}`. 

```
{% set order_statuses = ['Shipped', 'Complete', 'Processing'] %}
```
Jinja `expressions` are enclosed in `{{ }}`.

```
SELECT * FROM {{ ref('stg_orders') }}
```

Jinja `comments` are enclosed in `{# #}`.

```
{# This is a comment #}
```

### Jinja Statements
Jinja statements can take the forms of `set`, `loop`, conditional logic, macros, etc.

A `set` jinja statement is used to assign a value to a variable.

```sql
{% set country = 'USA' %}

SELECT * FROM {{ ref('stg_orders') }}
WHERE country = '{{ country }}'
```

Remember, Jinja statements are enclosed in `{% %}`. An example when looping through items:

Template:
```
{% for ... %} ... {% endfor %}
```

Example:
```
{% for order_status in order_statuses %}
    SUM(
        CASE WHEN status = '{{ order_status }}' 
          THEN order_id
        END
    )
{% endfor %}
```

When using SQL:
```sql
{% set order_statuses = ['Shipped', 'Complete', 'Processing'] %}

SELECT
    user_id,
    -- Jinja loop
    {% for order_status in order_statuses %}
        SUM(
            CASE WHEN status = '{{ order_status }}' THEN 1 ELSE 0 END) 
            -- Parametrized column name
            AS num_orders_{{ order_status }}
    {% endfor %}
FROM {{ ref('stg_orders') }}
GROUP BY 1
```

### Jinja Macros

Macros are reusable SQL snippets that can be defined once and used multiple times throughout a dbt project. They are defined in `.sql` files within the `macros` directory of a dbt project.

They are helpful in combining multiple SQL functions into one. For example, `ROUND()`, and `COALESCE()` are often used together for data cleaning. The `COALESCE()` function is used to handle null values by replacing NULL values with the first non-null value.

A macro always starts with `macro` and ends with `endmacro`.

```sql
{% macro clean_number(column_name) %}
    ROUND(COALESCE({{ column_name }}, 0), 2)
{% endmacro %}
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

## DBT Sources
Sources in dbt represent the ability to name and describe data loaded by the EL process. It is more of applying extra information to the data that is already in the warehouse. Note that dbt only handles the T (transform) in ELT.

dbt sources are present to provide data lineage information. Data lineage describes the flow of data in a data warehouse which helps in validation, troubleshooting, and understanding the data.

To give access a given source, we use the Jinja `source()` function in our model SQL files. The `source()` function takes two arguments: the source name and the table name.

```sql
SELECT *
FROM {{ source('my_source', 'my_table') }}
```

Defining sources in dbt, we use a YAML file which can be the models/model_properties.yml file or a separate file in the models directory.

Note that when it is named model_properties.yml, dbt only looks for a yml file for this information. The actual definition goes in the sources section of the yml file. 

When defining a source;
- Name the source starting with a `- name: <source_name>` option. This is usually the name of the database or schema.
- Then define each source table with a `-name` option under the `tables:` section.

Example of defining a source in a YAML file:
```yaml
version: 2

sources:
    - name: raw
      tables: 
        - name: phone_orders
        - name: web_orders
```

Note: This differs based on the data warehouse type.

### Accessing sources
To access a source in a dbt model, we use the `source()` function within the SQL code of the model. The `source()` function takes two arguments: the source name and the table name.

The function returns the proper name to access the source table in the data warehouse.

Example of accessing a source in a dbt model:
```sql
SELECT *
FROM {{ source('raw', 'phone_orders') }}
UNION
SELECT *
FROM {{ source('raw', 'web_orders') }}
```

After being compiled, the SQL code will look like this:
```sql
SELECT *
FROM raw.phone_orders
UNION
SELECT *
FROM raw.web_orders
```

### Testing sources
dbt allows us to define tests for sources to ensure data quality and integrity. Source tests are defined in the same YAML file where the sources are defined.

Example of defining tests for a source in a YAML file:
```yaml
version: 2

sources:
    - name: raw
      tables: 
        - name: phone_orders
          tests:
            - not_null:
                column_name: order_id
            - unique:
                column_name: order_id
        - name: web_orders
          tests:
            - not_null:
                column_name: order_id
            - unique:
                column_name: order_id
```
## dbt seeds

These are CSV files that can be loaded into the data warehouse as tables. They are useful for small, static datasets that are needed for analysis or reference.

They are not meant to contain raw data or data exported from another process.

Why do we need to use seeds?
- CSV files are relatively easy to create and maintain.
- They can be edited manually if needed, copied, etc.
- They are easy to use, whether in development, testing, or production environments.
- Finally, they are text, which makes them easy to version control.

To define a seed in dbt;
1. Add the CSV file to the `seeds` subdirectory within the dbt project directory. 
2. Ensure the header is the first row of the CSV file, as it will be used to define the column names in the resulting table.
3. Once ready, use the command `dbt seed` to load the CSV file into the data warehouse as a table.
4. Run the `dbt seed` to complete the process.

Further configuration can be added such as which schema and database to use, options, datatypes to assign the columns, etc. This is done in the `dbt_project.yml` file.

### Defining datatypes for seeds
To define datatypes for seed columns, we can specify the datatypes in the `dbt_project.yml` file under the `seeds` section. If not specified, dbt will infer the datatypes based on the data in the CSV file.

```yaml
version: 2

seeds:
  - name: zipcodes
    config:
      column_types:
        zipcode: varchar(10)
        city: varchar(50)
        state: varchar(2)
        population: integer
``` 

### Tests in seeds
Tests can be defined for seed tables in the same way as for models and sources. The tests are defined in the `model_properties.yml` file or a separate YAML file in the models directory.

```yaml
version: 2

seeds:
  - name: zipcodes
    config:
      column_types:
        zipcode: varchar(10)
    columns:
      - name: zipcode
        tests:
          - unique
          - not_null
```
### Accessing seeds
To access a seed table in a dbt model, we use the `ref()` function within the SQL code of the model. The `ref()` function takes one argument: the name of the seed table.

```sql
SELECT *
FROM {{ ref('zipcodes') }}
```

## Snapshots 
Slowly changing dimensions (SCD), mostly type 2, are used to manage and track changes to data over time. They are particularly useful for historical analysis and auditing purposes.

Snapshots in dbt allow us to capture the state of a table at a specific point in time and store it as a separate table in the data warehouse. This enables us to track changes to the data over time and analyze historical trends.

dbt tracks changes using snapshots, by adding extra columns to the output; `dbt_valid_from` and `dbt_valid_to` to indicate the time range during which a particular record was valid. Additionally, a `dbt_is_current` column is added to indicate whether a record is the most recent version.

To implement a snapshot in dbt:
1. Create a `snapshots` directory within the dbt project directory if it doesn't already exist.
2. Create a new SQL file in the `snapshots` directory to define the snapshot.
3. Use the `snapshot` block to define the snapshot, specifying the source table, unique key, and any additional columns to track.
4. Run the `dbt snapshot` command to create the snapshot table in the data warehouse.

Example of defining a snapshot in dbt:
```sql
{% snapshot customer_snapshot %}

    {{
        config(
            target_schema='snapshots',
            unique_key='customer_id',
            strategy='timestamp',
            updated_at='last_updated'
        )
    }}

    SELECT
        customer_id,
        first_name,
        last_name,
        email,
        last_updated
    FROM {{ source('raw', 'customers') }}

{% endsnapshot %}
```

## Automation with dbt build

`sources` and `seeds` feed initial data to dbt. `models` handle the transformation of data (usually from `sources` and `seeds`) for downstream consumption. We can then use `tests` to validate the data in `models`, `sources`, and `seeds`. `snapshots` are used to track changes in data over time.

Now, `dbt build` is a command that combines several dbt commands into a single command to streamline the workflow in a production environment. It combines various tasks, such as `dbt run`, `dbt test`, `dbt seed`, and `dbt snapshot`, into a single command.

Note: `dbt build` does not perform `dbt docs` operations.

`dbt build` is used because it simplifies the workflow by reducing the number of commands that need to be run manually. It ensures that all necessary steps are executed in the correct order, reducing the risk of errors or omissions.

It may not be needed for the testing and development phase, but it is very useful in production environments where consistency and reliability are crucial.

`dbt build` options include:
- `dbt build --select <object>`: To build specific objects (models, tests, seeds, snapshots) instead of the entire project.
- `dbt build -d` for debug mode, which provides detailed logging information during the build process.
- `dbt build --exclude <object>`: To exclude specific objects from the build process.

## Building a dbt project pipeline
1. Initialize a new dbt project using `dbt init <project_name>`.
2. Configure the `profiles.yml` file with the connection details for the data warehouse.
3. Define data sources in the `sources` section of a YAML file within the `models` directory.
4. Create seed files in the `seeds` directory and configure them in the `dbt_project.yml` file.
5. Develop models in the `models` directory using SQL and Jinja templating.
6. Define tests for models, sources, and seeds in a YAML file within the `models` directory.
7. Create snapshots in the `snapshots` directory to track changes in data over time.
8. Use `dbt build` to automate the entire workflow, ensuring that all steps are executed in the correct order.
9. Schedule and automate dbt runs using tools like Airflow or dbt Cloud for regular data updates and maintenance.
10. Monitor the dbt runs and review logs for any errors or issues that may arise during the process.
11. Generate and serve documentation using `dbt docs generate` and `dbt docs serve` to provide insights into the data models and their relationships.
12. Continuously update and maintain the dbt project as data requirements evolve, ensuring that models, tests, and documentation remain accurate and up-to-date.

## Additional Resources
- [dbt Learn](https://learn.getdbt.com/)
- [dbt Slack Community](https://www.getdbt.com/community/join-the-community/)
- [dbt YouTube Channel](https://www.youtube.com/c/dbtlabs)
- [dbt Blog](https://blog.getdbt.com/)