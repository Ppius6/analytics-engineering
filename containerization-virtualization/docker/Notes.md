# Docker

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
FROM ubuntu:22.04
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

Next, we customize the image using the RUN instruction. The RUN instruction allows us to execute commands inside the image during the build process. This is useful for installing dependencies, configuring settings, and setting up the environment.

```
FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
```

`apt-get update` is a package manager than allows us to install all kinds of software on Ubuntu. The `-y` flag is used to automatically answer "yes" to any prompts that may arise during the installation process.

## Managing files in Docker images

The `COPY` instruction is used to copy files from the host machine to the Docker image. This is useful for adding application code, configuration files, and other resources to the image.

```
FROM ubuntu
COPY <src-path-on-host> <dest-path-in-image>
```
If the destination path does not exist, the original filename is used. Similarly, not specifying a filename in the src path will copy all the file contents.

```
COPY /projects/pipeline_v3/pipeline.py /app/
```

``` 
COPY <src-folder> <dest-folder>
```

Instead of copying files from a local directory, files are often downloaded in the image build:

```
-- Download the file
RUN curl <file-url> -o <dest-path-in-image>

-- Unzip the file
RUN unzip <dest-folder>/<filename>.zip

-- Remove the zip file
RUN rm <dest-folder>/<filename>.zip
```

Each download instructions adds to the total size of the image. To reduce the image size, we can chain multiple commands together using `&&`:

```
RUN curl <file-url> -o <dest-path-in-image> && \
    unzip <dest-folder>/<filename>.zip && \
    rm <dest-folder>/<filename>.zip
```

## Start command
The `CMD` instruction is used to specify the command that will be executed when a container is started from the image. This is useful for setting the default behavior of the container.

```
FROM ubuntu
CMD ["echo", "Hello, World!"]
CMD python 3 my_script.py
```

We can override the default start command when running the container using the `docker run` command:

```
docker run <image_name> <new_command>
docker run my-app python my_script.py
```

## Docker caching
When building a Docker image, Docker uses a caching mechanism to speed up the build process. Each instruction in the Dockerfile creates a new layer in the image, and Docker caches these layers to avoid rebuilding them if they have not changed.

For example, if we have a Dockerfile with the following instructions:

```
FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
COPY . /app
```

When we build the image for the first time, Docker will execute each instruction and create a new layer for each one. If we make a change to the `COPY` instruction and rebuild the image, Docker will only re-execute the `COPY` instruction and create a new layer for it. The previous layers will be cached and reused, which speeds up the build process.

However, if we make a change to the `RUN` instruction that installs Python, Docker will re-execute that instruction and create a new layer for it. The previous layers will still be cached and reused, but the layer for the `RUN` instruction will be rebuilt.

To force Docker to ignore the cache and rebuild all layers, we can use the `--no-cache` option when building the image:

```
docker build --no-cache -t <image_name> .
```

This will ensure that all instructions in the Dockerfile are executed and all layers are rebuilt, regardless of whether they have changed or not.

## Changing the user and working directory

By default, Docker containers run as the root user. However, for security reasons, it is often recommended to run containers as a non-root user. We can change the user that the container runs as using the `USER` instruction in the Dockerfile.

```
FROM ubuntu
USER repl
RUN apt-get update
RUN apt-get install -y python3
```
In this example, the container will run as the `repl` user instead of the root user. We can also create a new user using the `RUN` instruction before changing the user.

```
FROM ubuntu
RUN useradd -ms /bin/bash newuser
USER newuser
RUN apt-get update
RUN apt-get install -y python3
```

We can also change the working directory of the container using the `WORKDIR` instruction. This sets the default directory for any subsequent instructions in the Dockerfile.

```
FROM ubuntu
WORKDIR /app
COPY . /app
RUN apt-get update
RUN apt-get install -y python3
CMD ["python3", "my_script.py"]
```

In this example, the working directory is set to `/app`, and any subsequent instructions will be executed in that directory. This is useful for organizing files and ensuring that the container runs in the correct context.

## Variables in Dockerfiles

Using variables in Dockerfiles can help make them more flexible and easier to maintain. We can define variables using the `ARG` instruction, which allows us to pass values to the Dockerfile at build time.

```
ARG <variable_name>=<default_value>
```

For example, ARG path=/home/repl

To use in the Dockerfile, we can reference the variable using the `$` symbol:

```
FROM ubuntu
ARG path=/home/repl
WORKDIR $path/app
COPY . $path/app
RUN apt-get update
RUN apt-get install -y python3
CMD ["python3", "my_script.py"]
```

We can also use the `ENV` instruction to set environment variables that will be available to the container at runtime.

```
ENV <variable_name>=<value>
```
For example, ENV PORT=8080

We can reference the environment variable in the Dockerfile using the `$` symbol:

```
FROM ubuntu
ENV PORT=8080
EXPOSE $PORT
CMD ["python3", "my_script.py"]
```

In this example, the `PORT` environment variable is set to `8080`, and the `EXPOSE` instruction uses the variable to specify the port that the container will listen on.

When building the Docker image, we can override the default value of an `ARG` variable using the `--build-arg` option:

```
docker build --build-arg <variable_name>=<value> -t <image_name> .
```

## Creating Secure Docker Images

 