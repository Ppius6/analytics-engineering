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

## Temporary Containers

Temporary containers are often used for tasks such as testing, debugging, or running one-off commands without the need to create a persistent container. These containers are created, run, and then removed automatically after their execution.

To create a temporary container, we can use the `docker run` command with the `--rm` option. This option ensures that the container is removed automatically after it stops running.

```
docker run --rm <image_name> <command>
```
For example, if we want to run a temporary container from the `ubuntu` image and execute the `echo` command, we can use the following command:

```
docker run --rm ubuntu echo "Hello, World!"
```
This command will create a temporary container from the `ubuntu` image, execute the `echo "Hello, World!"` command, and then remove the container once the command has completed.
 
## Mounting the host filesystem

Each container has its own filesystem, which is based on the image it was created from. Changes can be made to the filesystem but are tied to that instance only. If we restart the container, the changes will stay, but only for that specific instance and would not apply to other instances of the same container image.

Rather than modifying the contents of our running containers or always creating new Docker images, we can attach files or directories from the host system to the container. This would allow for the persistence of data, whether log files, database files, or configuration files, without the need to maintain the container image itself.

We can use Docker to upgrade the container to a newer version but safely keep all of our data separate, a technique known as `bind-mount`. It can be read-only, where the container can only read the files but not change them. 

To mount a file or directory from the host system into a container, we can use the `-v` or `--mount` option with the `docker run` command. The syntax for mounting a volume is as follows:

```
docker run -v <source>:<destination> <image_name>
```

Example:
```
docker run -v ~/html:/var/www/html my-web-server
```

In this example, the `~/html` directory on the host system is mounted to the `/var/www/html` directory inside the container. Any changes made to files in the `~/html` directory on the host will be reflected in the `/var/www/html` directory inside the container, and vice versa.

## Persistent volumes

Volumes are an option to store data in Docker, unrelated to the container image or host filesystem. They are managed from the command line, or API, can share with multiple containers.

They are higher performance than using bind-mounts and do exist until removed, even if no containers are using them.

To create a volume, we can use the `docker volume create` command:

```
docker volume create <volume_name>
```

To list all volumes, we can use the `docker volume ls` command:

```
docker volume ls or docker volume list
```

To inspect a volume, we can use the `docker volume inspect` command:

```
docker volume inspect <volume_name>
```

To remove a volume, we can use the `docker volume rm` command:

```
docker volume rm <volume_name>
```

To use a volume in a container, we can use the `-v` or `--mount` option with the `docker run` command. The syntax for mounting a volume is as follows:

```
docker run -v <volume_name>:<destination> <image_name>
```

For example, if we have a volume named `my-data` and we want to mount it to the `/data` directory inside a container, we can use the following command:

```
docker run -v my-data:/data my-app
```

For the volume drivers, they include the local filesystem, NFS, SMB, or CIFS. The default driver is `local`, which stores the volume data on the host filesystem.

To specify a different volume driver, we can use the `--driver` option when creating the volume:

```
docker volume create --driver <driver_name> <volume_name>
```

For example, to create a volume using the NFS driver, we can use the following command:

```
docker volume create --driver nfs my-nfs-volume
```

## Networking in Docker

Docker provides a built-in networking system that allows containers to communicate with each other and with the host system. By default, Docker creates a bridge network called `bridge`, which allows containers to communicate with each other on the same host.

A host is a general term for a computer or server that runs Docker and hosts containers. Each host has its own IP address and can run multiple containers.

A network is a group of hosts that are connected together and can communicate with each other. In Docker, networks are used to connect containers to each other and to the host system.

An interface is a connection from a host to a network such as Ethernet or Wi-Fi. An interface can be virtual, meaning it is entirely in software, or physical, meaning it is a hardware device.

A LAN is a local area network, which is a network that connects devices within a limited geographic area, such as a home or office.

A VLAN is a virtual or software-defined LAN that allows multiple virtual networks to be created on a single physical network.

An Internet Protocol is a method to connect between networks using IP addresses. IPv4 is the most commonly used version of IP, but IPv6 is becoming more widely adopted.

TCP is the Transmission Control Protocol, which is a protocol used for reliable communication between devices on a network. UDP is the User Datagram Protocol, which is a protocol used for faster, but less reliable communication between devices on a network.

