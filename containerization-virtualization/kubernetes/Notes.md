# Kubernetes

## Intro to Kubernetes

Kubernetes is an open-source platform designed to automate deploying, scaling, and operating application containers. 

It provides container-centric infrastructure that allows developers to deploy applications quickly and efficiently, while also providing the tools necessary for managing those applications in production.

### Basic Key Concepts
- **Pod**: The smallest deployable unit in Kubernetes, which can contain one or more containers.
- **Node**: A worker machine in Kubernetes, which can be a physical or virtual machine.
- **Cluster**: A set of nodes that run containerized applications managed by Kubernetes.
- **Service**: An abstraction that defines a logical set of Pods and a policy by which to access them.
- **Deployment**: A higher-level abstraction that manages a set of Pods, ensuring that the desired state of the application is maintained.
- **Namespace**: A way to divide cluster resources between multiple users or teams, providing a scope for names.
- **Kubelet**: An agent that runs on each node in the cluster, responsible for managing Pods and ensuring they are running as expected.

Note: A stateful application is one that maintains state across requests, such as a database or a message queue. A stateless application does not maintain any state between requests, making it easier to scale and manage.

### Kubernetes Architecture
Kubernetes architecture consists of a Control Plane and Nodes. The Control Plane manages the cluster, while Nodes run the applications. The Control Plane includes components like the API Server, Scheduler, Controller Manager, and etcd (a distributed key-value store). Nodes run the Kubelet, which communicates with the Control Plane, and the container runtime (like Docker) to run containers.

### Deploying a First (Stateless) Application

`kubectl` is the command-line tool used to interact with Kubernetes clusters and objects. The objects include Pods, Services, Deployments, and more.

The typical usage pattern includes:

1. `kubectl create -f <manifest.yaml>` creates new objects, with `-f` for "filename".
2. `kubectl apply -f <manifest.yaml>` creates new objects and changes the state of objects.
3. `kubectl get <object>` gives an overview of objects deployed on Kubernetes.
4. `kubectl describe <object>` provides detailed information about a specific object.

Manifests are YAML files that define the desired state of Kubernetes objects. They include specifications for Pods, Services, Deployments, etc. There are two important sections in a manifest:
- `metadata`: Contains information about the object, such as its name and labels.
- `spec`: Defines the desired state of the object, including container images, ports, and other configurations.

Stateless applications are general concepts and not specific to Kubernetes. They do not maintain any state between requests, making them easier to scale and manage. In Kubernetes, stateless applications can be deployed using Deployments, which manage the lifecycle of Pods.

An example is the database frontend querying a database backend. The frontend can be a stateless application that handles user requests, while the backend is a stateful service that manages data persistence.

Stateless applications translate to Kubernetes as Deployments. An example/template for a Deployment manifest is as follows:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: <deployment-name>
    labels:
        app: <a label for the application>
spec:
    replicas: <number of replicas>
    selector:
        matchLabels:
            app: <matches the label above>
    template:
        metadata:
            labels:
                app: <label to be given to each pod>
        spec:
            containers:
            - name: <container-name>
              image: <container-image>
              ports:
                - containerPort: <port for networking>
```

When deploying a stateless application, you can use the `kubectl apply -f <deployment.yaml>` command to create the Deployment. Kubernetes Control Plane will schedule the Deployment on Nodes. Then the Pods created will be triggered on the Nodes. 

Pods get a unique, but random identifier, which can be used to access the application. The Pods are managed by the Deployment, which ensures that the desired number of replicas is maintained.

### Scaling and Monitoring an Application

Scaling is a technique to add (scale up) or remove (scale down) resources to an application based on demand. In Kubernetes, scaling can be done manually or automatically.

Either we change the number of replicas in the Deployment manifest and apply it again, or we can use the `kubectl scale deployment ...` command to change the number of replicas on the fly.

Monitoring is essential to ensure that applications are running smoothly and to identify issues before they become critical. Kubernetes provides several tools for monitoring such as Prometheus, Grafana, or `kubectl`

For `kubectl`, we can use `kubectl get <object to be monitored>`. `kubectl get pods` will show the status of all Pods, including their readiness and health and `kubectl get services` will show the status of all services.

### Deploy, Scale, and Monitor a Stateful Application

Stateless applications map to Kubernetes Deployments and each Pod of the application does exactly the same tasks. Each Pod is an exact replica of the others. 

Stateful applications, on the other hand, need Pods that are not exact replicas of each other, as each Pod may work on different tasks. 

Stateful applications save some internal state. When interrupted or stopped, a new Pod is replicated and can continue to operate from the saved state. Stateful applications are used, i.e., database backends, message queues, or other services that require data persistence.

StatefulSets are used to create and manage stateful applications in Kubernetes. They provide guarantees about the ordering and uniqueness of Pods, which is essential for stateful applications.

An example/template for a StatefulSet manifest is as follows:


```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
    name: <deployment-name>
    labels:
        app: <a label for the application>
spec:
    replicas: <number of initial replicas>
    selector:
        matchLabels:
            app: <matches the label above>
    template:
        metadata:
            labels:
                app: <label to be given to each pod>
        spec:
            containers:
            - name: <container-name>
              image: <container-image>
              ports:
                - containerPort: <port for networking>
