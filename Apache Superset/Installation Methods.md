# Installation Methods

When it comes to determining the best installation method depends on the fundamental trade-off between you needing to do more of the detail work yourself versus having more of the configuration and setup abstracted away for you.

## Docker Compose

### Summary

This method takes advantage of containerization while remaining simpler than Kubernetes. It is the best way to try out Superset; while also being useful for developing & contributing back to Superset.

If you're not just demoing the software, you'll need a moderate understanding of Docker to customize your deployment and avoid a few risks. Even when fully-optimized this is not as robust a method as Kubernetes when it comes to large-scale production deployments.

You manage a superset-config.py file and a docker-compose.yml file. Docker Compose brings up all the needed services - the Superset application, a Postgres metadata DB, Redis cache, Celery worker and beat. They are automatically connected to each other.

### Responsibilities

You will need to back up your metadata DB. That could mean backing up the service running as a Docker container and its volume; ideally you are running Postgres as a service outside of that container and backing up that service.

You will also need to extend the Superset docker image. The default `lean` images do not contain drivers needed to access your metadata database (Postgres or MySQL), nor to access your data warehouse, nor the headless browser needed for Alerts & Reports. You could run a `-dev` image while demoing Superset, which has some of this, but you'll still need to install the driver for your data warehouse. The `-dev` images run as root, which is not recommended for production.

Ideally you will build your own image of Superset that extends `lean`, adding what your deployment needs. See [Building your own production Docker image](https://superset.apache.org/docs/installation/docker-builds/#building-your-own-production-docker-image).

The documentation for installing Superset via Docker Compose can be found [here](https://superset.apache.org/docs/installation/docker-compose).

## Kubernetes (K8s)

### Summary

This is the best way to deploy a production instance of Superset, but has the steepest skill requirements - someone who knows Kubernetes.

We will deploy Superset into a K8s cluster. The most common method is using the community-maintained Helm chart, though work is underway to implement [SIP-149 - a Kubernetes Operator for Superset](https://github.com/apache/superset/issues/31408).

### Responsibilities

You will need to build your own Docker image, and back up your metadata DB, both as described in Docker Compose above. You'll also need to customize your Helm chart values and deploy and maintain your Kubernetes cluster.

The documentation for running Superset on Kubernetes can be found [here](https://superset.apache.org/docs/installation/kubernetes).

## PyPI (Python)

### Summary

This method requires no knowledge of containers. It requires the most hands-on work to deploy, connect, and maintain each component. 

We install Superset using `pip` into a Python virtual environment. We then need to install and configure each of the other components ourselves - metadata DB, caching layer, worker & beat.

### Responsibilities

You will need to get the component services running and communicating with each other. You'll need to arrange backups of your metadata database.

When upgrading, you'll need to manage the system environment and packages and ensure all components have functional dependencies.

The documentation for installing Superset via PyPI can be found [here](https://superset.apache.org/docs/installation/pypi).