# Upgrading Superset

## Docker Compose

To upgrade a Superset instance installed via Docker Compose, we need to follow these steps:

First, shut down the running containers in Docker Compose:

```bash
docker-compose down
```

Next, update the folder that mirrors the `superset` repository through `git`:

```bash
git pull origin master
```

Then, restart the containers and any changed Docker images will be automatically pulled down:

```bash
docker-compose up
```

### Updating Superset Manually

To upgrade superset in a native installation, run the following commands

```bash
pip install apache-superset --upgrade
```

### Upgrading the Metadata Database

Migrate the database by running:

```bash
superset db upgrade
superset init
```

While upgrading superset should not delete your charts and dashboards, we recommend following best practices and to backup your metadata database before upgrading. Before upgrading production, we recommend upgrading in a staging environment and upgrading production finally during off-peak usage.

