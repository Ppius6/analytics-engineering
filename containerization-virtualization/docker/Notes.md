## The Docker CLI

On the command line, we can send instructions to the Docker daemon using the Docker CLI (Command Line Interface). The CLI is a command-line tool that allows users to interact with Docker and manage containers, images, networks, and volumes.

Some common Docker CLI commands include:
- `docker run`: This command is used to create and start a new container from a specified
    image. For example, `docker run hello-world` will create and start a container that runs the "hello-world" image.
- `docker ps`: This command lists all running containers. Adding the `-a` flag (`docker ps -a`) will show all containers, including those that are stopped.
- `docker run -it <image_name>`: This command runs a container in interactive mode with a terminal session, allowing users to interact with the container's shell.
- `docker run -d <image_name>`: This command runs a container in detached mode, allowing it to run in the background.
- `docker stop`: This command stops a running container. For example, `docker stop <container_id>` will stop the container with the specified ID.
- `docker rm`: This command removes a stopped container. For example, `docker rm <container_id>` will remove the container with the specified ID.
- `docker images`: This command lists all available Docker images on the local machine. 
- `docker run --name <container_name> <image_name>`: This command allows users to specify a custom name for the container being created.
- `docker stop <container_name>`: This command stops a running container using its custom name.
- `docker ps -f "name=<container_name>"`: This command filters the list of running containers to show only those with the specified name.
- `docker logs <container-id or container_name>`: This command retrieves the logs of a specified container, which can be useful for debugging and monitoring purposes.
- `docker logs -f <container-id or container_name>`: This command follows the logs of a specified container in real-time, allowing users to see new log entries as they are generated.
- `docker container rm <container-id or container_name>`: This command removes a specified container from the system.
- `docker container prune`: This command removes all stopped containers from the system, freeing up disk space.

## Managing local docker images

### Pulling an image
- `docker pull <image_name>` or `docker pull <image_name>:<image-version>`: This command downloads a Docker image from a registry (such as Docker Hub) to the local machine. The optional `<image-version>` tag allows users to specify a specific version of the image to pull.

### Building an image
- A Docker image can be built using a Dockerfile, which is a text file that contains a series of instructions for building the image. The `docker build` command is used to create an image from a Dockerfile.
- `docker build -t <image_name> .`: This command builds a Docker image from a Dockerfile in the current directory and tags it with the specified name.
- `docker images`: This command lists all available Docker images on the local machine, along with their repository names, tags, image IDs, creation dates, and sizes.
- `docker image rm <image_name>`: This command removes a specified Docker image from the local machine, either by its name or image ID.

### Cleaning up unused resources
- Over time, unused Docker images, containers, and other resources can accumulate on the local machine, taking up disk space. The following commands can be used to clean up these unused resources:
- `docker container prune`: This command removes all stopped containers from the local machine, freeing up disk space.
- `docker image prune`: This command removes all unused Docker images from the local machine, freeing up disk space.
- `docker system prune`: This command removes all unused data, including stopped containers, unused images, and unused networks, from the local machine, freeing up disk space.

### Dangling images
- Dangling images are layers that have no relationship to any tagged images. They are created when an image is built and a new layer is created, but the previous layer is no longer needed.
- To remove dangling images, you can use the following command:
- `docker image prune`: This command removes all dangling images from the local machine, freeing up disk space.
- `docker image prune -a`: This command removes all unused images, not just dangling ones, from the local machine, freeing up disk space.

## Distributing Docker images
Docker images can be distributed through Docker registries, which are repositories for storing and sharing Docker images. The most commonly used registry is Docker Hub, but private registries can also be set up for internal use.

To push an image to a registry, you can use the following command: `docker image push <image_name>`: This command uploads a Docker image to a specified registry, making it available for others to pull and use.
When pushing an image to a registry, it is important to ensure that the image is properly tagged with the registry URL and repository name. For example:
`docker tag <image_name> <registry_url>/<repository_name>:<tag>`: This command tags a Docker image with the specified registry URL, repository name, and tag, preparing it for pushing to the registry.
`docker image push <registry_url>/<repository_name>:<tag>`: This command pushes the tagged image to the specified registry, making it available for others to pull.
The image can be pulled from a private registry using the same `docker pull` command, but with the full registry URL included: `docker pull <private-registry_url>/<image_name>`

For official docker images, authentication is not needed. However, for private docker repositories, the owner can choose to require authentication. In such cases, users must log in to the registry using the following command:
- `docker login <registry_url>`: This command prompts the user for their username and password to authenticate with the specified registry. Once authenticated, users can push and pull images from the private registry.

Additionally, a docker image can be sent as a file especially when sending it to a few people. This can be done using the `docker save` command: `docker save -o <output_file.tar> <image_name>`

To load a docker image from a file, you can use the `docker load` command: `docker load -i <input_file.tar>`

## Creating Docker Images
Docker images are the recipes or blueprints for Docker containers. To create the blueprint, we must write down a list of instructions in a file called a Dockerfile. The Dockerfile contains a series of commands that specify how to build the image, including the base image, dependencies, and configuration.

Besides, the file should be named `Dockerfile` for Docker to recognize it. The Dockerfile should be placed in the root directory of the project or in a specific directory where the image will be built.

### Starting a Dockerfile
A Dockerfile always start from another image, specified using the `FROM` instruction. 

```
FROM postgres
FROM ubuntu
FROM hello-world
FROM my-custom-data-pipeline
```

```
FROM postgres:15.0
FROM ubutnu:22.04
FROM hello-world:latest
FROM my-custom-data-pipeline:v1
```

Then, we can create an image from the Dockerfile using the `docker build` command. This is the followed by the location of the Dockerfile we want to build. If our Dockerfile is in the current folder, we can use a dot (`.`) to represent the current directory. 

When running the `docker build` command, in the last line of the output, we can see the id or hash assigns the new image. The new hash starts by indicating its type, sha256, followed by a long string of alphanumeric characters. 

```
docker build /location/to/Dockerfile
docker build .
```

If we want to give our image a name, we can use the `-t` or `--tag` option followed by the desired name. 

```
docker build -t <image_name> .
docker build --tag <image_name> .
```

We can also add a version tag to the image name using a colon (`:`) followed by the version number. If no version is specified, Docker will assign the `latest` tag by default.

```
docker build -t <image_name>:<version> .
docker build --tag <image_name>:<version> .
```