```

Deploying a StatefulSet is similar to deploying a Deployment. You can use the `kubectl apply -f <statefulset.yaml>` command to create the StatefulSet. 

Once deployed, a StatefulSet is created differently from a Deployment. Pods are created one after the other, and each Pod gets a unique identifier (name) based on its ordinal index. This ensures that each Pod can be addressed individually, which is crucial for stateful applications.

They can also be scaled up or down using the `kubectl scale statefulset ...` command, but scaling down will not delete Pods in reverse order. Instead, it will delete the last Pod first, ensuring that the state is preserved.

For monitoring stateful applications, you can use the same `kubectl` commands as for stateless applications. The same commands like `kubectl get pods` and `kubectl get services` can be used to monitor the status of StatefulSets and their Pods.

### Storage in Kubernetes

The fundamental objects for storage in Kubernetes are Persistent Volumes (PV) maintained in parallel to Pods.

Persistent Volumes are mapped to Pods using Persistent Volume Claims (PVC). PVCs are requests for storage resources that Pods can use. 

A mapped PV allows data persistence when the Pod is stopped, killed, or restarted. This is crucial for stateful applications that need to maintain their data across Pod restarts.

When a Pod needs storage, it creates a PVC, which is then bound to a PV that meets the storage requirements. This allows Pods to access persistent storage even if they are rescheduled or restarted.

PVs can be provisioned either manually by an Kubernetes administrator or dynamically by Kubernetes using Storage Classes. The SCs are defined by an administrator and specify the type of storage to be used, such as NFS, AWS EBS, or GCE Persistent Disk.

For a Pod with Persistent Volume

```yaml
apiVersion: v1
kind: Pod
...
spec:
    containers:
    ...
      volumeMounts:
      - name: pv-mydata
        mountPath: /data
    volumes:
    - name: pv-mydata
      persistentVolumeClaim:
        claimName: datacamp-pvc
```

For a Persistent Volume Claim with Storage Class

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: datacamp-pvc
spec:
  storageClassName: "standard"
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
```

The commands for storage include:
- `kubectl get pv`: Lists all Persistent Volumes in the cluster.
- `kubectl get pvc`: Lists all Persistent Volume Claims in the cluster.
- `kubectl get sc`: Lists all Storage Classes in the cluster.

As usual, `kubectl apply -f <manifest.yaml>` is used to create or update Persistent Volumes, Persistent Volume Claims, and Storage Classes.

### Networking, Load Balancing, and Security

Labels and selectors are used to group and select Kubernetes objects. Labels are key-value pairs attached to objects, while selectors are used to filter objects based on their labels.

Services, which can be created using Manifests, are used to expose Pods to the network. They provide a stable endpoint for accessing a set of Pods, allowing for load balancing and service discovery.

Load balancing is a feature of Services that distributes incoming traffic across multiple Pods. This ensures that no single Pod is overwhelmed with requests, improving the availability and reliability of the application. They can be declared in the `spec` section of a Service manifest.

Load balancers are pre-configured to work with cloud providers, such as AWS or GCP, and can be created using the `type: LoadBalancer` field in the Service manifest. This allows Kubernetes to automatically provision a cloud load balancer that routes traffic to the Pods.

Ingress allows us to route HTTP and HTTPS traffic to Services which is done by rules that define which service is used by which requests. For example, the ingress rules route requests for endpoint /for_service1 to K8s Service1 and requests for endpoint /for_service2 to K8s Service2.

Security in Kubernetes is managed through Role-Based Access Control (RBAC), which allows administrators to define roles and permissions for users and service accounts. This ensures that only authorized users can access and modify Kubernetes resources.


### Data Pipelines in Kubernetes

Data pipelines are a set of processes to move data from a source to a destination, transform data from one form into another, and analyze the data to get insights from it. 

In most cases, the data pipelines consists of three major steps: extract, transform, and load (ETL). Similarly, ELT (extract, load, transform) is a variation that is often used in modern data architectures, where data is loaded into a staging area before being transformed.

In Kubernetes, the extract, transform, and load steps can be deployed using Deployments or StatefulSets, and the data that gets extracted and transformed can be stored using Persistent Volumes. Further, if we use scalable solutions for all these steps, we can use K8s to scale our deployments and storage when needed. 

For extracting data, we can use tools like Apache Kafka, Apache Nifi with Kafka Connect. For transforming data, we can use tools like Apache Spark, Apache Kafka, Apache Flink, PostgreSQL, and for loading data, we can use tools like Apache Spark, Apache Kafka with KSQL, PostgreSQL, and for storage on top of PVs, we can use Minio or block storage like Ceph.

### MLOps in Kubernetes

MLOps is a set of practices that combines machine learning (ML) and operations (Ops) to automate the deployment, monitoring, and management of ML models in production. It is a collection of best-practice workflows with a strong focus on continous development and constant improvement of ML models.

The isolated experimental systems that we need for development and testing can easily be realized by Pods and K8s Storage. We can monitor our productive ML models easily by following the lifecycle of our Pods, together with the images we have deployed. It is also possible to work synchronously as a team, on model accuracy, as this is enabled from the very beginning by the architecture of Kubernetes Several frameworks exist for MLOps on Kubernetes, such as Kubeflow, MLflow, and TensorFlow Extended (TFX).

Kubeflow is an open-source platform that provides a set of tools for building, deploying, and managing ML workflows on Kubernetes. It includes components for data preprocessing, model training, hyperparameter tuning, and model deployment. It covers the entire ML lifecycle, from data preparation to model deployment and monitoring. Python can be used for scripting and automating tasks within Kubeflow.