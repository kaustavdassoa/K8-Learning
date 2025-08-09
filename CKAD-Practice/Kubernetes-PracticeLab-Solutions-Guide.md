# Kubernetes Practice Lab Solutions Guide

**User:** KD  

## Response:
LAB: Practice Test Solutions
============================

Table of Contents
-----------------

*   [LAB:Practice_Test_Pods](#LAB:Practice_Test_Pods)
*   [LAB Practice Test - ReplicaSets](#LAB Practice Test - ReplicaSets)
*   [Difference between ReplicaSet and Deployment](#Difference between ReplicaSet and Deployment)
*   [LAB Practice Test - Deployments](#LAB Practice Test - Deployments)
*   [LAB Practice Test - Docker Images](#LAB Practice Test - Docker Images])
*   [LAB Practice Test - Commands and Arguments](https://www.google.com/search?q=%23lab-practice-test---commands-and-arguments)
*   [LAB Practice Test - ConfigMaps](https://www.google.com/search?q=%23lab-practice-test---configmaps)
*   [LAB Practice Test - Security Contexts](https://www.google.com/search?q=%23lab-practice-test---security-contexts)
*   [LAB Practice Test - Service Accounts](https://www.google.com/search?q=%23lab-practice-test---service-accounts)
*   [LAB Practice Test - Secrets](https://www.google.com/search?q=%23lab-practice-test---secrets)
*   [LAB Practice Test - Resource Requirements](#LAB Practice Test - Resource Requirements)
*   [LAB Practice Test - Taints and Toleration](#LAB Practice Test - Taints and Toleration)
*   [LAB Practice Test - Node Affinity](https://www.google.com/search?q=%23lab-practice-test---node-affinity)
*   [LAB Practice Test - Multi-Container Pods](https://www.google.com/search?q=%23lab-practice-test---multi-container-pods)
*   [LAB Practice Test – Init Containers](https://www.google.com/search?q=%23lab-practice-test--init-containers)
*   [LAB Practice Test - Readiness and Liveness Probes](#LAB Practice Test - Readiness and Liveness Probes)
*   [LAB Practice Test - Container Logging](https://www.google.com/search?q=%23lab-practice-test---container-logging)
*   [LAB Practice Test - Monitoring](#LAB Practice Test - Monitoring)
*   [LAB Practice Test - Labels, Selectors and Annotations](#LAB Practice Test - Labels, Selectors and Annotations)
*   [LAB Practice Test - Rolling Updates & Rollbacks](#LAB Practice Test - Rolling Updates & Rollbacks)
*   [LAB Practice Test - Deployment Strategies](#LAB Practice Test - Deployment Strategies)
*   [LAB Practice Test - Jobs & CronJobs](https://www.google.com/search?q=%23lab-practice-test---jobs--cronjobs)
*   [LAB Practice Test - Services](https://www.google.com/search?q=%23lab-practice-test---services)
*   [LAB Practice Test - Ingress Networking - 1](https://www.google.com/search?q=%23lab-practice-test---ingress-networking---1)
*   [LAB Practice Test - Network Policies](https://www.google.com/search?q=%23lab-practice-test---network-policies)
*   [LAB Practice Test - Persistent Volumes](https://www.google.com/search?q=%23lab-practice-test---persistent-volumes)
*   [LAB Practice Test - Storage Class](https://www.google.com/search?q=%23lab-practice-test---storage-class)
*   [LAB Practice Test - KubeConfig](https://www.google.com/search?q=%23lab-practice-test---kubeconfig)
*   [LAB Practice Test Role Based Access Controls](https://www.google.com/search?q=%23lab-practice-test-role-based-access-controls)

* * *

# LAB:Practice_Test_Pods
-------------------------

**Important `kubectl` commands**

*   **List pods:**
    ```
    kubectl get pods
    ```
    _This command lists all pods in the current namespace._
*   **Describe a pod:**
    ```
    kubectl describe pod <pod-name>
    ```
    _This command provides detailed information about a specific pod, including its status, events, and container details._
*   **Create a pod with nginx image:**
    ```
    kubectl run ngix --image=nginx
    kubectl run redis --image=redis123
    ```
    _The `kubectl run` command is an imperative way to create a pod. Here, `ngix` and `redis` are the names of the pods, and `nginx` and `redis123` are the container images used._

	Here's an example of listing pods with wide output, showing IP addresses and nodes:

	```
	kubectl get pods -o wide
	```

	This output shows pods `newpods-h7b7b`, `newpods-pllpx`, `newpods-w9w4l`, and `ngix` are running on the `controlplane` node, along with their IP addresses._

	```
	NAME            READY   STATUS    RESTARTS   AGE     IP           NODE           NOMINATED NODE   READINESS GATES
	newpods-h7b7b   1/1     Running   0          4m15s   10.42.0.10   controlplane   <none>           <none>
	newpods-pllpx   1/1     Running   0          4m15s   10.42.0.9    controlplane   <none>           <none>
	newpods-w9w4l   1/1     Running   0          4m15s   10.42.0.11   controlplane   <none>           <none>
	ngix            1/1     Running   0          2m43s   10.42.0.13   controlplane   <none>           <none>
	```

	Here's an example of listing pods showing a `webapp` pod in `ImagePullBackOff` status:

	```
	kubectl get pods
	```

	```
	NAME            READY   STATUS             RESTARTS   AGE
	newpods-h7b7b   1/1     Running            0          4m54s
	newpods-pllpx   1/1     Running            0          4m54s
	newpods-w9w4l   1/1     Running            0          4m54s
	ngix            1/1     Running            0          3m22s
	webapp          1/2     ImagePullBackOff   0          27s
	```

	This output indicates that the `webapp` pod is experiencing an `ImagePullBackOff` error, meaning it's unable to pull one of its container images.

	**Describing the `webapp` pod:**

	```
	kubectl describe pod webapp
	```



	```
	## Output

	Name:             webapp
	Namespace:        default
	Priority:         0
	Service Account:  default
	Node:             controlplane/192.168.187.125
	Start Time:       Mon, 06 Jan 2025 14:02:05 +0000
	Labels:           <none>
	Annotations:      <none>
	Status:           Pending
	IP:               10.42.0.14
	IPs:
	  IP:  10.42.0.14
	Containers:
	  nginx:
		Container ID:   containerd://9d6ef984452d2ed51987b7e12d82fcc664b3d1a982018a3460336fa82d1be8fe
		Image:          nginx
		Image ID:       docker.io/library/nginx@sha256:42e917aaa1b5bb40dd0f6f7f4f857490ac7747d7ef73b391c774a41a8b994f15
		Port:           <none>
		Host Port:      <none>
		State:          Running
		  Started:      Mon, 06 Jan 2025 14:02:06 +0000
		Ready:          True
		Restart Count:  0
		Environment:    <none>
		Mounts:
		  /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7qrr7 (ro)
	  agentx:
		Container ID:
		Image:          agentx
		Image ID:
		Port:           <none>
		Host Port:      <none>
		State:          Waiting
		  Reason:       ImagePullBackOff
		Ready:          False
		Restart Count:  0
		Environment:    <none>
		Mounts:
		  /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7qrr7 (ro)
	Conditions:
	  Type                        Status
	  PodReadyToStartContainers   True
	  Initialized                 True
	  Ready                       False
	  ContainersReady             False
	  PodScheduled                True
	Volumes:
	  kube-api-access-7qrr7:
		Type:                    Projected (a volume that contains injected data from multiple sources)
		TokenExpirationSeconds:  3607
		ConfigMapName:           kube-root-ca.crt
		ConfigMapOptional:       <nil>
		DownwardAPI:             true
	QoS Class:                   BestEffort
	Node-Selectors:              <none>
	Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
								 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
	Events:
	  Type     Reason     Age                From               Message
	  ----     ------     ----               ----               -------
	  Normal   Scheduled  98s                default-scheduler  Successfully assigned default/webapp to controlplane
	  Normal   Pulling    98s                kubelet            Pulling image "nginx"
	  Normal   Pulled     98s                kubelet            Successfully pulled image "nginx" in 159ms (159ms including waiting). Image size: 72099410 bytes.
	  Normal   Created    98s                kubelet            Created container nginx
	  Normal   Started    98s                kubelet            Started container nginx
	  Warning  Failed     57s (x3 over 97s)  kubelet            Error: ErrImagePull
	  Normal   BackOff    18s (x5 over 97s)  kubelet            Back-off pulling image "agentx"
	  Warning  Failed     18s (x5 over 97s)  kubelet            Error: ImagePullBackOff
	  Normal   Pulling    7s (x4 over 98s)   kubelet            Pulling image "agentx"
	  Warning  Failed     6s (x4 over 97s)   kubelet            Failed to pull image "agentx": failed to pull and unpack image "docker.io/library/agentx:latest": failed to resolve reference "docker.io/library/agentx:latest": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
	```

	The `describe` output clearly shows that the `nginx` container is running, but the `agentx` container is in `ImagePullBackOff` state. The events section provides the specific error: "Failed to pull image 'agentx': failed to pull and unpack image 'docker.io/library/agentx:latest': failed to resolve reference 'docker.io/library/agentx:latest': pull access denied, repository does not exist or may require authorization: server message: insufficient\_scope: authorization failed." This indicates the image `agentx` could not be found or pulled.

	NOTE: Total number of running pods/Total number of pods

	#### Edit Pods

*   **Set image for a pod, replicationcontroller, deployment, etc.:**
    ```
    kubectl set image (-f FILENAME | TYPE NAME) CONTAINER_NAME_1=CONTAINER_IMAGE_1 ... CONTAINER_NAME_N=CONTAINER_IMAGE_N
    ```
    The above command allows you to update the image of one or more containers within a specified resource. You can target various resource types like `pod`, `replicationcontroller`, `deployment`, `daemonset`, `statefulset`, `cronjob`, and `replicaset`._
   
	**Example:**
    ```
    kubectl set image po redis redis=redis
    ```
    
	This command updates the `redis` container's image in the `redis` pod to `redis`._
*   **Edit a pod directly:**
    
	```
    kubectl edit pod <pod-name>
    ```
    
	This command opens the pod's definition in your default editor, allowing for direct modifications._
    **NOTE**: Please note that only the properties listed below are editable for a running pod:
    *   `spec.containers[*].image`
    *   `spec.initContainers[*].image`
    *   `spec.activeDeadlineSeconds`
    *   `spec.tolerations`
    *   `spec.terminationGracePeriodSeconds`


#LAB Practice Test - ReplicaSets
-------------------------------

*   **Describe a ReplicaSet:**
    ```
    kubectl describe rs new-replica-set
    ```
    This command provides detailed information about the `new-replica-set` ReplicaSet, including its desired state, current state, and the pod template it uses.
    
	```
	apiVersion: apps/v1
	kind: ReplicaSet
	metadata:
	  creationTimestamp: "2025-01-06T14:19:09Z"
	  generation: 1
	  name: new-replica-set
	  namespace: default
	  resourceVersion: "749"
	  uid: 0ebd606d-4eec-43fd-8084-ebc00f4dc9af
	spec:
	  replicas: 4                                              # Specifies that 4 replicas of the pod should be maintained.
	  selector:
		matchLabels:
		  name: busybox-pod                                    # The ReplicaSet will manage pods with this label.
	  template:
		metadata:
		  creationTimestamp: null
		  labels:
			name: busybox-pod                                   # Labels applied to pods created by this ReplicaSet.
		spec:
		  containers:
		  - command: # Command to run inside the container.
			- sh
			- -c
			- echo Hello Kubernetes! && sleep 3600               # The command executed by the busybox container.
			image: busybox777                                    # The container image to use. This image appears to be incorrect/unavailable.
			imagePullPolicy: Always                              # Always attempt to pull the image.
			name: busybox-container                              # Name of the container.
			resources: {}
			terminationMessagePath: /dev/termination-log
			terminationMessagePolicy: File
		  dnsPolicy: ClusterFirst
		  restartPolicy: Always                                  # Always restart the container if it exits.
		  schedulerName: default-scheduler
		  securityContext: {}
		  terminationGracePeriodSeconds: 30
	status:
	  fullyLabeledReplicas: 4
	  observedGeneration: 1
	  replicas: 4
	```

	The ReplicaSet `new-replica-set` is configured to maintain 4 replicas of a pod named `busybox-pod`. The pods attempt to use the `busybox777` image and execute a shell command. The status section shows that 4 replicas are desired and 4 are currently managed.

*   **Get ReplicaSets:**
    ```
    kubectl get rs
    ```
    This command lists all ReplicaSets in the current namespace._
    
	```
	NAME              DESIRED   CURRENT   READY   AGE
	new-replica-set   4         4         0       3m17s
	```

	The output shows that `new-replica-set` desires 4 pods, currently has 4 pods, but 0 are ready. This indicates an issue with the pods becoming ready, likely due to an image pull problem._

*   **Get pods:**
    ```
    kubectl get pods
    ```
    This command lists all pods, and in this case, reveals the reason for the ReplicaSet's unready status._
    
	```
	NAME                    READY   STATUS             RESTARTS   AGE
	new-replica-set-2r2rv   0/1     ImagePullBackOff   0          4m22s
	new-replica-set-hgbgm   0/1     ImagePullBackOff   0          4m22s
	new-replica-set-lpvsm   0/1     ImagePullBackOff   0          4m22s
	new-replica-set-pbrlq   0/1     ImagePullBackOff   0          4m22s
	```

	All pods managed by `new-replica-set` are in `ImagePullBackOff` status, confirming the image pull issue._

*   **Get a specific pod:**
    ```
    kubectl get pod new-replica-set-2r2rv
    ```
    This command provides a quick status update for a single pod.
    
	```
	NAME                    READY   STATUS             RESTARTS   AGE
	new-replica-set-2r2rv   0/1     ImagePullBackOff   0          4m34s
	```

*   **Describe a specific pod in ReplicaSet:**

    ```
    kubectl describe pod new-replica-set-2r2rv
    ```
    
	This command provides detailed events and status for the failing pod.
    
	```
	Name:             new-replica-set-2r2rv
	Namespace:        default
	Priority:         0
	Service Account:  default
	Node:             controlplane/192.168.44.33
	Start Time:       Mon, 06 Jan 2025 14:19:09 +0000
	Labels:           name=busybox-pod
	Annotations:      <none>
	Status:           Pending
	IP:               10.42.0.10
	IPs:
	  IP:           10.42.0.10
	Controlled By:  ReplicaSet/new-replica-set
	Containers:
	  busybox-container:
		Container ID:
		Image:         busybox777 # The image that failed to pull.
		Image ID:
		Port:          <none>
		Host Port:     <none>
		Command:
		  sh
		  -c
		  echo Hello Kubernetes! && sleep 3600
		State:          Waiting
		  Reason:       ImagePullBackOff
		Ready:          False
		Restart Count:  0
		Environment:    <none>
		Mounts:
		  /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-jmdsx (ro)
	Conditions:
	  Type                        Status
	  PodReadyToStartContainers   True
	  Initialized                 True
	  Ready                       False
	  ContainersReady             False
	  PodScheduled                True
	Volumes:
	  kube-api-access-jmdsx:
		Type:                    Projected (a volume that contains injected data from multiple sources)
		TokenExpirationSeconds:  3607
		ConfigMapName:           kube-root-ca.crt
		ConfigMapOptional:       <nil>
		DownwardAPI:             true
	QoS Class:                   BestEffort
	Node-Selectors:              <none>
	Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
								 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
	Events:
	  Type     Reason     Age                    From               Message
	  ----     ------     ----                   ----               -------
	  Normal   Scheduled  4m43s                  default-scheduler  Successfully assigned default/new-replica-set-2r2rv to controlplane
	  Normal   Pulling    3m18s (x4 over 4m43s)  kubelet            Pulling image "busybox777"
	  Warning  Failed     3m17s (x4 over 4m42s)  kubelet            Failed to pull image "busybox777": failed to pull and unpack image "docker.io/library/busybox777:latest": failed to resolve reference "docker.io/library/busybox777:latest": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
	  Warning  Failed     3m17s (x4 over 4m42s)  kubelet            Error: ErrImagePull
	  Warning  Failed     3m5s (x6 over 4m42s)   kubelet            Error: ImagePullBackOff
	  Normal   BackOff    2m52s (x7 over 4m42s)  kubelet            Back-off pulling image "busybox777"
	```

	The `describe` output for `new-replica-set-2r2rv` confirms the `ImagePullBackOff` status. The key message in the events section is "Failed to pull image 'busybox777': failed to pull and unpack image 'docker.io/library/busybox777:latest': failed to resolve reference 'docker.io/library/busybox777:latest': pull access denied, repository does not exist or may require authorization: server message: insufficient\_scope: authorization failed". This indicates that the `busybox777` image does not exist or is inaccessible._

*   **Delete multiple pods:**
    ```
    kubectl delete pods new-replica-set-2r2rv new-replica-set-hgbgm new-replica-set-lpvsm new-replica-set-pbrlq
    ```
    Deleting the failing pods will cause the ReplicaSet to recreate them, giving an opportunity for a fix (e.g., updating the image)._

	Here's an example YAML for a ReplicaSet with an `nginx` container:

	```
	apiVersion: apps/v1
	kind: ReplicaSet
	metadata:
	  name: replicaset-1
	spec:
	  replicas: 2 # Desired number of pod replicas.
	  selector:
		matchLabels:
		  tier: frontend # Selector to identify pods managed by this ReplicaSet.
	  template:
		metadata:
		  labels:
			tier: frontend # Labels applied to pods created by this ReplicaSet.
		spec:
		  containers:
		  - name: nginx # Name of the container.
			image: nginx # Image to use for the container.
	```

	This YAML defines a ReplicaSet named `replicaset-1` that aims to maintain 2 replicas of an `nginx` pod, identified by the label `tier: frontend`._

*   **Delete multiple ReplicaSets:**
    ```
    kubectl delete rs replicaset-1 replicaset-2
    ```
    _This command deletes the specified ReplicaSets._
    
	```
	replicaset.apps "replicaset-1" deleted
	replicaset.apps "replicaset-2" deleted
	```

*   **Update the image of a ReplicaSet:**
    ```
    kubectl set image rs new-replica-set busybox-container=busybox
    ```
    _This command updates the `busybox-container` in the `new-replica-set` ReplicaSet to use the `busybox` image.
    **NOTE**: After updating the ReplicaSet image, one needs to delete the existing pods to get the pods recreated with the new image. The ReplicaSet will automatically create new pods with the updated image.

*   **Scale a ReplicaSet:**
    ```
    kubectl scale rs new-replica-set --replicas=5
    ```
    This command scales the `new-replica-set` ReplicaSet to have 5 replicas._

*   **Edit a ReplicaSet directly:**
    ```
    kubectl edit replicaset new-replica-set
    ```
    This command opens the ReplicaSet's definition in your default editor for direct modification._

	Difference between ReplicaSet and Deployment
	--------------------------------------------

	*   **Purpose and Functionality:**
		*   **ReplicaSet** ensures a specified number of pod replicas are running at any given time.
		*   **Deployment** manages ReplicaSets and provides declarative updates to applications, along with additional features for managing application lifecycle.
	*   **Update Strategy:**
		*   **ReplicaSet** doesn't handle updates to pod templates - if you want to update the pod template, you need to create a new ReplicaSet.
		*   **Deployment** automatically handles updates by creating new ReplicaSets and gradually transitioning pods from old to new versions (rolling updates).
	*   **Version History:**
		*   **ReplicaSet** maintains no history of previous versions.
		*   **Deployment** maintains a revision history and allows easy rollback to previous versions.

	#### ReplicaSet example

	```
	apiVersion: apps/v1
	kind: ReplicaSet
	metadata:
	  name: frontend
	spec:
	  replicas: 3 # Desired number of pods.
	  selector:
		matchLabels:
		  app: frontend # Selector to identify pods.
	  template:
		metadata:
		  labels:
			app: frontend # Labels applied to pods.
		spec:
		  containers:
		  - name: php-redis # Name of the container.
			image: gcr.io/google_samples/gb-frontend:v1 # Image for the container.
	```

	This YAML defines a ReplicaSet named `frontend` that maintains 3 replicas of a pod running the `php-redis` container with the specified image._

	#### Deployment example

	```
	apiVersion: apps/v1
	kind: Deployment
	metadata:
	  name: frontend
	spec:
	  replicas: 3 # Desired number of pods.
	  strategy:
		type: RollingUpdate # Specifies a rolling update strategy.
		rollingUpdate:
		  maxSurge: 1 # Allows one extra pod to be created during update.
		  maxUnavailable: 0 # Ensures no pods are unavailable during update.
	  selector:
		matchLabels:
		  app: frontend # Selector to identify pods.
	  template:
		metadata:
		  labels:
			app: frontend # Labels applied to pods.
		spec:
		  containers:
		  - name: php-redis # Name of the container.
			image: gcr.io/google_samples/gb-frontend:v1 # Image for the container.
	```

	This YAML defines a Deployment named `frontend` that aims for 3 replicas using a `RollingUpdate` strategy. This allows for smooth updates of the `php-redis` application without downtime._

# LAB Practice Test - Deployments
-------------------------------

*   **Get pods:**
    ```
    kubectl get pods
    ```
    _Lists all pods in the current namespace._
*   **Get ReplicaSets:**
    ```
    kubectl get rs
    ```
    _Lists all ReplicaSets in the current namespace._
*   **Get Deployments:**
    ```
    kubectl get deploy
    ```
    _Lists all Deployments in the current namespace._
*   **Create a deployment imperatively:**
    ```
    kubectl create deployment httpd-frontend --image httpd:2.4-alpine --replicas 3
    ```
    _This imperative command creates a Deployment named `httpd-frontend` using the `httpd:2.4-alpine` image and sets the desired number of replicas to 3._

LAB Practice Test - Docker Images
---------------------------------

*   **Create a pod with labels:**
    ```
    kubectl run redis --image=redis:alpine --labels=tier=db
    ```
    _This imperative command creates a pod named `redis` using the `redis:alpine` image and assigns it a label `tier=db`._
*   **Expose a pod as a ClusterIP service:**
    ```
    kubectl expose pod redis --port=6379 --name=redis-service --type=ClusterIP
    ```
    _This command creates a `ClusterIP` service named `redis-service` that exposes the `redis` pod on port 6379. `ClusterIP` services are only accessible from within the Kubernetes cluster._
*   **Create a deployment:**
    ```
    kubectl create deploy webapp --image=kodekloud/webapp-color --replicas=3
    ```
    _This imperative command creates a Deployment named `webapp` with 3 replicas, using the `kodekloud/webapp-color` image._
*   **Create a new pod with a custom container port:** _Create a new pod called `custom-nginx` using the `nginx` image and run it on container port 8080._
*   **Create a namespace and deployment within it:**
    ```
    kubectl create ns dev-ns
    kubectl create deploy redis-deploy --image=redis --replicas=2 --namespace=dev-ns
    ```
    _First, a new namespace `dev-ns` is created. Then, a Deployment named `redis-deploy` with 2 replicas using the `redis` image is created within the `dev-ns` namespace._
    **Validation:**
    ```
    kubectl get deploy --namespace=dev-ns
    kubectl get pods --namespace=dev-ns
    ```
    _These commands are used to verify that the deployment and pods were successfully created in the `dev-ns` namespace._
*   **Create a pod and expose it as a ClusterIP service:** _Create a pod called `httpd` using the image `httpd:alpine` in the default namespace. Next, create a service of type `ClusterIP` by the same name (`httpd`). The target port for the service should be 80._
    ```
    kubectl run httpd --image=httpd:alpine --port=8081
    kubectl expose pod httpd --port=8081 --target-port=80 --type=ClusterIP --name=httpd
    ```
    _The `kubectl run` command creates the `httpd` pod and specifies container port 8081. The `kubectl expose` command then creates a `ClusterIP` service named `httpd` that listens on port 8081 and directs traffic to container port 80 within the `httpd` pod._

LAB Practice Test - Commands and Arguments
------------------------------------------

*   **Describe a pod to see its command and arguments:**
    ```
    kubectl describe pod ubuntu-sleeper
    ```
    _This command provides a detailed description of the `ubuntu-sleeper` pod, including the command it executes._
    
	```
	Name:             ubuntu-sleeper
	Namespace:        default
	Priority:         0
	Service Account:  default
	Node:             controlplane/192.168.212.138
	Start Time:       Wed, 08 Jan 2025 04:15:47 +0000
	Labels:           <none>
	Annotations:      <none>
	Status:           Running
	IP:               10.42.0.9
	IPs:
	  IP:  10.42.0.9
	Containers:
	  ubuntu:
		Container ID:  containerd://c9ad605d45be994c54ba99d280fc16de71a6db73d6f8d015494eac2a95f85bc9
		Image:         ubuntu
		Image ID:      docker.io/library/ubuntu@sha256:80dd3c3b9c6cecb9f1667e9290b3bc61b78c2678c02cbdae5f0fea92cc6734ab
		Port:          <none>
		Host Port:     <none>
		Command: # The command executed by the container.
		  sleep
		  4800 # The argument passed to the sleep command.
		State:          Running
		  Started:      Wed, 08 Jan 2025 04:15:49 +0000
		Ready:          True
		Restart Count:  0
		Environment:    <none>
		Mounts:
		  /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-dh74f (ro)
	Conditions:
	  Type                        Status
	  PodReadyToStartContainers   True
	  Initialized                 True
	  Ready                       True
	  ContainersReady             True
	  PodScheduled                True
	Volumes:
	  kube-api-access-dh74f:
		Type:                    Projected (a volume that contains injected data from multiple sources)
		TokenExpirationSeconds:  3607
		ConfigMapName:           kube-root-ca.crt
		ConfigMapOptional:       <nil>
		DownwardAPI:             true
	QoS Class:                   BestEffort
	Node-Selectors:              <none>
	Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
								 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
	Events:
	  Type    Reason     Age   From               Message
	  ----    ------     ----  ----               -------
	  Normal  Scheduled  37s   default-scheduler  Successfully assigned default/ubuntu-sleeper to controlplane
	  Normal  Pulling    37s   kubelet            Pulling image "ubuntu"
	  Normal  Pulled     36s   kubelet            Successfully pulled image "ubuntu" in 1.265s (1.265s including waiting). Image size: 29761377 bytes.
	  Normal  Created    36s   kubelet            Created container ubuntu
	  Normal  Started    36s   kubelet            Started container ubuntu
	```

	The `ubuntu-sleeper` pod uses the `ubuntu` image and executes the command `sleep 4800`, meaning the container will sleep for 4800 seconds._

	Here's a YAML definition for a pod demonstrating `command` usage:

	```
	apiVersion: v1
	kind: Pod
	metadata:
	  name: vi
	  namespace: default
	spec:
	  containers:
	  - name : ubuntu-container
		image: ubuntu
		command:            # Defines the command to be executed.
		- "sleep"           # The primary command.
		- "5000"            # Argument for the command.
	```

	**NOTE**: The commands should be in a string array. This pod `vi` runs an `ubuntu` container that executes `sleep 5000`, making the container sleep for 5000 seconds._

	Here's another YAML definition for a pod demonstrating `command` usage with a different string array representation:

	```
	apiVersion: v1
	kind: Pod
	metadata:
	  name: ubuntu-sleeper-3
	spec:
	  containers:
	  - name: ubuntu
		image: ubuntu
		command: ["sleep","1200"] # Another way to represent a string array for command.
	```

	**NOTE**: The commands should be in a string array, here is another way to represent string array. This pod `ubuntu-sleeper-3` also runs an `ubuntu` container, but sleeps for 1200 seconds.

*   **Edit a pod and force replace it:**
    ```
    k edit pod ubuntu-sleeper-3
    k replace --force -f /tmp/kubectl-edit-95038272.yaml
    ```
    _The `k edit` command allows for interactive editing of a live pod. `k replace --force -f` then forces an update to the pod using the modified definition from the temporary file. This is useful for applying changes that are not directly editable on a running pod, as it deletes and recreates the pod._

	Here are examples of Dockerfiles demonstrating `ENTRYPOINT` and `CMD`:

	**Dockerfile 1 (using ENTRYPOINT):**

	```
	FROM python:3.6-alpine
	RUN pip install flask
	COPY . /opt/
	EXPOSE 8080
	WORKDIR /opt
	ENTRYPOINT ["python", "app.py"] # Defines the executable for the container.
	```

	In this Dockerfile, `ENTRYPOINT ["python", "app.py"]` means that `python app.py` will be the command executed when the container starts. Any `CMD` specified would be passed as arguments to this entrypoint._

	**Dockerfile 2 (using ENTRYPOINT and CMD):**

	```
	FROM python:3.6-alpine
	RUN pip install flask
	COPY . /opt/
	EXPOSE 8080
	WORKDIR /opt
	ENTRYPOINT ["python", "app.py"] # Defines the executable.
	CMD ["--color", "red"] # Provides default arguments to the ENTRYPOINT.
	```

	Here, `ENTRYPOINT` is `python app.py`, and `CMD` provides default arguments `--color red`. So the effective command when the container starts will be `python app.py --color red`._

	Here's a YAML definition for a pod demonstrating `command` and `args` usage:

	```
	apiVersion: v1
	kind: Pod
	metadata:
	  name: webapp-green
	  labels:
		  name: webapp-green
	spec:
	  containers:
	  - name: simple-webapp
		image: kodekloud/webapp-color
		command: ["python", "app.py"] # Overrides the Dockerfile's ENTRYPOINT.
		args: ["--color", "pink"] # Overrides the Dockerfile's CMD and are arguments for the command.
	```

	This pod `webapp-green` runs the `kodekloud/webapp-color` image. It explicitly sets the `command` to `["python", "app.py"]` and `args` to `["--color", "pink"]`, effectively running `python app.py --color pink` inside the container._

*   **Generate a pod YAML with `run` and `dry-run`:**
    ```
    k run webapp-green --image=kodekloud/webapp-color -o yaml --dry-run=client > webapp-green.yaml
    ```
    This command uses `kubectl run` to generate a YAML manifest for a pod named `webapp-green` with the specified image, but it does not create the pod on the cluster (`--dry-run=client`). The output is directed to `webapp-green.yaml`._
    
	```
	apiVersion: v1
	kind: Pod
	metadata:
	  creationTimestamp: null
	  labels:
		run: webapp-green
	  name: webapp-green
	spec:
	  containers:
	  - image: kodekloud/webapp-color
		name: webapp-green
		args: ["--color=green"] # Arguments passed to the container's command/entrypoint. ["--color", "green"] even this is correct
	```

	This generated YAML shows how to pass arguments to a container using the `args` field. Both `["--color=green"]` and `["--color", "green"]` are valid ways to specify arguments._

	#LAB Practice Test - ConfigMaps
	------------------------------

	Here's a YAML definition for a pod using environment variables directly:

	```
	apiVersion: v1
	kind: Pod
	metadata:
	  labels:
		name: webapp-color
	  name: webapp-color
	  namespace: default
	spec:
	  containers:
	  - env:                                                 # Defines environment variables for the container.
		- name: APP_COLOR                                    # Name of the environment variable.
		  value: green                                       # Hardcoded value for the environment variable.
		name: webapp-color
		image: kodekloud/webapp-color
	```

    **NOTE TO MYSELF**: check why the sequence of `-env` matters here. _This pod `webapp-color` runs an application that uses the `APP_COLOR` environment variable, setting its value directly to `green`._

*   **Create a ConfigMap from literals:**

    ```
    k create configmap webapp-config-map --from-literal=APP_COLOR=darkblue --from-literal=APP_OTHER=disregard
    ```
    This imperative command creates a ConfigMap named `webapp-config-map` and populates it with two key-value pairs: `APP_COLOR=darkblue` and `APP_OTHER=disregard`._

	Here's the YAML of the created ConfigMap:

	```
	apiVersion: v1
	kind: ConfigMap
	metadata:
	  name: webapp-config-map
	  namespace: default
	data: # Data section for key-value pairs.
	  APP_COLOR: darkblue
	  APP_OTHER: disregard
	```

	This YAML shows the structure of the ConfigMap `webapp-config-map` with its defined data._

	Here's a YAML definition for a pod consuming a ConfigMap:

	```
	apiVersion: v1
	kind: Pod
	metadata:
	  labels:
		name: webapp-color
	  name: webapp-color
	  namespace: default
	spec:
	  containers:
	  - env: 											# Defines environment variables for the container.
		- name: APP_COLOR 								# Name of the environment variable.
		  valueFrom: 									# Specifies that the value comes from a source.
		   configMapKeyRef: 							# Refers to a key within a ConfigMap.
			 name: webapp-config-map 					# Name of the ConfigMap.
			 key: APP_COLOR 							# Key within the ConfigMap whose value will be used.
		image: kodekloud/webapp-color
		name: webapp-color
	```

	This pod `webapp-color` now gets its `APP_COLOR` environment variable from the `APP_COLOR` key within the `webapp-config-map` ConfigMap._

	#LAB Practice Test - Security Contexts
	-------------------------------------

	Quick Note: Security context can be set at the container level OR at the pod level.

	Here's an example of setting security context at the pod level:

	```
	spec:
	  securityContext: 						     # Security context applied to all containers in the pod.
		runAsUser: 1000							 # Specifies the UID to run the process as.
		runAsGroup: 3000                         # Specifies the GID to run the primary process of the container as.
		fsGroup: 2000                            # Specifies the GID for the pod's volume and any files created in that volume.
		supplementalGroups: [4000]               # Supplemental groups added to the container's process.
	```

	This snippet demonstrates how to apply security settings globally to all containers within a pod._

	Here's an example of a multi-container pod with security context set at both pod and container levels:

	```
	apiVersion: v1
	kind: Pod
	metadata:
	  name: multi-pod
	spec:
	  securityContext: 								# Pod-level security context.
		runAsUser: 1001
	  containers:
	  - image: ubuntu
		name: web
		command: ["sleep", "5000"]
		securityContext: 							# Container-level security context. This overrides pod-level setting for this container.
		  runAsUser: 1002
	  - image: ubuntu
		name: sidecar
		command: ["sleep", "5000"]
	```

	In this `multi-pod` definition, the `web` containerexplicitly sets `runAsUser` to `1002`, overriding the pod-level `runAsUser` of `1001`. The `sidecar` container will inherit the pod-level `runAsUser` of `1001` as it doesn't specify its own._

*   **Update pod `ubuntu-sleeper` to run as Root user and with the `SYS_TIME` capability.** **NOTE**: By default, containers are run by root unless specified otherwise.
    
	```
	apiVersion: v1
	kind: Pod
	metadata:
	  labels:
		run: ubuntu-sleeper
	  name: ubuntu-sleeper
	spec:
	  containers:
	  - image: ubuntu
		name: ubuntu-sleeper
		command: ["sleep", "5000"]
		securityContext: # Container-level security context.
		  capabilities: # Defines specific capabilities to add or drop.
			add: ["SYS_TIME"] # Adds the SYS_TIME capability, allowing modification of the system clock.
	```

	This YAML modifies the `ubuntu-sleeper` pod to run its container with the `SYS_TIME` capability, allowing it to adjust the system time._

	#LAB Practice Test - Service Accounts
	------------------------------------

*   **Describe a Service Account:**

    ```
    k describe sa default
    ```
    
	This command provides a description of the `default` Service Account in the current namespace._
    
	```
	Name:                default
	Namespace:           default
	Labels:              <none>
	Annotations:         <none>
	Image pull secrets:  <none>
	Mountable secrets:   <none>
	Tokens:              <none>
	Events:              <none>
	```

	This output shows the basic details of the `default` Service Account._

*   **Get Service Account YAML:**
    ```
    k get serviceaccount default -o yaml
    ```
    This command retrieves the YAML definition of the `default` Service Account.
    
	```
	apiVersion: v1
	kind: ServiceAccount
	metadata:
	  creationTimestamp: "2025-01-09T00:34:17Z"
	  name: default
	  namespace: default
	  resourceVersion: "327"
	  uid: 99f5125c-4edd-4318-8858-e426754293d5
	```

	This YAML confirms the existence and basic metadata of the `default` Service Account._

	Tokens are created here: `/var/run/secrets/kubernetes.io/serviceaccount/token`.

	Role Binding binds a role to a service account._

	Here's a YAML example of a Role and RoleBinding:

	```
	---
	kind: RoleBinding
	apiVersion: rbac.authorization.k8s.io/v1
	metadata:
	  name: read-pods
	  namespace: default
	subjects:
	- kind: ServiceAccount # Specifies the type of subject.
	  name: dashboard-sa # Name of the Service Account.
	  namespace: default # Namespace of the Service Account.
	roleRef:
	  kind: Role # This must be Role or ClusterRole.
	  name: pod-reader # This must match the name of the Role or ClusterRole you wish to bind to.
	  apiGroup: rbac.authorization.k8s.io # API group for the role.
	---
	kind: Role
	apiVersion: rbac.authorization.k8s.io/v1
	metadata:
	  namespace: default
	  name: pod-reader # Name of the Role.
	rules: # Defines permissions for the role.
	- apiGroups:
	  - '' # Refers to the core API group.
	  resources:
	  - pods # Resource that this role has permissions over.
	  verbs: # Actions allowed on the resource.
	  - get
	  - watch
	  - list
	```

	This configuration creates a `pod-reader` Role that allows `get`, `watch`, and `list` operations on pods in the `default` namespace. It then creates a `read-pods` RoleBinding that grants these permissions to the `dashboard-sa` Service Account._

	*   **Command to generate a token for a created service account:**
		```
		kubectl create token dashboard-sa
		```
		_This command generates a new token for the `dashboard-sa` Service Account. This token can be used for authentication._

	Service account should be in the same namespace as the RoleBinding._

#LAB Practice Test - Secrets
---------------------------

*   **Command to get all secrets:**
    ```
    kubectl get secrets
    ```
    _This command lists all secrets in the current namespace._
*   **Command to describe a secret:**
    ```
    kubectl describe secret dashboard-token
    ```
    _This command provides detailed information about the `dashboard-token` secret._
*   **Imperative command to create a generic secret:**
    ```
    kubectl create secret generic db-secret --from-literal=DB_Host=sql01 \
    --from-literal=DB_User=root --from-literal=DB_Password=password123
    ```
    _This imperative command creates a generic secret named `db-secret` and populates it with three key-value pairs, where the values are provided as literals._
*   **Secret generated from the above imperative command:**
    ```
    apiVersion: v1
    kind: Secret
    type: Opaque # Type of the secret (generic).
    metadata:
      name: db-secret
    data: # Data section where values are base64 encoded.
      DB_Host: c3FsMDE=                            # automatically base64Encoded when created with imperative command
      DB_Password: cGFzc3dvcmQxMjM=
      DB_User: cm9vdA==
    ```
    _This YAML shows the `db-secret` with its data base64 encoded, which is how secrets store their values._
*   **How to use a secret inside a pod?**
    Here's a YAML definition for a pod consuming a secret by individually referencing keys:
    ```
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        name: webapp-pod
      name: webapp-pod
      namespace: default
    spec:
      containers:
      - name: webapp
        image: kodekloud/simple-webapp-mysql
        env:                                         # Defines environment variables for the container.
        - name: DB_User                              # Name of the environment variable.
          valueFrom:                                 # Specifies that the value comes from a source.
            secretKeyRef:                            # Refers to a key within a Secret.
              name: db-secret                        # Name of the Secret.
              key: DB_User                           # Key within the Secret whose value will be used.
        - name: DB_Host
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: DB_Host
        - name: DB_Password
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: DB_Password
    ```
    _This pod `webapp-pod` consumes the `db-secret` by mapping individual keys from the secret to environment variables within its `webapp` container._
    **Alternative solution (recommended):** While both implementations will work when properly formatted, Implementation 2 is recommended because:
    1.  It's more maintainable.
    2.  Less prone to syntax errors.
    3.  Automatically includes all keys from the secret.
    4.  Requires less code.
    5.  Easier to update when new secret keys are added.
    ```
    apiVersion: v1
    kind: Pod
    metadata:
      labels:
        name: webapp-pod
      name: webapp-pod
      namespace: default
    spec:
      containers:
      - image: kodekloud/simple-webapp-mysql
        imagePullPolicy: Always
        name: webapp
        envFrom:                                   # Specifies that environment variables should be populated from a source.
        - secretRef:                               # Refers to a Secret.
            name: db-secret                        # Name of the Secret from which to take all key-value pairs as environment variables.
    ```
    
	This `webapp-pod` definition uses `envFrom` to inject all key-value pairs from the `db-secret` as environment variables into the `webapp` container. This is a more concise and recommended approach._

#LAB Practice Test - Resource Requirements
-----------------------------------------

### Quick notes

Here's a YAML definition for a `LimitRange` for CPU resources:

```
apiVersion: v1
kind: LimitRange
metadata:
  name: cpu-resource-constraint
spec:
  limits:
  - default: # This section defines default limits for resources.
      cpu: 500m # Default CPU limit for containers if not specified.
    defaultRequest: # This section defines default requests for resources.
      cpu: 500m # Default CPU request for containers if not specified.
    max: # Max defines the upper bound for CPU requests/limits.
      cpu: "1" # Maximum allowed CPU limit for a container.
    min: # Min defines the lower bound for CPU requests/limits.
      cpu: 100m # Minimum allowed CPU request for a container.
    type: Container # Applies to individual containers.
```

**fileName**: `cpu-constraints-pod.yaml` _This `LimitRange` named `cpu-resource-constraint` sets default CPU requests and limits for containers within its namespace, as well as maximum and minimum allowable CPU values._

Here's a YAML definition for a `LimitRange` for memory resources:

```
apiVersion: v1
kind: LimitRange
metadata:
  name: memory-resource-constraint
spec:
  limits:
  - default: # This section defines default limits for resources.
      memeory: 1Gi # Default memory limit for containers if not specified. (Typo: "memeory" should be "memory")
    defaultRequest: # This section defines default requests for resources.
      memeory: 1Gi # Default memory request for containers if not specified. (Typo: "memeory" should be "memory")
    max: # Max defines the upper bound for memory requests/limits.
      memeory: 1G1i # Maximum allowed memory limit for a container. (Typo: "1G1i" should be "1Gi" or similar valid unit)
    min: # Min defines the lower bound for memory requests/limits.
      memeory: 500Mi # Minimum allowed memory request for a container. (Typo: "memeory" should be "memory")
    type: Container # Applies to individual containers.
```

**fileName**: `memory-constraints-pod.yaml` _This `LimitRange` aims to set default memory requests and limits, along with max and min values for containers. Note the typos in "memeory" and "1G1i"._

*   **Applying LimitRange to a specific namespace:**
    ```
    kubectl apply -f constraint-define-yaml-fileName --namespace=<namespace-name>
    ```
    **Example:**
    ```
    kubectl create namespace constraints-cpu-example
    kubectl apply -f cpu-constraints-pod.yaml --namespace=constraints-cpu-example
    ```
    _These commands create a new namespace `constraints-cpu-example` and then apply the `cpu-constraints-pod.yaml` `LimitRange` to that specific namespace._

_A LimitRange does not check the consistency of the default values it applies. This means that a default value for the limit that is set by LimitRange may be less than the request value specified for the container in the spec that a client submits to the API server. If that happens, the final Pod will not be schedulable._

_Then that Pod will not be scheduled, failing with an error similar to:_

```
Pod "example-conflict-with-limitrange-cpu" is invalid: spec.containers[0].resources.requests: Invalid value: "700m": must be less than or equal to cpu limit
```

_This error message indicates that the requested CPU (700m) for a container exceeds the allowed CPU limit defined by a `LimitRange` in the namespace, preventing the pod from being scheduled._

# LAB Practice Test - Taints and Toleration
-----------------------------------------

*   **Taints and Tolerations:**
    *   **Node affinity** is a property of Pods that attracts them to a set of nodes (either as a preference or a hard requirement).
    *   **Taints** are the opposite -- they allow a node to repel a set of pods.
    *   Taints and tolerations work together to ensure that pods are not scheduled onto inappropriate nodes. One or more taints are applied to a node; this marks that the node should not accept any pods that do not tolerate the taints.
*   **To apply a taint:**
    
	```bash 
    kubectl taint nodes node1 key1=value1:NoSchedule
    ```
	
    This command applies a taint with key `key1`, value `value1`, and `NoSchedule` effect to `node1`. This means no new pods will be scheduled on `node1` unless they have a matching toleration.
	
*   **To remove a taint:**
    
	```bash
    kubectl taint nodes node1 key1=value1:NoSchedule-
    ```
    
	The `-` at the end removes the specified taint from `node1`.
	


	Here's a YAML definition for a pod with tolerations:

	```yaml
	apiVersion: v1
	kind: Pod
	metadata:
	  creationTimestamp: null
	  labels:
		run: bee
	  name: bee
	spec:
	  containers:
	  - image: nginx
		name: bee
	  tolerations:                                # Defines tolerations for taints on nodes.
		- key : "spray"                           # Key of the taint to tolerate.
		  operator : "Equal"                      # Operator for matching the taint value.
		  value: "mortein"                        # Value of the taint to tolerate.
		  effect : NoSchedule                     # Effect of the taint (must match the taint's effect).
	```

_This pod `bee` has a toleration for a taint with `key: spray`, `value: mortein`, and `effect: NoSchedule`. This means it can be scheduled on a node tainted with `spray=mortein:NoSchedule`._

*   **Get nodes in all namespaces:**
    
	```shell
    k get nodes --all-namespaces
    ```
    _This command lists all nodes across all namespaces._
*   **Get services:**
    
	```shell
    kubectl get service
    ```
    _This command lists all services in the current namespace._
*   **Taint a node:**
    
	```shell
    kubectl taint nodes node01 spray=mortein:NoSchedule
    ```
    _This command applies a taint `spray=mortein:NoSchedule` to `node01`, preventing pods without a matching toleration from being scheduled on it._
*   **Run a pod:**
    
	```shell
    k run mosquito --image=nginx
    ```
	This command attempts to run a new pod named `mosquito` with the `nginx` image._
    
	```shell
	Events:
	  Type     Reason            Age   From               Message
	  ----     ------            ----  ----               -------
	  Warning  FailedScheduling  56s   default-scheduler  0/2 nodes are available: 1 node(s) had untolerated taint {node-role.kubernetes.io/control-plane: }, 1 node(s) had untolerated taint {spray: mortein}. preemption: 0/2 nodes are available: 2 Preemption is not helpful for scheduling.
	```

	This event log shows that the `mosquito` pod failed to schedule because both available nodes had untolerated taints: one had the `node-role.kubernetes.io/control-plane` taint (which pods usually don't tolerate by default) and the other had the `spray: mortein` taint that `mosquito` does not tolerate.
	
	
	
	NOTE: The below command will list down all the tains on all the nodes
	
	```shell
	# Command to get all nodes taints 
	kubectl get nodes -o custom-columns=NAME:.metadata.name,TAINTS:.spec.taints	
	```
	
	#### **Effect Value Breakdown:**

	- **NoSchedule**: (Hard) Don’t schedule unaffiliated pods on this node.
		- *"Do not allow new pods here unless they can tolerate this taint."*
	- **PreferNoSchedule**: (Soft) Try to avoid, but not a strict rule.
		- *"Prefer not to schedule here, but allow if necessary."*
	- **NoExecute**: Applies to both new pods and existing pods.
		- New pods: Not scheduled unless tolerant.
		- Existing pods: Are evicted UNLESS they tolerate the taint (possibly with tolerationSeconds).


    #### **Tabular Summary (CKAD Reference)**

	| Effect | Scheduling Impact | Running Pod Impact | Supported in Taint? | Supported in Toleration? |
	| :-- | :-- | :-- | :-- | :-- |
	| NoSchedule | New pods not scheduled unless tolerated | No impact | Yes | Yes |
	| PreferNoSchedule | Scheduler avoids node unless necessary | No impact | Yes | Yes |
	| NoExecute | New pods not scheduled unless tolerated | Non-tolerating pods evicted | Yes | Yes |

**References:**

- [Kubernetes Official Docs: Taints and Tolerations (v1.33)](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration)


# LAB Practice Test - Node Affinity
---------------------------------

Here's a YAML definition for a pod with `nodeAffinity`:

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  affinity: # Defines affinity rules for scheduling.
    nodeAffinity: # Specifies node affinity rules.
      requiredDuringSchedulingIgnoredDuringExecution: # A hard requirement for scheduling.
        nodeSelectorTerms:
        - matchExpressions: # A list of node selector requirements.
          - key: disktype # The label key to match.
            operator: In # Operator for the match (e.g., In, NotIn, Exists, DoesNotExist, Gt, Lt).
            values: # List of values for the given key.
            - ssd
  containers:
  - name: nginx
    image: nginx
```

_This pod `nginx` will only be scheduled on nodes that have the label `disktype` with a value of `ssd`._

*   **Apply a label to a node:**
    ```
    k label node node01 color=blue
    ```
    _This command adds the label `color=blue` to `node01`._
*   **Create a new deployment with node affinity:** _Create a new deployment named `blue` with the `nginx` image and 3 replicas._
    ```
    k create deploy blue --image=nginx --replicas=3 -o json
    ```
    _This command imperatively creates a deployment named `blue` with 3 replicas and the `nginx` image, outputting the definition in JSON format._
    
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name : blue
  labels:
   color: blue
spec:
  replicas: 3
  selector:
    matchLabels:
      color: blue
  template:
    metadata:
      labels:
        color: blue
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: color # Match nodes with this label key.
                operator: In
                values:
                - blue # Match nodes where 'color' label has 'blue' value.
      containers:
      - name: blue
        image: nginx
```

_This Deployment `blue` will ensure its 3 replicas are scheduled only on nodes labeled with `color: blue`._

Here's a YAML definition for a Deployment with node affinity targeting the control plane:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name : red
  labels:
   color: red
spec:
  replicas: 2
  selector:
    matchLabels:
      color: red
  template:
    metadata:
      labels:
        color: red
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: node-role.kubernetes.io/control-plane # Match nodes with this specific role label.
                operator: Exists # Check if the label key exists on the node.
      containers:
      - name: blue # Note: Container name is 'blue' but deployment is 'red', might be a typo if not intentional.
        image: nginx
```

_This Deployment `red` aims for 2 replicas and will schedule its pods only on nodes that have the `node-role.kubernetes.io/control-plane` label (i.e., control plane nodes)._

LAB Practice Test - Multi-Container Pods
----------------------------------------

*   **Create a multi-container pod with 2 containers.** _Use the spec given below:_ _If the pod goes into `CrashLoopBackOff`, then add the command `sleep 1000` in the `lemon` container._

_The content for the multi-container pod was missing from the original input._ Here's a possible YAML structure for a multi-container pod (example):

```
apiVersion: v1
kind: Pod
metadata:
  name: my-multi-container-pod
spec:
  containers:
  - name: nginx-container
    image: nginx
    ports:
    - containerPort: 80
  - name: busybox-container
    image: busybox
    command: ["sh", "-c", "echo Hello from busybox; sleep 3600"] # Example command to keep it running
```

_This YAML defines a pod named `my-multi-container-pod` with two containers: `nginx-container` and `busybox-container`._

*   **View logs on a pod (from a specific container):**
    ```
    kubectl -n elastic-stack exec -it app -- cat /log/app.log
    ```
    _This command executes `cat /log/app.log` inside the `app` pod, specifically in the default container (or the first container if multiple are defined), within the `elastic-stack` namespace._

Here's a YAML definition for a multi-container pod demonstrating shared volume:

```
apiVersion: v1
kind: Pod
metadata:
  name: app
  namespace: elastic-stack
  labels:
    name: app
spec:
  containers:
  - name: app
    image: kodekloud/event-simulator
    volumeMounts: # Mounts a volume into the container.
    - mountPath: /log # Path inside the container where the volume will be mounted.
      name: log-volume # Name of the volume to mount.
  - name: sidecar
    image: kodekloud/filebeat-configured
    volumeMounts:
    - mountPath: /var/log/event-simulator/ # Path inside the container.
      name: log-volume # Same volume as above, shared between containers.
  volumes: # Defines volumes that can be mounted into containers.
  - name: log-volume # Name of the volume.
    hostPath: # Specifies a hostPath volume (mounts a file or directory from the host node).
      path: /var/log/webapp # Path on the host machine.
      type: DirectoryOrCreate # Ensures the directory exists, creating it if not.
```

_This pod `app` contains two containers, `app` and `sidecar`. Both containers share a `hostPath` volume named `log-volume`, allowing the `event-simulator` (app container) to write logs to `/log` and the `filebeat-configured` (sidecar container) to read them from `/var/log/event-simulator/`, effectively tailing the logs._

LAB Practice Test – Init Containers
-----------------------------------

Here's a YAML definition for a pod with an init container:

```
apiVersion: v1
kind: Pod
metadata:
  name: red
  namespace: default
spec:
  initContainers: # Defines a list of init containers.
  - image : busybox # Image for the init container.
    name : busybox # Name of the init container.
    command: ["sleep","20"] # Command to execute. This init container will sleep for 20 seconds.
  containers: # Defines the main application containers.
  - command:
    - sh
    - -c
    - echo The app is running! && sleep 3600 # Main container's command.
    image: busybox:1.28
    imagePullPolicy: IfNotPresent
    name: red-container
```

_This pod `red` has an `initContainer` named `busybox` that sleeps for 20 seconds. The `red-container` (main application container) will only start executing its command after the `busybox` init container successfully completes._

LAB Practice Test - Readiness and Liveness Probes
-------------------------------------------------

Here's a YAML definition for a pod with a readiness probe:

```
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: simple-webapp-2
  name: simple-webapp-2
spec:
  containers:
  - image: kodekloud/webapp-delayed-start
    name: simple-webapp-2
    readinessProbe: # Defines a readiness probe.
      httpGet: # Specifies an HTTP GET request to check readiness.
        path: /ready # Path to hit on the container.
        port: 8080 # Port to connect to.
```

_This pod `simple-webapp-2` includes a `readinessProbe` that performs an HTTP GET request to `/ready` on port 8080. The pod will not be considered "ready" until this probe succeeds, meaning it won't receive traffic from Services until then._

Here's a YAML definition for pods with readiness and liveness probes:

```
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: simple-webapp-1
  name: simple-webapp-1
spec:
  containers:
  - image: kodekloud/webapp-delayed-start
    name: simple-webapp-1
    readinessProbe: # Checks if the container is ready to serve traffic.
      httpGet:
        path: /ready
        port: 8080
    livenessProbe: # Checks if the container is still running and healthy.
      httpGet:
        path: /live
        port: 8080
    periodSeconds: 1 # How often (in seconds) to perform the probe.
    initialDelaySeconds: 80 # Number of seconds after the container has started before probes are initiated.
---
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: simple-webapp-2
  name: simple-webapp-2
spec:
  containers:
  - image: kodekloud/webapp-delayed-start
    name: simple-webapp-2
    readinessProbe:
      httpGet:
        path: /ready
        port: 8080
    livenessProbe:
      httpGet:
        path: /live
        port: 8080
    periodSeconds: 1
    initialDelaySeconds: 80
```

_These pod definitions (`simple-webapp-1` and `simple-webapp-2`) both include `readinessProbe` (checking `/ready`) and `livenessProbe` (checking `/live`) on port 8080. They also specify `periodSeconds: 1` for frequent checks and `initialDelaySeconds: 80` to allow the application to start up before probes begin._

*   **Expose pods as LoadBalancer services:**
    ```
    kubectl expose pod simple-webapp-1 --port=8080 --name=webapp-service-1 --type=LoadBalancer
    kubectl expose pod simple-webapp-1 --port=8080 --name=webapp-service-1 --type=LoadBalancer # Duplicate command
    ```
    _These commands expose the `simple-webapp-1` pod as a `LoadBalancer` type service named `webapp-service-1` on port 8080. Note that the second command is a duplicate and would likely result in an error if the first service already exists._

LAB Practice Test - Container Logging
-------------------------------------

*   **View pod logs:**
    ```
    kubectl logs <pod-name>
    ```
    _This command displays the logs for the specified pod._
*   **View pod logs with grep:**
    ```
    kubectl logs <pod-name> | grep 'search string'
    ```
    _This pipes the pod's logs to `grep`, allowing you to filter for specific strings._
*   **Stream pod logs:**
    ```
    kubectl logs -f <pod-name>
    ```
    _The `-f` flag "follows" the logs, continuously displaying new log entries as they appear._

LAB Practice Test - Monitoring
------------------------------

*   **Deploying Metrics Server:**
    ```
    kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
    ```
    _This command applies the official YAML manifest for the Metrics Server, which is required for `kubectl top` commands to function._
    
```
serviceaccount/metrics-server created
clusterrole.rbac.authorization.k8s.io/system:aggregated-metrics-reader created
clusterrole.rbac.authorization.k8s.io/system:metrics-server created
rolebinding.rbac.authorization.k8s.io/metrics-server-auth-reader created
clusterrolebinding.rbac.authorization.k8s.io/metrics-server:system:auth-delegator created
clusterrolebinding.rbac.authorization.k8s.io/system:metrics-server created
service/metrics-server created
deployment.apps/metrics-server created
apiservice.apiregistration.k8s.io/v1beta1.metrics.k8s.io created
```

_This output confirms the successful creation of various Kubernetes resources necessary for the Metrics Server, including Service Accounts, Roles, RoleBindings, a Service, a Deployment, and an APIService._

*   **Get Node Metrics:**
    ```
    kubectl top node
    ```
    _This command displays CPU and memory utilization for all nodes in the cluster, gathered by the Metrics Server._
    
```
NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
controlplane   282m         1%     907Mi           1%
node01         27m          0%     185Mi           0%
```

_This shows the current resource usage for `controlplane` and `node01`._

*   **Get Pod Metrics:**
    ```
    kubectl top pod
    ```
    _This command displays CPU and memory utilization for pods in the current namespace, gathered by the Metrics Server._
    
```
NAME       CPU(cores)   MEMORY(bytes)
elephant   21m          30Mi
lion       1m           16Mi
rabbit     147m         250Mi
```

_This output shows the resource usage for pods named `elephant`, `lion`, and `rabbit`._

LAB Practice Test - Labels, Selectors and Annotations
-----------------------------------------------------

*   **Command to get all the pods with label `env=dev`:**
    ```
    kubectl get pods -l env=dev
    ```
    _The `-l` flag is used to filter resources by label, here showing pods with `env` label equal to `dev`._
*   **Command to get all the pods with label `env=prod`:**
    ```
    kubectl get all -l env=prod
    ```
    _This command retrieves all resource types (pods, services, deployments, etc.) that have the label `env=prod`._
*   **Command to get all the pods with multiple labels `[env=prod,bu=finance,tier=frontend]`:**
    ```
    kubectl get pod -l env=prod,bu=finance,tier=frontend
    ```
    _Multiple labels can be specified separated by commas, meaning all labels must match._
*   **ReplicaSet definition, where replica-set pod template label should match with selector label.**
    
```
apiVersion: apps/v1
kind: ReplicaSet
metadata:
   name: replicaset-1
spec:
   replicas: 2
   selector:
      matchLabels: # Defines the labels that pods must have to be managed by this ReplicaSet.
        tier: front-end
   template: # Defines the pod template for new pods created by this ReplicaSet.
     metadata:
       labels: # These labels *must* match the selector labels.
        tier: front-end
     spec:
       containers:
       - name: nginx
         image: nginx
```

_This `ReplicaSet` definition demonstrates the critical relationship between `selector.matchLabels` and `template.metadata.labels`. For a `ReplicaSet` to manage pods, the labels defined in its `template` must match the labels specified in its `selector`._

LAB Practice Test - Rolling Updates & Rollbacks
-----------------------------------------------

*   **Perform a rolling update on a deployment and record the change:**
    ```
    kubectl set image deployment/frontend simple-webapp=kodekloud/webapp-color:v2 --record=true
    ```
    _This command updates the `simple-webapp` container's image in the `frontend` Deployment to `kodekloud/webapp-color:v2`. The `--record=true` flag (though deprecated) was historically used to record the command in the deployment's history for easier rollback tracking._
    **NOTE**: The `record` flag is getting deprecated.
*   **Check the status of a rolling update:**
    ```
    kubectl rollout status deployment/frontend
    ```
    _This command provides real-time information on the progress of a rolling update for the `frontend` Deployment._
*   **View the rollout history of a deployment:**
    ```
    kubectl rollout history deployment/frontend
    ```
    _This command shows the revision history of the `frontend` Deployment, useful for understanding past changes and for rollbacks._
*   **Describe a deployment to see its details and update strategy:**
    ```
    kubectl describe deployment frontend
    ```
    _This command provides comprehensive details about the `frontend` Deployment, including its status, update strategy, and associated ReplicaSets._
    
```
Name:                   frontend
Namespace:              default
CreationTimestamp:      Sat, 29 Mar 2025 08:46:40 +0000
Labels:                 <none>
Annotations:            deployment.kubernetes.io/revision: 2
                        kubernetes.io/change-cause: kubectl set image deployment/frontend simple-webapp=kodekloud/webapp-color:v2 --record=true
Selector:               name=webapp
Replicas:               4 desired | 4 updated | 4 total | 4 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        20
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  name=webapp
  Containers:
   simple-webapp:
    Image:         kodekloud/webapp-color:v2
    Port:          8080/TCP
    Host Port:     0/TCP
    Environment:   <none>
    Mounts:        <none>
  Volumes:         <none>
  Node-Selectors:  <none>
  Tolerations:     <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  frontend-6765b99794 (0/0 replicas created)
NewReplicaSet:   frontend-854b57fbbf (4/4 replicas created)
Events:
  Type    Reason             Age    From                   Message
  ----    ------             ----   -------                -------
  Normal  ScalingReplicaSet  10m    deployment-controller  Scaled up replica set frontend-6765b99794 from 0 to 4
  Normal  ScalingReplicaSet  3m17s  deployment-controller  Scaled up replica set frontend-854b57fbbf from 0 to 1
  Normal  ScalingReplicaSet  3m17s  deployment-controller  Scaled down replica set frontend-6765b99794 from 4 to 3
  Normal  ScalingReplicaSet  3m17s  deployment-controller  Scaled up replica set frontend-854b57fbbf from 1 to 2
  Normal  ScalingReplicaSet  2m56s  deployment-controller  Scaled down replica set frontend-6765b99794 from 3 to 1
  Normal  ScalingReplicaSet  2m56s  deployment-controller  Scaled up replica set frontend-854b57fbbf from 2 to 4
  Normal  ScalingReplicaSet  2m34s  deployment-controller  Scaled down replica set frontend-6765b99794 from 1 to 0
```

_This `describe` output details the `frontend` Deployment. Key information includes: `StrategyType: RollingUpdate`, `Replicas: 4 desired | 4 updated | 4 total | 4 available`, and `RollingUpdateStrategy: 25% max unavailable, 25% max surge`. This means during an update, a maximum of 1 pod can be unavailable, and a maximum of 1 new pod can be created beyond the desired replica count._

*   **Initiate another rolling update:**
    ```
    kubectl set image deployment/frontend simple-webapp=kodekloud/webapp-color:v3
    ```
    _This command initiates a new rolling update for the `frontend` Deployment, changing the image to `kodekloud/webapp-color:v3`._

LAB Practice Test - Deployment Strategies
-----------------------------------------

*   **Get services with wide output:**
    ```
    kubectl get service -o wide
    ```
    _This command lists services and includes additional details like external IP and selector._
    
```
NAME               TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE     SELECTOR
frontend-service   NodePort    172.20.154.102   <none>        8080:30080/TCP   78s     app=frontend
kubernetes         ClusterIP   172.20.0.1       <none>        443/TCP          8m57s   <none>
```

_This output shows `frontend-service` as a `NodePort` service, exposing port 8080 internally and 30080 externally, targeting pods with `app=frontend`._

**Blue-Green Deployment Strategy** _This strategy involves running two identical production environments (Blue and Green). At any time, only one of the environments is live. When a new version is released, it's deployed to the inactive environment (e.g., Green), tested, and then traffic is switched over by updating a Service or Ingress. If issues arise, traffic can be instantly rolled back to the old (Blue) environment._

**Canary Deployment Strategy** _This strategy involves slowly rolling out a new version of an application to a small subset of users (the "canary group") before rolling it out to the entire infrastructure and making it available to everyone. This minimizes risk by exposing the new version to a controlled audience._

*   **Scale down a deployment (example during canary):**
    ```
    kubectl scale --current-replicas=5 --replicas=4 deployment/frontend
    kubectl scale --current-replicas=2 --replicas=1 deployment/frontend-v2
    ```
    _These commands are used to manually adjust the number of replicas for deployments, often part of a canary or blue-green strategy to shift traffic gradually or completely._
*   **Get deployments status:**
    ```
    kubectl get deploy
    ```
    _This command shows the current state of deployments, including `READY`, `UP-TO-DATE`, and `AVAILABLE` replicas._
    
```
NAME          READY   UP-TO-DATE   AVAILABLE   AGE
frontend      4/4     4            4           10m
frontend-v2   1/1     1            1           8m7s
```

_This shows two deployments: `frontend` fully available with 4 replicas, and `frontend-v2` with 1 replica, possibly in a canary setup._

```
controlplane ~ ➜  k get deploy
NAME          READY   UP-TO-DATE   AVAILABLE   AGE
frontend      0/0     0            0           12m
frontend-v2   5/5     5            5           10m
```

_This shows a state where the `frontend` deployment has been scaled down to 0 replicas, and `frontend-v2` has been scaled up to 5 replicas, indicating a full transition from the old version to the new one._

LAB Practice Test - Jobs & CronJobs
-----------------------------------

**Job** _Jobs are used to run a specified number of pods to completion. They ensure that a given number of successful completions are achieved before the Job is marked as complete._

Here's a YAML definition for a Job that runs once:

```
apiVersion: batch/v1
kind: Job
metadata:
  name: throw-dice-job
spec:
  completions: 1     # exits when 1 container is sucessful (specifies the number of successful pod completions).
  template:
    spec:
      containers:
      - name: throw-dice-job
        image: kodekloud/throw-dice
      restartPolicy: Never # Specifies that the pod should not be restarted if it completes.
```

_This Job `throw-dice-job` will create one pod running `kodekloud/throw-dice`, and the Job will be considered complete once that single pod finishes successfully._

**Job Definition - 2**

```
apiVersion: batch/v1
kind: Job
metadata:
  name: throw-dice-job
spec:
  completions: 2   # exits when 2 container is sucessful (The Job will wait for 2 successful pod completions).
  template:
    spec:
      containers:
      - name: throw-dice-job
        image: kodekloud/throw-dice
      restartPolicy: Never
```

_This Job `throw-dice-job` now requires 2 successful completions before it is marked as finished._

**Job Definition - 3**

```
apiVersion: batch/v1
kind: Job
metadata:
  name: throw-dice-job
spec:
  completions: 3       # exits when 3 container is sucessful (The Job will wait for 3 successful pod completions).
  parallelism: 3       # runs 3 container in parallel (Specifies how many pods should run concurrently).
  template:
    spec:
      containers:
      - name: throw-dice-job
        image: kodekloud/throw-dice
      restartPolicy: Never
```

_This Job `throw-dice-job` will run 3 pods concurrently (`parallelism: 3`) and will complete once 3 of these pods have successfully finished (`completions: 3`)._

*   **Command to force recreate jobs from a file:**
    ```
    k replace --force -f throw-dice-job.yaml
    ```
    _This command forces the replacement of an existing `throw-dice-job` with the definition in `throw-dice-job.yaml`. The `--force` flag ensures that the old resource is deleted before the new one is created, which is useful for applying changes that might not be mutable in place._

**CronJob** - _a job that gets triggered at a specific time._ _CronJobs are used to create Jobs on a repeating schedule._

Here's a YAML definition for a CronJob:

```
apiVersion: batch/v1
kind: CronJob
metadata:
  name: throw-dice-cron-job
spec:
  schedule: "30 21 * * *" # Cron schedule: "minute hour day-of-month month day-of-week" (21:30 every day).
  jobTemplate: # Template for the Job to be created.
    spec:
      completions: 3
      parallelism: 3
      template:
        spec:
          containers:
            - name: throw-dice-job
              image: kodekloud/throw-dice
          restartPolicy: Never
```

_This `CronJob` named `throw-dice-cron-job` will create a Job (with 3 completions and 3 parallel pods) every day at 21:30 (9:30 PM)._

LAB Practice Test - Services
----------------------------

*   **Create base service definition using Imperative Command Reference:**
    *   **ClusterIP Service** is not exposed to the outside world.
    *   **LoadBalancer Service** is exposed to the outside world (requires cloud provider integration).
    *   **NodePort Service** exposes a service on a static port on each Node's IP.
*   **Create a NodePort service imperatively and output to YAML:**
    ```
    kubectl create service nodeport webapp-service --tcp=8080:30080 --node-port=30080 -o yaml > service-definition-2.yaml
    ```
    _This command creates a NodePort service named `webapp-service`. It maps TCP port 8080 on the service to the container's target port (which is implicitly also 8080 in this usage, or needs to be specified with `--target-port`) and exposes it on node port 30080. The output is saved to `service-definition-2.yaml`._
*   **Edit `service-definition-2.yaml`:**
    ```
    apiVersion: v1
    kind: Service
    metadata:
      creationTimestamp: "2025-01-08T03:46:05Z"
      labels:
        app: webapp-service
      name: webapp-service
      namespace: default
    spec:
      type: NodePort # Specifies the service type as NodePort.
      ports:
      - name: webapp-service-port # Name of the service port.
        nodePort: 30080 # The port on each node that the service is exposed on.
        port: 8080 # The port on which the service is exposed.
        targetPort: 8080 # The port on the pod to which the service sends traffic.
      selector: # Selects pods with matching labels to route traffic to.
        name : simple-webapp
    ```
    _This YAML defines a `NodePort` service named `webapp-service`. It listens on ClusterIP port 8080, and is exposed on each node's IP at port 30080. It directs traffic to pods labeled `name: simple-webapp` on their container port 8080._

LAB Practice Test - Ingress Networking - 1
------------------------------------------

Here's a YAML for an Ingress resource (original from provided file):

```
apiVersion: v1
items:
- apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    annotations:
      nginx.ingress.kubernetes.io/rewrite-target: / # Rewrites the URL path before sending to the backend service.
      nginx.ingress.kubernetes.io/ssl-redirect: "false" # Disables SSL redirection.
    creationTimestamp: "2025-06-17T10:44:29Z"
    generation: 1
    name: ingress-wear-watch
    namespace: app-space
    resourceVersion: "865"
    uid: ecffaa56-fb31-4072-8a89-1fd4332c0e03
  spec:
    rules:
    - http:
        paths:
        - backend: # Defines the backend service for the path.
            service:
              name: wear-service
              port:
                number: 8080
          path: /wear # Path for the ingress rule.
          pathType: Prefix # Matches any URL starting with /wear.
        - backend:
            service:
              name: wear-service # Duplicate entry, likely a copy-paste error.
              port:
                number: 8080
          path: /wear
          pathType: Prefix
        - backend:
            service:
              name: video-service
              port:
                number: 8080
          path: /stream
          pathType: Prefix
  status:
    loadBalancer:
      ingress:
      - ip: 172.20.71.208
kind: List
metadata:
  resourceVersion: ""
```

_This Ingress `ingress-wear-watch` in `app-space` is configured to route traffic. Requests to `/wear` are directed to `wear-service:8080` (with a duplicate entry). Requests to `/stream` are directed to `video-service:8080`. The `nginx.ingress.kubernetes.io/rewrite-target: /` annotation ensures that the path prefix (e.g., `/wear` or `/stream`) is stripped before the request is forwarded to the backend service._

Here's a corrected/modified YAML for an Ingress resource:

```
apiVersion: v1
items:
- apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    annotations:
      nginx.ingress.kubernetes.io/rewrite-target: /
      nginx.ingress.kubernetes.io/ssl-redirect: "false"
    creationTimestamp: "2025-06-17T10:44:29Z"
    generation: 1
    name: ingress-wear-watch
    namespace: app-space
    resourceVersion: "865"
    uid: ecffaa56-fb31-4072-8a89-1fd4332c0e03
  spec:
    rules:
    - http:
        paths:
        - backend:
            service:
              name: wear-service
              port:
                number: 8080
          path: /wear
          pathType: Prefix
        - backend:
            service:
              name: video-service
              port:
                number: 8080
          path: /stream
          pathType: Prefix
        - backend: # New rule added for /eat.
            service:
              name: food-service
              port:
                number: 8080
          path: /eat
          pathType: Prefix
  status:
    loadBalancer:
      ingress:
      - ip: 172.20.71.208
kind: List
metadata:
  resourceVersion: ""
```

_This Ingress definition now includes an additional rule to route traffic from `/eat` to `food-service:8080`._

**`critical-space/Pay App`**

```
apiVersion: v1
kind: List
items:
- apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    annotations:
      nginx.ingress.kubernetes.io/rewrite-target: / # Rewrites the URL path.
      nginx.ingress.kubernetes.io/ssl-redirect: "false"
    name: critical-ingress
    namespace: critical-space # Specifies the namespace for this Ingress.
  spec:
    rules:
    - http:
        paths:
        - backend:
            service:
              name: pay-service
              port:
                number: 8282
          path: /pay # Path to match for routing.
          pathType: Prefix
```

_This Ingress `critical-ingress` in the `critical-space` namespace routes traffic from `/pay` to `pay-service:8282`, also using `rewrite-target: /`._

*   **Create an Ingress imperatively:**
    ```
    kubctl create ingress ingress-pay -n critical-space --rule="/pay=pay-service:8282"
    ```
    _This imperative command creates an Ingress named `ingress-pay` in the `critical-space` namespace, with a rule that routes requests to `/pay` to `pay-service` on port 8282._

_Without the `rewrite-target` option, this is what would happen:_

`http://<ingress-service>:<ingress-port>/watch --> http://<watch-service>:<port>/watch` `http://<ingress-service>:<ingress-port>/wear --> http://<wear-service>:<port>/wear`

_To fix that we want to "ReWrite" the URL when the request is passed on to the watch or wear applications._

```
annotations:
      nginx.ingress.kubernetes.io/rewrite-target: /  # this will rewrite the backend URL and remove the /pay when forwarding the request.
```

_The `nginx.ingress.kubernetes.io/rewrite-target: /` annotation is crucial for stripping the path prefix (e.g., `/wear`, `/watch`, `/pay`) from the URL before forwarding the request to the backend service. This means the backend service receives a request for `/` instead of `/wear` or `/watch`._

_With the `rewrite-target`:_

`http://<ingress-service>:<ingress-port>/watch --> http://<watch-service>:<port>` `http://<ingress-service>:<ingress-port>/pay --> http://<pay-service>:<port>`

```
controlplane ~ ➜  k describe clusterrolebindings ingress-nginx -n=ingress-nginx
Name:         ingress-nginx
Labels:       app.kubernetes.io/instance=ingress-nginx
              app.kubernetes.io/managed-by=Helm
              app.kubernetes.io/name=ingress-nginx
              app.kubernetes.io/part-of=ingress-nginx
              app.kubernetes.io/version=1.1.2
              helm.sh/chart=ingress-nginx-4.0.18
Annotations:  <none>
Role:
  Kind:  ClusterRole
  Name:  ingress-nginx
Subjects:
  Kind            Name           Namespace
  ----            ----           ---------
  ServiceAccount  ingress-nginx  ingress-nginx

controlplane ~ ✖ k describe clusterrolebindings ingress-nginx-admission -n=ingress-nginx
Name:         ingress-nginx-admission
Labels:       app.kubernetes.io/component=admission-webhook
              app.kubernetes.io/instance=ingress-nginx
              app.kubernetes.io/managed-by=Helm
              app.kubernetes.io/name=ingress-nginx
              app.kubernetes.io/part-of=ingress-nginx
              app.kubernetes.io/version=1.1.2
              helm.sh/chart=ingress-nginx-4.0.18
Annotations:  helm.sh/hook: pre-install,pre-upgrade,post-install,post-upgrade
              helm.sh/hook-delete-policy: before-hook-creation,hook-succeeded
Role:
  Kind:  ClusterRole
  Name:  ingress-nginx-admission
Subjects:
  Kind            Name                     Namespace
  ----            ----                     ---------
  ServiceAccount  ingress-nginx-admission  ingress-nginx
```

_These `describe clusterrolebindings` commands show the permissions granted to the `ingress-nginx` and `ingress-nginx-admission` Service Accounts in the `ingress-nginx` namespace. These bindings are essential for the NGINX Ingress Controller to function correctly._

```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app.kubernetes.io/component: controller
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
    app.kubernetes.io/version: 1.1.2
    helm.sh/chart: ingress-nginx-4.0.18
  name: ingress-nginx-controller
  namespace: ingress-nginx
spec:
  minReadySeconds: 0
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      app.kubernetes.io/component: controller
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/name: ingress-nginx
  template:
    metadata:
      labels:
        app.kubernetes.io/component: controller
        app.kubernetes.io/instance: ingress-nginx
        app.kubernetes.io/name: ingress-nginx
    spec:
      containers:
      - args:
        - /nginx-ingress-controller
        - --publish-service=$(POD_NAMESPACE)/ingress-nginx-controller
        - --election-id=ingress-controller-leader
        - --watch-ingress-without-class=true
        - --default-backend-service=app-space/default-http-backend # Specifies a default backend for requests that don't match any rules.
        - --controller-class=k8s.io/ingress-nginx
        - --ingress-class=nginx
        - --configmap=$(POD_NAMESPACE)/ingress-nginx-controller
        - --validating-webhook=:8443
        - --validating-webhook-certificate=/usr/local/certificates/cert
        - --validating-webhook-key=/usr/local/certificates/key
        env:
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: POD_NAMESPACE
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace
        - name: LD_PRELOAD
          value: /usr/local/lib/libmimalloc.so
        image: registry.k8s.io/ingress-nginx/controller:v1.1.2@sha256:28b11ce69e57843de44e3db6413e98d09de0f6688e33d4bd384002a44f78405c
        imagePullPolicy: IfNotPresent
        lifecycle:
          preStop:
            exec:
              command:
              - /wait-shutdown
        livenessProbe:
          failureThreshold: 5
          httpGet:
            path: /healthz
            port: 10254
            scheme: HTTP
          initialDelaySeconds: 10
          periodSeconds: 10
          successThreshold: 1
          timeoutSeconds: 1
          resources:
          requests:
            cpu: 100m
            memory: 90Mi
        securityContext:
          allowPrivilegeEscalation: true
          capabilities:
            add:
            - NET_BIND_SERVICE
            drop:
            - ALL
          runAsUser: 101
        volumeMounts:
        - mountPath: /usr/local/certificates/
          name: webhook-cert
          readOnly: true
      dnsPolicy: ClusterFirst
      nodeSelector:
        kubernetes.io/os: linux
      serviceAccountName: ingress-nginx
      terminationGracePeriodSeconds: 300
      volumes:
      - name: webhook-cert
        secret:
          secretName: ingress-nginx-admission
---
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: null
  labels:
    app.kubernetes.io/component: controller
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
    app.kubernetes.io/version: 1.1.2
    helm.sh/chart: ingress-nginx-4.0.18
  name: ingress-nginx-controller
  namespace: ingress-nginx
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
    nodePort: 30080 # Exposes the controller on this node port.
  selector:
    app.kubernetes.io/component: controller
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/name: ingress-nginx
  type: NodePort
```

_This extensive YAML defines the NGINX Ingress Controller Deployment and its associated Service. The Deployment manages the controller pods, configured with various arguments for ingress handling, webhooks, and resource limits. The Service, of type `NodePort`, exposes the Ingress Controller on port 80 (mapping to container port 80) and on node port 30080, making it accessible from outside the cluster._

*   **Create Ingress with multiple rules:**
    ```
    k create ingress ingress-wear-watch -n app-space --rule="/wear=wear-service:8080" --rule="/watch=video-service:8080"
    ```
    _This imperative command creates an Ingress named `ingress-wear-watch` in the `app-space` namespace with two rules: `/wear` mapping to `wear-service:8080` and `/watch` mapping to `video-service:8080`._

LAB Practice Test - Network Policies
------------------------------------

*   **Get network policies in all namespaces:**
    ```
    k get networkpolicy -A
    ```
    _This command lists all NetworkPolicy resources across all namespaces in the cluster._
*   **Get pods by label:**
    ```
    kubectl get pods -l key=value
    ```
    _This command filters and displays pods that have a specific label `key=value`._

Here's a YAML definition for a NetworkPolicy:

```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: internal-policy
  namespace: default
spec:
  podSelector: # Selects the pods to which this policy applies.
    matchLabels:
      name: internal # This policy applies to pods with the label 'name: internal'.
  policyTypes: # Specifies the types of policies (Ingress, Egress).
  - Egress # This policy only applies to outbound traffic.
  egress: # Defines rules for outbound traffic.
  - to: # Specifies allowed destinations.
    - podSelector: # Selects pods as destinations.
        matchLabels:
          name: mysql # Allows egress to pods with 'name: mysql'.
    ports: # Specifies allowed ports for the egress rule.
    - port: 3306
      protocol: TCP
  - to:
    - podSelector:
        matchLabels:
          name: payroll # Allows egress to pods with 'name: payroll'.
    ports:
    - port: 8080
      protocol: TCP
  - ports: # Allows egress to any destination on these ports.
     - port: 53
       protocol: UDP
     - port: 53
       protocol: TCP
```

_This `internal-policy` NetworkPolicy applies to pods labeled `name: internal` in the `default` namespace. It defines `Egress` (outbound) rules: allowing TCP traffic on port 3306 to pods labeled `name: mysql`, TCP traffic on port 8080 to pods labeled `name: payroll`, and UDP/TCP traffic on port 53 (DNS) to any destination._

*   **Describe a NetworkPolicy:**
    ```
    controlplane ~ ➜  k describe networkpolicy internal-policy
    Name:         internal-policy
    Namespace:    default
    Created on:   2025-06-17 18:02:02 +0000 UTC
    Labels:       <none>
    Annotations:  <none>
    Spec:
      PodSelector:     name=internal
      Not affecting ingress traffic
      Allowing egress traffic:
        To Port: 3306/TCP
        To:
          PodSelector: name=mysql
        ----------
        To Port: 8080/TCP
        To:
          PodSelector: name=payroll
        ----------
        To Port: 53/UDP
        To Port: 53/TCP
        To: <any> (traffic not restricted by destination)
      Policy Types: Egress
    ```
    _This `describe` output confirms the details of `internal-policy`: it targets pods with `name=internal`, only affects `Egress` traffic, and specifies the allowed outbound destinations and ports, including DNS traffic on ports 53 UDP/TCP to any destination._

LAB Practice Test - Persistent Volumes
--------------------------------------

*   **Execute a command inside a pod to view logs:**
    ```
    kubectl exec webapp -- cat /log/app.log
    ```
    _This command executes `cat /log/app.log` inside the `webapp` pod, typically to view application logs stored in a mounted volume._

Here's a YAML definition for a pod using a `hostPath` volume:

```
apiVersion: v1
kind: Pod
metadata:
  name: webapp
spec:
  containers:
    - name: webapp
      image: kodekloud/event-simulator
      volumeMounts: # Mounts volumes into the container.
        - name: vol-1 # Name of the volume to mount.
          mountPath: /log # Path inside the container where the volume is mounted.
  volumes: # Defines volumes available to the pod.
    - name: vol-1
      hostPath: # A volume that mounts a file or directory from the host node.
        path: /var/log/webapp # Path on the host machine.
```

_This `webapp` pod uses a `hostPath` volume named `vol-1` to store data from the container's `/log` directory directly onto the host's `/var/log/webapp` directory. This means data will persist even if the pod is deleted, as long as the node exists._

Here's a YAML definition for a PersistentVolume:

```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-log
spec:
  capacity: # Defines the storage capacity of the PV.
    storage: 100Mi
  accessModes: # Defines how the volume can be accessed (e.g., ReadWriteOnce, ReadWriteMany).
    - ReadWriteMany # Allows the volume to be mounted as read-write by many nodes.
  volumeMode: Filesystem # Specifies the volume mode as a filesystem.
  persistentVolumeReclaimPolicy: Retain # Defines what happens to the volume when the PVC is deleted. 'Retain' means the volume is kept for manual reclamation.
  hostPath: # Specifies a hostPath volume, common for learning/testing but not recommended for production.
    path: /pv/log # Path on the host machine where the volume data resides.
```

_This `PersistentVolume` named `pv-log` is a `hostPath` volume with 100Mi capacity, allowing `ReadWriteMany` access. Its `Retain` reclaim policy means the underlying data on the host will not be deleted when the associated `PersistentVolumeClaim` is deleted._

Here's a YAML definition for a PersistentVolumeClaim:

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: claim-log-1
spec:
  accessModes: # Requests the access mode for the volume.
    - ReadWriteMany # Requests the ability to be mounted read-write by many nodes.
  resources: # Specifies the storage resources requested.
    requests:
      storage: 50Mi # Requests 50Mi of storage.
```

_This `PersistentVolumeClaim` named `claim-log-1` requests 50Mi of storage with `ReadWriteMany` access. This PVC will attempt to bind to a suitable `PersistentVolume` that matches these criteria._

Here's a YAML definition for a pod using a PersistentVolumeClaim:

```
apiVersion: v1
kind: Pod
metadata:
  name: webapp
spec:
  containers:
  - name: webapp
    image: kodekloud/event-simulator
    volumeMounts: # Mounts volumes into the container.
    - mountPath: /usr # Path inside the container where the volume is mounted.
      name : pv-storage # Name of the volume to mount.
  volumes: # Defines volumes available to the pod.
    - name: pv-storage
      persistentVolumeClaim: # Specifies that the volume is backed by a PVC.
        claimName: claim-log-1 # Name of the PersistentVolumeClaim to use.
```

_This `webapp` pod mounts the `claim-log-1` PVC to `/usr` inside its `webapp` container. This allows the pod to use the storage provisioned by the `PersistentVolume` that the PVC is bound to._

LAB Practice Test - Storage Class
---------------------------------

Here's a YAML definition for a PersistentVolumeClaim referencing a StorageClass:

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-pvc
spec:
  storageClassName : local-storage # Specifies the StorageClass to use for dynamic provisioning.
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
```

_This `PersistentVolumeClaim` named `local-pvc` explicitly requests storage from a `StorageClass` named `local-storage`. It requests 500Mi of storage with `ReadWriteOnce` access mode._

**NOTE**: The Storage Class called `local-storage` makes use of `VolumeBindingMode` set to `WaitForFirstConsumer`. This will delay the binding and provisioning of a PersistentVolume until a Pod using the PersistentVolumeClaim is created. _This note highlights an important characteristic of `WaitForFirstConsumer` binding mode: it delays the actual provisioning of the PV until a pod attempts to use the PVC, which can be useful for topology-aware scheduling._

Here's a YAML definition for a pod using a PersistentVolumeClaim:

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:alpine
    volumeMounts: # Mounts volumes into the container.
    - mountPath: /var/www/html # Path inside the container where the volume is mounted.
      name : pv-storage # Name of the volume to mount.
  volumes: # Defines volumes available to the pod.
    - name: pv-storage
      persistentVolumeClaim: # Specifies that the volume is backed by a PVC.
        claimName: local-pvc # Name of the PersistentVolumeClaim to use.
```

_This `nginx` pod mounts the `local-pvc` to `/var/www/html` within its `nginx` container, thereby utilizing the storage provisioned by the `local-storage` StorageClass._

Here's a YAML definition for a StorageClass:

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: low-latency
  annotations:
    storageclass.kubernetes.io/is-default-class: "false" # Explicitly marks this as not the default StorageClass.
provisioner: kubernetes.io/no-provisioner # Indicates a static provisioner (manual PV creation).
reclaimPolicy: Retain # Default value is Delete. 'Retain' means the PV is not deleted when the PVC is deleted.
allowVolumeExpansion: true # Allows volumes created by this StorageClass to be expanded.
mountOptions: # Optional mount options for the volume.
  - discard # This might enable UNMAP / TRIM at the block storage layer.
volumeBindingMode: WaitForFirstConsumer # Delays PV binding until a pod requests it.
parameters: # Provider-specific parameters.
  guaranteedReadWriteLatency: "true" # provider-specific
```

_This `StorageClass` named `low-latency` is a non-default class with `kubernetes.io/no-provisioner`, meaning PersistentVolumes associated with it must be manually created. It has a `Retain` reclaim policy, allows volume expansion, and uses `WaitForFirstConsumer` binding mode for topology-aware provisioning._

LAB Practice Test - KubeConfig
------------------------------

*   **View kubeconfig file:**
    ```
    vi /root/.kube/config
    ```
    _This command opens the default `kubeconfig` file in the `vi` editor. This file contains cluster connection details, user credentials, and contexts._
*   **Switch context in kubeconfig:**
    ```
    kubectl config --kubeconfig=/root/my-kube-config use-context research
    ```
    _This command sets the current context to `research` within the specified `my-kube-config` file. A context is a combination of a cluster, a user, and a namespace._
*   **Set alias for kubectl:**
    ```
    vi ~/.bashrc
    alias k=kubectl
    ```
    _These commands add an alias `k` for `kubectl` to the `~/.bashrc` file, making it easier to execute `kubectl` commands by typing `k`._
*   **Execute kubectl command with explicit client certificates and key (less common):**
    ```
    kubectl get pods --client-certificate=/etc/kubernetes/pki/users/dev-user/dev-user.crt --client-key=/etc/kubernetes/pki/users/dev-user/dev-user.key --certificate-authority=/etc/kubernetes/pki/users/dev-user/dev-user.csr
    ```
    _This command directly uses client certificate and key files for authentication to list pods. This method is generally avoided in favor of `kubeconfig` files for better manageability._
*   **Create/set credentials in a kubeconfig file:**
    ```
    kubectl config set-credentials dev-user \
      --client-certificate=/etc/kubernetes/pki/users/dev-user/dev-user.csr \
      --client-key=/etc/kubernetes/pki/users/dev-user/dev-user.key \
      --kubeconfig=/root/.kube/config
    ```
    _This command adds (or updates) a user named `dev-user` in the `/root/.kube/config` file, using the specified client certificate and key files for authentication._
*   **View kubeconfig file:**
    ```
    k config view --kubeconfig=/root/.kube/config
    ```
    _This command displays the contents of the specified `kubeconfig` file._

LAB Practice Test Role Based Access Controls
--------------------------------------------

*   **Inspect kube-apiserver process for admission plugins:**
    ```
    ps aux | grep kube-apiserver
    ```
    _This command lists all running processes and filters for `kube-apiserver`, which can reveal its configuration flags, including enabled admission plugins._
*   **Create a Role with specific verbs and resources:**
    ```
    kubectl create role developer --verb=list --verb=create --verb=delete --resource=pods
    ```
    _This imperative command creates a `Role` named `developer` in the current namespace that grants permissions to `list`, `create`, and `delete` pods._
*   **Create a RoleBinding:**
    ```
    kubectl create rolebinding dev-user-binding --role=developer --user=dev-user
    ```
    _This imperative command creates a `RoleBinding` named `dev-user-binding` that binds the `developer` Role to the `dev-user` user in the current namespace._
*   **Check user permissions:**
    ```
    k auth can-i --as dev-user pod describe -n blue
    ```
    _This command checks if `dev-user` has permission to `describe` pods in the `blue` namespace. It's a useful tool for verifying RBAC configurations._
    
```
controlplane ~ ✦ ✖ k describe role developer -n blue
Name:         developer
Labels:       <none>
Annotations:  <none>
PolicyRule:
  Resources  Non-Resource URLs  Resource Names  Verbs
  ---------  -----------------  --------------  -----
  pods       []                 [blue-app]      [get watch create delete]
```

_This `describe` output shows that the `developer` Role in the `blue` namespace has `get`, `watch`, `create`, and `delete` permissions specifically on the `blue-app` pod resource._

*   **Force replace a Role:**
    ```
    k replace --force -f developer-role.yaml
    ```
    _This command forces the replacement of an existing `developer` Role with the definition in `developer-role.yaml`._
    
```
controlplane ~ ✦ ➜  k describe role developer -n blue
Name:         developer
Labels:       <none>
Annotations:  <none>
PolicyRule:
  Resources  Non-Resource URLs  Resource Names   Verbs
  ---------  -----------------  --------------   -----
  pods       []                 [dark-blue-app]  [get watch create delete]
```

_This updated `describe` output indicates that the `developer` Role's permissions are now restricted to the `dark-blue-app` pod._

```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  creationTimestamp: "2025-06-21T02:32:33Z"
  name: developer
  namespace: blue
  resourceVersion: "4733"
  uid: cd331a6d-7ec7-45ac-91f6-b1f04e42b48e
rules:
- apiGroups:
  - "" # Core API group
  resourceNames:
  - dark-blue-app # Specific resource name the rule applies to.
  resources:
  - pods
  verbs:
  - get
  - watch
  - create
  - delete
- apiGroups:
  - "apps" # API group for Deployments, ReplicaSets etc.
  resources:
  - deployments
  verbs:
  - create
  - list
```

_This YAML defines the `developer` Role, granting `get`, `watch`, `create`, `delete` permissions on the `dark-blue-app` pod, and `create`, `list` permissions on `deployments` within the `apps` API group in the `blue` namespace._

Here's a YAML definition for a ClusterRole providing node access:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole # A ClusterRole grants permissions across all namespaces.
metadata:
  name: NodeAccessClusterRoles
rules:
- apiGroups: [""] # Core API group.
  resources: ["nodes"] # Resource: nodes.
  verbs: ["*"] # All verbs (actions) on nodes.
```

_This `ClusterRole` named `NodeAccessClusterRoles` grants full access (`*` verb) to `nodes` resources across the entire cluster. This is a very broad permission and should be used with caution._

Here's a YAML definition for a ClusterRoleBinding:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding # Binds a ClusterRole to a subject (user, group, or service account).
metadata:
  name: NodeAccessClusterRoles-michelle
subjects: # List of subjects that will be granted the role's permissions.
- kind: User # Type of subject.
  name: michelle # Name of the user.
  apiGroup: rbac.authorization.k8s.io
roleRef: # Reference to the Role or ClusterRole being bound.
  kind: ClusterRole
  name: NodeAccessClusterRoles
  apiGroup: rbac.authorization.k8s.io
```

_This `ClusterRoleBinding` named `NodeAccessClusterRoles-michelle` grants the `NodeAccessClusterRoles` (full access to nodes) to the user `michelle` across the entire cluster._

*   **Get API resources and filter by storage:**
    ```
    kubectl api-resources
    controlplane ~ ➜  kubectl api-resources | grep storage
    csidrivers                                       storage.k8s.io/v1                 false        CSIDriver
    csinodes                                         storage.k8s.io/v1                 false        CSINode
    csistoragecapacities                             storage.k8s.io/v1                 true         CSIStorageCapacity
    storageclasses                      sc           storage.k8s.io/v1                 false        StorageClass
    volumeattachments                                storage.k8s.sio/v1                 false        VolumeAttachment
    persistentvolumes                   pv           v1                                false        PersistentVolume
    ```
    _`kubectl api-resources` lists all API resources available in the cluster. Piping it to `grep storage` filters for storage-related resources, showing their `APIGroup`, `Kind`, `shortnames`, etc._

Here's a YAML definition for a ClusterRole for storage administration:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: storage-admin
rules:
- apiGroups: [""] # Core API group for PersistentVolumes.
  resources: ["persistentvolumes"]
  verbs: ["*"] # Full access to PersistentVolumes.
- apiGroups: ["storage.k8s.io"] # API group for StorageClasses.
  resources: ["storageclasses"]
  verbs: ["*"] # Full access to StorageClasses.
```

_This `ClusterRole` named `storage-admin` grants full administrative access (`*` verb) to both `persistentvolumes` (in the core API group) and `storageclasses` (in the `storage.k8s.io` API group) across the cluster._

Here's a YAML definition for a ClusterRoleBinding for storage administration:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: michelle-storage-admin
subjects:
- kind: User
  name: michelle
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: storage-admin
  apiGroup: rbac.authorization.k8s.io
```

_This `ClusterRoleBinding` named `michelle-storage-admin` grants the `storage-admin` ClusterRole to the user `michelle`, giving her full administrative control over PersistentVolumes and StorageClasses._

*   **Check user permissions:**
    ```
    kubectl auth can-i get pv
    kubectl auth can-i get sc
    ```
    _These commands verify if the current user (or a specified user) has the `get` permission on `PersistentVolume` (`pv`) and `StorageClass` (`sc`) resources._
*   **Inspect kube-apiserver configuration:**
    ```
    cat /etc/kubernetes/manifests/kube-apiserver.yaml | grep admission
    ```
    _This command is used to inspect the `kube-apiserver.yaml` manifest file, specifically looking for lines related to `admission` controllers, which enforce policies on object creation/updates._
    ```
    ps -ef | grep kube-apiserver | grep admission-plugins
    ```
    _This command filters running processes to find the `kube-apiserver` and then checks its command-line arguments for `admission-plugins`, revealing which admission controllers are enabled._
    ```
    kubectl get pods -n kube-system
    ```
    _This command lists pods running in the `kube-system` namespace, which often includes core Kubernetes components._
    ```
    ps -ef | grep kube-apiserver | grep mutating
    ```
    _This command specifically looks for `mutating` admission webhooks configured for the `kube-apiserver`._
*   **Create a TLS secret for a webhook:**
    ```
    kubectl create secret tls webhook-server-tls --cert=/root/keys/webhook-server-tls.crt --key=/root/keys/webhook-server-tls.key -n webhook-demo
    ```
    _This command creates a TLS secret named `webhook-server-tls` in the `webhook-demo` namespace, using provided certificate and key files. This secret is typically used by webhook servers for secure communication._
*   **Get API resources and filter by storage (duplicate):**
    ```
    kubectl api-resources | grep storage
    ```
    _This command (repeated) lists storage-related API resources._
*   **Convert an old Ingress YAML to a new API version:**
    ```
    kubectl convert -f ingress-old.yaml --local -o json > ingress-new.yaml
    ```
    _This command converts the `ingress-old.yaml` file (assuming it's using an older Ingress API version) to the latest API version. The `--local` flag performs the conversion client-side without interacting with the cluster, and `-o json` outputs the result in JSON format to `ingress-new.yaml`._



---
# Quick Notes


## Kubernetes Node Scheduling Mechanisms

| **Mechanism** | **When to Use** | **How it Works** | **Use Case Examples** | **Flexibility** |
|---------------|-----------------|------------------|----------------------|-----------------|
| **nodeSelector** | Simple node selection based on exact label match | Pods scheduled only on nodes with matching key-value labels | • Dev pods on dev nodes<br>• GPU workloads on GPU nodes<br>• Region-specific deployments| **Low** - Exact match only |
| **Node Affinity** | Complex node selection with multiple conditions and preferences | Advanced rule-based scheduling with required/preferred conditions | • Multi-zone deployments<br>• Hardware-specific requirements<br>• Complex label combinations<br>• Soft/hard preferences  | **High** - Multiple operators, AND/OR logic |
| **Taints** | Prevent pods from being scheduled on specific nodes (node repels pods) | Nodes marked with taints that repel pods without matching tolerations | • Dedicated nodes for specific workloads<br>• Master nodes (no regular pods)<br>• Maintenance mode<br>• Isolating problematic nodes | **Medium** - Works with tolerations |
| **Tolerations** | Allow pods to be scheduled on tainted nodes (pod tolerates taint) | Pods with tolerations can be scheduled on nodes with matching taints | • System pods on master nodes<br>• Special workloads on dedicated nodes<br>• Pods that can handle node issues  | **Medium** - Must match taint keys/effects |


# Detailed Explanation of Kubernetes Node Scheduling Examples

## 1. nodeSelector Example

```yaml
spec:
  nodeSelector:
    environment: production
    gpu: "true"
```

### What this does:
- **Simple filtering**: This pod will ONLY be scheduled on nodes that have BOTH labels
- **Exact match required**: The node must have `environment=production` AND `gpu=true` labels
- **Binary decision**: Either the node matches ALL criteria or the pod won't be scheduled there

### Step-by-step process:
1. Kubernetes scheduler looks at all available nodes
2. Filters out nodes that don't have `environment: production` label
3. From remaining nodes, filters out those without `gpu: "true"` label
4. Schedules pod on any remaining node that matches both criteria
5. If no nodes match, pod remains in "Pending" state

### Real-world scenario:
```yaml
# First, label your nodes:
# kubectl label nodes gpu-node-1 environment=production
# kubectl label nodes gpu-node-1 gpu=true

apiVersion: v1
kind: Pod
metadata:
  name: ml-training-job
spec:
  nodeSelector:
    environment: production
    gpu: "true"
  containers:
  - name: tensorflow
    image: tensorflow/tensorflow:latest-gpu
```

---

## 2. Node Affinity Example

```yaml
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: zone
            operator: In
            values: ["us-west-1a", "us-west-1b"]
```

### What this does:
- **Flexible matching**: Pod can be scheduled on nodes in EITHER `us-west-1a` OR `us-west-1b` zones
- **Operator-based logic**: Uses `In` operator to check if node's zone label matches any value in the list
- **Required rule**: This is a hard requirement (pod won't be scheduled if no matching nodes exist)

### Breaking down the components:
- **`requiredDuringSchedulingIgnoredDuringExecution`**: Hard requirement during scheduling, but ignored if node changes after pod is running
- **`nodeSelectorTerms`**: Array of terms (OR logic between terms)
- **`matchExpressions`**: Array of expressions (AND logic within a term)
- **`operator: In`**: Node label value must be in the specified list

### Advanced example with multiple conditions:
```yaml
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: zone
            operator: In
            values: ["us-west-1a", "us-west-1b"]
          - key: instance-type
            operator: NotIn
            values: ["t2.micro", "t2.small"]
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        preference:
          matchExpressions:
          - key: zone
            operator: In
            values: ["us-west-1a"]
```

### Available operators:
- **`In`**: Label value is in the list
- **`NotIn`**: Label value is not in the list
- **`Exists`**: Label key exists (regardless of value)
- **`DoesNotExist`**: Label key doesn't exist
- **`Gt`**: Label value is greater than specified value
- **`Lt`**: Label value is less than specified value

---

## 3. Taints Example

```yaml
# Applied to Node
spec:
  taints:
  - key: dedicated
    value: gpu
    effect: NoSchedule
  - key: node-role.kubernetes.io/master
    effect: NoSchedule
```

### What this does:
- **Node-level restriction**: These taints are applied to a node to repel pods
- **Two taints applied**: One custom taint for GPU dedication, one standard master node taint
- **NoSchedule effect**: Prevents new pods from being scheduled (existing pods remain)

### Taint effects explained:
1. **`NoSchedule`**: New pods without matching tolerations won't be scheduled
2. **`PreferNoSchedule`**: Scheduler tries to avoid placing pods, but not guaranteed
3. **`NoExecute`**: Existing pods without tolerations are evicted, new ones rejected

### How to apply taints:
```bash
# Taint a node for GPU workloads only
kubectl taint nodes gpu-node-1 dedicated=gpu:NoSchedule

# Taint master nodes (usually done automatically)
kubectl taint nodes master-node node-role.kubernetes.io/master:NoSchedule

# Remove a taint (notice the minus sign)
kubectl taint nodes gpu-node-1 dedicated=gpu:NoSchedule-
```

### Real-world scenarios:
- **Dedicated hardware**: Prevent regular workloads from using expensive GPU/SSD nodes
- **Maintenance mode**: Taint nodes before maintenance to prevent new pods
- **Problem nodes**: Taint nodes with hardware issues to isolate them
- **Master nodes**: Prevent application pods from running on control plane nodes

---

## 4. Tolerations Example

```yaml
spec:
  tolerations:
  - key: "dedicated"
    operator: "Equal"
    value: "gpu"
    effect: "NoSchedule"
  - key: "node-role.kubernetes.io/master"
    effect: "NoSchedule"
```

### What this does:
- **Pod-level permission**: Allows this pod to be scheduled on tainted nodes
- **Matches taints**: First toleration matches the `dedicated=gpu:NoSchedule` taint
- **Master access**: Second toleration allows scheduling on master nodes

### Toleration operators:
1. **`Equal`**: Taint key, value, and effect must match exactly
2. **`Exists`**: Only taint key and effect need to match (ignores value)

### Detailed breakdown:

#### First toleration:
```yaml
- key: "dedicated"
    operator: "Equal"
    value: "gpu"
    effect: "NoSchedule"
```
- Matches taint: `dedicated=gpu:NoSchedule`
- Pod can be scheduled on nodes with this specific taint

#### Second toleration:
```yaml
- key: "node-role.kubernetes.io/master"
    effect: "NoSchedule"
```
- Operator defaults to "Equal" when not specified
- Since no value is provided, it matches any taint with this key and effect
- Allows pod to run on master nodes

### Complete example with context:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: gpu-ml-job
spec:
  tolerations:
  - key: "dedicated"
    operator: "Equal"
    value: "gpu"
    effect: "NoSchedule"
  nodeSelector:
    gpu: "true"
  containers:
  - name: training-container
    image: tensorflow/tensorflow:latest-gpu
    resources:
      limits:
        nvidia.com/gpu: 1
```

### Special toleration patterns:
```yaml
# Tolerate all taints (dangerous - use carefully)
tolerations:
- operator: "Exists"

# Tolerate all taints with specific effect
tolerations:
- key: ""
  operator: "Exists"
  effect: "NoSchedule"

# Tolerate for limited time (useful for temporary issues)
tolerations:
- key: "node.kubernetes.io/unreachable"
  operator: "Exists"
  effect: "NoExecute"
  tolerationSeconds: 300
```

## How They Work Together

### Complete workflow example:
1. **Administrator** taints GPU nodes: `kubectl taint nodes gpu-node dedicated=gpu:NoSchedule`
2. **Regular pods** cannot be scheduled on GPU nodes (due to taint)
3. **ML workload pods** include tolerations for `dedicated=gpu:NoSchedule`
4. **ML pods** can now be scheduled on GPU nodes
5. **Optional**: Add nodeSelector or affinity to ensure ML pods ONLY go to GPU nodes

This creates a dedicated pool of resources while maintaining flexibility and control over pod placement.