Both TCP and UDP require a port value, a method to address different services on a given host via TCP or UDP. The port is a value between 0 and 65535, with ports below 1024 being reserved for well-known services. Values above 1024 are usually referred to as ephemeral ports.

HTTP is an application protocol defaulting to TCP port 80 for web communication. The secure version, HTTPS, defaults to TCP port 443. SMTP is an email transfer protocol that defaults to TCP port 25. SNMP is a network management protocol that uses UDP port 161. 

Docker has extensive networking capabilities that allow users to create custom networks, connect containers to multiple networks, and configure network settings such as IP addresses and DNS servers.

Containers can have their own IP addresses. These can be seen using the command `ifconfig` or `ip addr show <interface>` to view the interfaces and IPs assigned. The `ping -c <x> <host>` can be used to verify connectivity. The `-c` flag requires a count for the number of pings, and the host you wish to connect to, such as an IP address or a hostname.

Port mapping is a technique used to expose a container's internal ports to the host system. This allows services running inside the container to be accessed from outside the container.

To map a container's port to a host port, we can use the `-p` or `--publish` option with the `docker run` command. The syntax for port mapping is as follows:

```
docker run -p <host_port>:<container_port> <image_name>
```

For example, if we have a container running a web server on port 80 and we want to map it to port 8080 on the host system, we can use the following command:

```
docker run -p 8080:80 my-web-server
```
This command will map port 80 inside the container to port 8080 on the host system. We can then access the web server by navigating to `http://localhost:8080` in a web browser.

Exposing a port is a way to indicate that a container will listen on a specific port at runtime. This is done using the `EXPOSE` instruction in the Dockerfile.

```
EXPOSE <port_number>
```

```
FROM python:3.9
ENTRYPOINT ["python", "-mhttp.server"]
# Let the Docker engine know
# port 8000 should be available
EXPOSE 8000
```

To make a port reachable from outside the container, we must use port mapping when running the container using the `-p` or `--publish` option with the `docker run` command.

```
docker run -P <image_name>
```

To find the exposed ports, we can use the `docker inspect` command:

```
docker inspect <container_id or container_name>
```

Docker has extensive networking capabilities that allow users to create custom networks, connect containers to multiple networks, and configure network settings such as IP addresses and DNS servers.

It supports different networking types using drivers, including:
- Bridge: The default network type that allows containers on the same host to communicate with each other
- Host: A network type that allows containers to share the host's network stack
- none: A network type that disables all networking for the container

and many others, including overlay networks for multi-host communication.

`docker network ls` or `docker network list`: This command lists all available Docker networks on the local machine, along with their names, IDs, drivers, and scopes.
`docker network inspect <network_name or network_id>`: This command retrieves detailed information about a specified Docker network, including its configuration, connected containers, and IP address range.
`docker network create <network_name>`: This command creates a new Docker network with the specified name, using the default bridge driver.
`docker network create --driver <driver_name> <network_name>`: This command creates a new Docker network with the specified name and driver. For example, `docker network create --
driver overlay my-overlay-network` creates a new overlay network named "my-overlay-network".
`docker network rm <network_name or network_id>`: This command removes a specified Docker network from the local machine. Note that a network can only be removed if no containers are connected to it.
`docker network connect <network_name> <container_id or container_name>`: This command connects a specified container to a specified Docker network, allowing the container to communicate with other containers on the same network.

### jq command-line JSON processor
The `jq` command-line tool is a lightweight and flexible JSON processor that allows users to parse, filter, and manipulate JSON data from the command line. It is particularly useful for working with Docker, as many Docker commands return JSON output.

