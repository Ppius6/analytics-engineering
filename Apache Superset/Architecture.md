# Architecture

## Components

A Superset installation is made up of these components:

1. The Superset application itself.
2. A metadata database to store Superset's internal data (e.g., users, dashboards, charts).
3. A caching layer, optional but necessary for some features.
4. A worker & beat, optional but necessary for some features.

## Optional components and associated features

The optional components above are necessary for the following features:

  - Alerts and Reports
  - Caching
  - Async Queries
  - Dashboard Thumpnails

If we install with Kubernetes or Docker Compose, all of these components will be included. However, if we install with `PyPI`, only the application will be created. Using `PyPI` will require us to configure a caching layer, worker, and beaty separately if we want to use the features above.

## The Superset application

This is the core application. Superset operates like this:

  - A user visits a chart or dashboard
  - That triggers a SQL query to the data warehouse holding the underlying data
  - The resulting data is served up in a data visualization
  - The Superset application is comprised of the Python (Flask) backend application (server), API layer, and the React frontend application (client), built via Webpack, and static assets needed for the application to work.

## Metadata database

This is where chart and dashboard definitions, user information, logs, etc. are stored. Superset is tested to work with PostgreSQL and MySQL databases as the metadata database (not to be confused with a data source, i.e., data warehouse).

Some installation methods like our Quickstart and PyPI come configured with a `SQLite` on-disk database. And in a Docker Compose installation, the data would be stored in a PostgreSQL container volume. 

However, neither of these are suitable for production use. For production, we should set up a dedicated PostgreSQL or MySQL database and configure Superset to use that instead.

## Caching layer

The caching layer serves two main functions:

  - Store the results of queries to your data warehouse so that when a chart is loaded twice, it pulls from the cache the second time, speeding up the application and reducing load on your data warehouse.
  - Act as a message broker for the worker, enabling the Alerts & Reports, async queries, and thumbnail caching features.

  Most people use `Redis` as their caching layer, but Superset supports other options such as `Memcached`, `SimpleCache` (in-memory), or the local filesystem. Other custom cache backends can be implemented as well.

## Worker & Beat

This is one or more workers who execute tasks like run async queries or take snapshots of reports and send emails, and a "beat" that acts as the scheduler and tells workers when to perform their tasks. 

Most installations use `Celery` as the worker framework, with `Redis` as the message broker. Other message brokers are also supported, such as `RabbitMQ`.

## Other Components

Other components can be incorporated into Superset. Further [details](https://superset.apache.org/docs/configuration/configuring-superset/) etails can be found here.

For instance, we could set up a load balancer or reverse proxy to implement HTTPS in front of our Superset application, or specify a Mapbox URL to enable geospatial charts, etc.

Superset won't even start without certain configuration settings established, so it is essential to review that page.