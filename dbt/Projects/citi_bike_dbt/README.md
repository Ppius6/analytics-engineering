# Citi Bike Analytics dbt Project

This dbt project analyzes Citi Bike trip data to provide insights into bike sharing patterns, station usage, and rider behavior.

## Project Overview

The project transforms raw Citi Bike trip data through a series of staging, intermediate, and mart models to create analytics-ready datasets.

### Data Architecture

```text
Raw Data (seeds/trips_2024.csv)
    ↓
Staging (stg_rides)
    ↓
Intermediate (int_rides_with_duration)
    ↓
Marts (dim_stations, fct_rides_daily)
```

## Models

### Staging

- **stg_rides**: Cleaned and standardized trip data with proper data types

### Intermediate

- **int_rides_with_duration**: Enhanced trip data with calculated duration, distance, and ride categorization

### Marts

- **dim_stations**: Dimension table with unique station information
- **fct_rides_daily**: Daily aggregated ride metrics and statistics

## Getting Started

### Prerequisites

- Python 3.7+
- dbt-core
- dbt-duckdb

### Setup

1. Activate your virtual environment:

   ```bash
   source ../../../dbt-venv/bin/activate
   ```

2. Install dependencies (if not already installed):

   ```bash
   pip install dbt-core dbt-duckdb
   ```

3. Load seed data:

   ```bash
   dbt seed
   ```

4. Run the models:

   ```bash
   dbt run
   ```

5. Test the models:

   ```bash
   dbt test
   ```

### Documentation

Generate and serve documentation:

```bash
dbt docs generate
dbt docs serve
```

## Data Sources

- **trips_2024.csv**: Raw Citi Bike trip data for 2024 containing ride details, timestamps, and station information

## Key Metrics

- Daily ride counts by membership type
- Average ride duration and distance
- Station popularity and usage patterns
- Ride categorization (short/medium/long)

## Database

This project uses DuckDB as the data warehouse, with the database file located at `dev.duckdb`.

## Resources

- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