Some common `jq` commands include:
- `jq '.'`: This command pretty-prints JSON data, making it easier to read and understand.
- `jq '.[]'`: This command iterates over an array of JSON objects, returning each object on a new line.
- `jq '.[0]'`: This command retrieves the first object in an array of JSON objects.
- `jq '.key'`: This command retrieves the value of a specified key in a JSON object.
- `jq '.[].key'`: This command retrieves the value of a specified key from each object in an array of JSON objects.
- `jq 'select(.key == "value")'`: This command filters an array of JSON objects, returning only those objects where the specified key matches the specified value.
- `jq '.[].key | length'`: This command retrieves the length of the value of a specified key from each object in an array of JSON objects.
- `jq '.[].key |= "new_value"'`: This command updates the value of a specified key in each object in an array of JSON objects to a new value.
- `jq '.[].key += 1'`: This command increments the value of a specified key in each object in an array of JSON objects by 1.
- `jq '.[].key -= 1'`: This command decrements the value of a specified key in each object in an array of JSON objects by 1.
- `jq '.[].key *= 2'`: This command multiplies the value of a specified key in each object in an array of JSON objects by 2.
- `jq '.[].key /= 2'`: This command divides the value of a specified key in each object in an array of JSON objects by 2.
- `jq '.[].key // "default_value"'`: This command retrieves the value of a specified key from each object in an array of JSON objects, returning a default value if the key does not exist.
- `jq '.[].key | tostring'`: This command converts the value of a specified key from each object in an array of JSON objects to a string.
- `jq '.[].key | tonumber'`: This command converts the value of a specified key from each object in an array of JSON objects to a number.
- `jq '.[].key | @csv'`: This command converts the value of a specified key from each object in an array of JSON objects to a CSV format.

and more.

To find an image with the most layers, we can use the following command:

```
docker image inspect <image_name> | jq '.[0].RootFS.Layers | length'
```

### Multi-stage builds
Multi-stage builds are a feature of Docker that allows users to create multiple stages in a single Dockerfile. Each stage can use a different base image and can include different instructions for building the image. This is useful for creating smaller, more efficient images by separating the build process into multiple stages.

```
# Stage 1: Build the application
FROM golang:1.16 AS builder
WORKDIR /app
COPY . .
RUN go build -o myapp
# Stage 2: Create the final image
FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/myapp .
CMD ["./myapp"]
```

In this example, the first stage uses the `golang:1.16` base image to build a Go application. The second stage uses the `alpine:latest` base image to create a smaller final image that only includes the built application. The `COPY --from=builder` instruction is used to copy the built application from the first stage to the second stage.

To check the size of the final image, we can use the `docker images` command:

```
docker images <image_name>
```

### Multi-platform builds

Multi-platform builds are a feature of Docker that allows users to create images that can run on multiple architectures, such as x86_64 and ARM. This is useful for creating images that can run on different types of devices, such as servers, desktops, and mobile devices.

To create a multi-platform build, we can use the `docker buildx` command, which is an extension of the `docker build` command that supports building images for multiple platforms.

First, we need to create a new builder instance using the following command:

```
docker buildx create --name mybuilder --use
```
This command creates a new builder instance named `mybuilder` and sets it as the default builder.

Next, we can use the `docker buildx build` command to create a multi-platform build. The syntax for the command is as follows:

```
docker buildx build --platform <platforms> -t <image_name> .
```

For example, to create a multi-platform build for the `linux/amd64` and `linux/arm64` architectures, we can use the following command:

```
docker buildx build --platform linux/amd64,linux/arm64 . -t my-multi-platform-image
```
This command will create a multi-platform build for the specified architectures and tag the image with the name `my-multi-platform-image`.

A multi-platform example Dockerfile:

```
# Initial stage, using local platform
FROM --platform=$BUILDPLATFORM golang:1.16 AS builder
# Copy source into place
WORKDIR /src
COPY . .
# Pull the environment variables from the host
ARG TARGETOS TARGETARCH
# Build for the target platform
RUN env GOOS=$TARGETOS GOARCH=$TARGETARCH go build -o /out/myapp .
# Final stage, using target platform
FROM alpine
COPY --from=builder /out/myapp /myapp
```

## Docker Compose

Docker Compose is a tool that allows users to define and manage multi-container Docker applications. It uses a YAML file to define the services, networks, and volumes that make up the application.

A simple example of a `docker-compose.yml` file:

```yaml
services:
  # Define the container(s), by name
  webapp:
    # The image to use for the container
    image: "webapp"
    # Map port 80 in the container to port 8080 on the host
    ports:
      - "8080:80"
  # Defining any other containers
  redis:
    image: "redis:alpine"
```

To start the application, we can use the `docker-compose up` command:

```
docker compose up or docker-compose up
```

`docker compose up -d or docker-compose up -d`: This command starts the application in detached mode, allowing it to run in the background.

`docker compose down or docker-compose down`: This command stops and removes the application, including all containers, networks, and volumes defined in the `docker-compose.yml` file.

`docker compose ps or docker-compose ps`: This command lists all running containers in the application, along with their names, statuses, and ports.

