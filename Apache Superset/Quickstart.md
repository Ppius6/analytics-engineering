# Apache Superset

## Quickstart

First, we need to have `Docker`, `Docker Compose`, and `Git` installed on our local machine.

1. Clone the Apache Superset repository:

   ```bash
   git clone https://github.com/apache/superset
   ```

2. Start the latest official release of Superset using Docker Compose:

   ```bash
   # Enter the superset directory we just cloned
   $ cd superset

   # Set the repository to the state associated with the latest official version
   $ git checkout tags/5.0.0

   # Fire up Superset using Docker Compose
   $ docker-compose -f docker-compose-image-tag.yml up
   ```

Then we wait for Docker Compose to fetch the underlying container images and load up some examples. 

Note: If we get an error message like `validating superset\docker-compose-image-tag.yml: services.superset-worker-beat.env_file.0 must be a string`, we need to update our version of `docker compose`.

3. Login to Superset:

   Open a web browser and navigate to `http://localhost:8088`. Use the default credentials:

   - Username: `admin`
   - Password: `admin`

And we should be logged into the Superset dashboard! From here, we can start exploring the features of Apache Superset.