`docker compose ls or docker-compose ls`: This command lists all available Docker Compose applications on the local machine, along with their names, statuses, and number of containers.

`docker compose -f <file> up or docker-compose -f <file> up`: This command starts the application using a specified `docker-compose.yml` file, allowing users to define multiple applications with different configurations.

`docker compose -f <file> down or docker-compose -f <file> down`: This command stops and removes the application defined in a specified `docker-compose.yml` file.

`docker compose -f <file> ps or docker-compose -f <file> ps`: This command lists all running containers in the application defined in a specified `docker-compose.yml` file.

### YAML
YAML (YAML Ain't Markup Language) is a human-readable data serialization format that is often used for configuration files and data exchange between programming languages. It is designed to be easy to read and write, with a simple syntax that uses indentation to indicate structure.

Some common YAML syntax includes:
- Key-value pairs: YAML uses key-value pairs to represent data. The key is followed by a colon (`:`) and the value is separated by a space. For example, `name: John` represents a key-value pair where the key is `name` and the value is `John`.
- Lists: YAML uses hyphens (`-`) to represent lists. Each item in the list is preceded by a hyphen and a space. For example:

  ```
  fruits:
    - apple
    - banana
    - orange
  ```
represents a list of fruits with three items: `apple`, `banana`, and `orange`.

- Nested structures: YAML uses indentation to indicate nested structures. Each level of indentation represents a new level of hierarchy. For example:

  ```
  person:
    name: John
    age: 30
    address:
      street: 123 Main St
      city: Anytown
      state: CA
  ```
represents a nested structure where `person` is the top-level key, and `name`, `age`, and `address` are nested keys.

The main sections are `services`, `networks`, and `volumes`. The `services` section defines the containers that make up the application, while the `networks` and `volumes` sections define any custom networks or volumes that are used by the services.

Note that the `networks` and `volumes` sections are optional and can be omitted if not needed. If they are included, they should be defined at the same level as the `services` section.

The `configs` section handles configuration options without custom images. The `secrets` section is used to manage sensitive information, such as passwords or API keys, that should not be stored in the `docker-compose.yml` file.

The services section defines all the containers that make up the application. Each service is defined by a name and a set of options, such as the image to use, the ports to expose, and any environment variables to set.

An example is:

```yaml
services:
  # Resource name
  postgres:
    # Container name, otherwise random
    container_name: postgres
    # The image to use for the container
    image: postgres:latest
    # Any port mappings
    ports:
     - "5432:5432"

  # Next resource
   pgadmin:
    ...
```

Dependencies between services can be defined using the `depends_on` option. This ensures that a service is started only after its dependencies are started.

For example, we define a postgresql database with no dependencies, then the python application that depends on the database, and finally a web server that depends on the python application:

Other options include `condition` to specify the condition for starting the service, such as `service_healthy` to wait until the service is healthy before starting the dependent service, and `service_started` to wait until the service is started before starting the dependent service.

The `service_completed_successfully` condition ensures that the dependent service is started only if the service it depends on has completed successfully.

```yaml
services:
  db:
    image: postgres
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb

  app:
    image: my-python-app
    depends_on:
      db:
        condition: service_healthy

  web:
    image: nginx
    depends_on:
      app:
        condition: service_started
```

`docker compose logs` or `docker-compose logs`: This command retrieves the logs for all containers in the application, allowing users to view the output of each container.

`docker compose top` or `docker-compose top`: This command displays the running processes inside each container in the application, allowing users to monitor resource usage and performance.

The above commands help when troubleshooting issues with the application or monitoring its performance.

### Data sharing in compose.yml

Data can be shared between containers in a Docker Compose application using volumes. Volumes are a way to persist data outside of the container's filesystem, allowing data to be shared between multiple containers.

To define a volume in a `docker-compose.yml` file, we can use the `volumes` section. The syntax for defining a volume is as follows:

```yaml
volumes:
  <volume_name>:
    driver: <driver_name>
    driver_opts:
      <option_name>: <option_value>
```

For example, to define a volume named `my-data` using the default `local` driver, we can use the following syntax:

```yaml
volumes:
  my-data:
    driver: local
```

We can also add a networking section to define custom networks for the application. The syntax for defining a network is as follows:

```yaml
services:
  resource:
    name: resource1

    networks:
       network_name:
         aliases:
           - alias1
           - alias2
```

