# Kubernetes Practice Test - 1 Solutions

 

## Response:
* * *

### Task 1: Create and Mount a Persistent Volume and PVC

**Task Description:** Create a Persistent Volume (PV) named `log-volume` with a `manual` storage class, `ReadWriteMany` (RWX) access mode, and a size of 1Gi. The volume should use the host path `/opt/volume/nginx`. Next, create a Persistent Volume Claim (PVC) named `log-claim` requesting a minimum of 200Mi of storage, ensuring it binds to `log-volume`. Finally, mount this PVC in a pod called `logger` at the location `/var/www/nginx`, using the `nginx:alpine` image.

**Solution:**

The following YAML defines the Persistent Volume, Persistent Volume Claim, and the Pod as per the requirements.


**PersistentVolume definition**
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: log-volume                     # Name of the Persistent Volume 
spec:
  storageClassName: manual             # Specifies the storage class 
  capacity:
    storage: 1Gi                       # Defines the size of the volume 
  accessModes:
    - ReadWriteMany                    # Sets the access mode to ReadWriteMany (RWX) 
  hostPath:
    path: /opt/volume/nginx            # Specifies the host path for the volume 
```

**PersistentVolumeClaim definition**

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: log-claim                      # Name of the Persistent Volume Claim
spec:
  storageClassName: manual             # Must match the storageClassName of the PV to bind 
  resources:
    requests:
     storage: 200Mi                    # Requests a minimum of 200Mi of storage 
  accessModes:
   - ReadWriteMany                     # Must match the access modes of the PV 
```

**Pod definition**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: logger                         # Name of the pod
  labels:
    run: logger
spec:
  containers:
   - name: logger                      # Name of the container
     image: nginx:alpine               # Uses the nginx:alpine image 
     volumeMounts:
      - name : log                     # Name of the volume mount, references the volume defined below 
        mountPath : /var/www/nginx     # Path inside the container where the volume will be mounted 
  volumes:
   - name : log                        # Name of the volume
     persistentVolumeClaim :
       claimName : log-claim           # Binds to the log-claim PVC
```

**Explanation:**

*   **PersistentVolume (`log-volume`):** This resource defines a piece of storage in the cluster. It's configured with a `manual` storage class, allowing explicit binding to a PVC. The `1Gi` capacity and `ReadWriteMany` access mode are specified, along with the `hostPath` `/opt/volume/nginx`, meaning the data will be stored directly on the node's filesystem at that location.
*   **PersistentVolumeClaim (`log-claim`):** This resource is a request for storage by a user. It requests `200Mi` of storage and specifies `ReadWriteMany` access and the `manual` storage class, which allows it to bind to our pre-defined `log-volume`.
*   **Pod (`logger`):** This pod runs an `nginx:alpine` image. It mounts the `log-claim` PVC to the `/var/www/nginx` directory inside the container. This ensures that any data written to `/var/www/nginx` by the `nginx` container will be persistently stored on the host path defined by `log-volume`.

### Task 2: Troubleshoot Network Policy for `secure-pod`

**Task Description:** A pod named `secure-pod` and a service named `secure-service` have been deployed, but incoming or outgoing connections to `secure-pod` are not working. Troubleshoot this issue and ensure that incoming connections from the `webapp-color` pod are successful. Do not delete any existing objects.

**Solution:**

The issue is likely due to a restrictive NetworkPolicy. The provided NetworkPolicy snippet only allows ingress from `webapp-color` on port 80. To ensure incoming connections from `webapp-color` are successful, the existing NetworkPolicy needs to be correctly applied and verified.

**NetworkPolicy definition**
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: webapp-color-network-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      run: secure-pod                         # This policy applies to pods with the label 'run: secure-pod' [cite: 9]
  policyTypes:
    - Ingress                                 # Specifies that this policy applies to incoming connections [cite: 9]
  ingress:
    - from :
        podSelector:
          matchLabels:
            name: webapp-color                # Allows ingress from pods with the label 'name: webapp-color' [cite: 9]
      ports:
        - protocol: TCP
          port :80                            # Allows ingress on TCP port 80 [cite: 9]
```

**Explanation:**

defautlDenyAll network policy is created, which blocks all the incomming connection between the pods. A new networkPolicy `netpol` was needed allow incomming (ingress) connection from webapp-color pod to secure-pod pod. 

The above NetworkPolicy, `webapp-color-network-policy`, is configured to target `secure-pod` (via `podSelector: matchLabels: run: secure-pod`). It sets an `Ingress` policy type, meaning it controls incoming connections. The `ingress` rule specifically allows connections _only_ from pods with the label `name: webapp-color` on TCP port `80`. This policy restricts all other incoming connections to `secure-pod`. To ensure connections from `webapp-color` are successful, this policy needs to be correctly deployed.



**Verification (Bash Command):**

To test connectivity from `webapp-color` to `secure-service` on port 80:

# Command to test connectivity from webapp-color to secure-service on port 80
```bash
kubectl exec -it webapp-color -- sh -c "nc -v -z -w 5 secure-service 80"
```

Command Breakdown:

1. `kubectl exec` - Executes a command inside a running container
2. `-it`          - Interactive terminal flags:
3. `-i`           - Keep STDIN open (interactive)
4. `-t`           - Allocate a pseudo-TTY (terminal)
5. `webapp-color` - The target pod name
6. `--`           - Separates kubectl arguments from the command to execute
7. `sh -c`        - Runs the following command in a shell

Note : `kubectl exec -it webapp-color -- sh -c`  - commands mentioned after this will be executed in the shell 

8. `nc`              - netcat (network utility for reading/writing network connections)
9. `-v`              - Verbose output (shows connection details)
10. `-z`             - Zero-I/O mode (just scan for listening daemons, don't send data)
11. `-w 5`           - Timeout after 5 seconds
12. `secure-service` - Target service name (Kubernetes service)
13. `80`             - Target port number (HTTP port)

**Outcome:**

If the NetworkPolicy is correctly applied, the

`nc` command from `webapp-color` to `secure-service` on port 80 should succeed, indicating that incoming connections from `webapp-color` are now working as expected. Other connections not explicitly allowed by this policy will continue to be blocked.

### Task 3: Create a Pod with ConfigMap-driven Environment Variable and Volume

**Task Description:** Create a pod named `time-check` in the `dvl1987` namespace. This pod should run a container also called `time-check` using the `busybox` image. Create a ConfigMap named `time-config` with the data `TIME_FREQ=10` in the same namespace. The `time-check` container should execute the command `while true; do date; sleep $TIME_FREQ; done` and write the result to `/opt/time/time-check.log`. The `/opt/time` path on the pod should mount a volume that lasts the lifetime of the pod.

**Solution:**

First, create the namespace and ConfigMap using imperative commands.

**Command to create the dvl1987 namespace**
```bash
kubectl create namespace dvl1987 
```

**Comand to create the time-config ConfigMap in the dvl1987 namespace with the TIME_FREQ variable**
```bash
kubectl create configmap time-config --from-literal=TIME_FREQ=10 --namespace=dvl1987 
```

Then, define the Pod in YAML.

**Pod definition**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: time-check                             # Name of the pod 
  labels:
    run: time-check
    namespace : dvl1987                        # Specifies the namespace for the pod 
spec:
  containers:
   - name: time-check                          # Name of the container 
     image: busybox                            # Uses the busybox image 
     command: ["sh", "-c"]                     # Specifies the shell command interpreter
     args:
      - while true; 
	  do 
	    date; 
		sleep $(TIME_FREQ); 
		echo date >  /opt/time/time-check.log; 
	  done;                                     # The command to execute, logging date and sleeping based on TIME_FREQ 
     env:
      - name: TIME_FREQ                         # Environment variable name 
        valueFrom:
          configMapKeyRef :
            name : time-config                  # Refers to the time-config ConfigMap 
            key : TIME_FREQ                     # Retrieves the value of TIME_FREQ from the ConfigMap 
     volumeMounts:
      - name : log                              # Name of the volume mount
        mountPath : /opt/time                   # Path inside the container where the volume will be mounted 
  volumes:
   - name : log                                 # Name of the volume
     emptyDir: {}                               # Defines an emptyDir volume, which lasts the lifetime of the pod 
```

**Explanation:**

*   **Namespace Creation:** The command `kubectl create namespace dvl1987` creates a dedicated namespace for our resources, ensuring better organization and isolation.
*   **ConfigMap Creation:** The command `kubectl create configmap time-config --from-literal=TIME_FREQ=10 --namespace=dvl1987` creates a ConfigMap named `time-config` that stores the `TIME_FREQ` variable with a value of `10`. This allows us to inject configuration data into the pod.
*   **Pod (`time-check`):**
    *   The pod is deployed in the `dvl1987` namespace.
    *   The `time-check` container uses the `busybox` image.
    *   The
        `command` and `args` execute a shell script that continuously prints the current `date`, then `sleeps` for a duration specified by the `TIME_FREQ` environment variable, and redirects the output to `/opt/time/time-check.log`.
    *   The
        `TIME_FREQ` environment variable's value is sourced directly from the `time-config` ConfigMap using `valueFrom.configMapKeyRef`.
    *   An `emptyDir` volume named `log` is defined and mounted at `/opt/time` within the container. An `emptyDir` volume is created when a pod is assigned to a node and exists as long as that pod is running on that node. When the pod is removed from a node, the data in the
        `emptyDir` is deleted permanently. This ensures the log file persists for the pod's lifetime.

* * *

### Task 4: Nginx Deployment and Rollout Management

**Task Description:** Create an Nginx deployment with 4 replicas. Then, update the image and perform a rollout undo.

**Solution:**

First, create the initial Deployment YAML.

**Imperative command to create a dry-run YAML for an Nginx deployment with 4 replicas**
```bash
kubectl create deployment nginx-deploy --image=nginx:1.16 --replicas=4 --dry-run=client -o yaml > nginx-deploy.yaml
```

** Nginx Deployment definition:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy                       # Name of the deployment
  namespace : default                      # Namespace for the deployment
  labels:
    name: nginx-deploy
spec:
   replicas: 4                             # Desired number of pod replicas 
   selector:
     matchLabels:
       app: nginx                          # Selector to identify pods managed by this deployment
   strategy:
     type: RollingUpdate                   # Specifies the rollout strategy as RollingUpdate 
     rollingUpdate:
       maxSurge : 1                        # Maximum number of pods that can be created above the desired number of pods 
       maxUnavailable: 2                   # Maximum number of pods that can be unavailable during the update process 
   template:
     metadata:
       labels:
         app: nginx                        # Labels applied to the pods created by this deployment
    spec:
      containers:
      - name: nginx                        # Name of the container
        image: nginx:1.16                  # Initial Nginx image version 
```

**Explanation:**

The `nginx-deploy.yaml` defines a Deployment named `nginx-deploy` in the `default` namespace with 4 replicas. It uses a `RollingUpdate` strategy, allowing for updates with `maxSurge` of 1 (one extra pod can be created) and `maxUnavailable` of 2 (two pods can be unavailable during the update). The pods will run the

`nginx:1.16` image.

**Deployment and Rollout Commands (Bash):**

```
# Apply the Nginx deployment YAML
kubectl apply -f nginx-deploy.yaml

# Update the Nginx image to version 1.17 and record the change
kubectl set image deployment nginx-deploy nginx=nginx:1.17 --record

# Undo the last rollout (revert to the previous image)
kubectl rollout undo deployment nginx-deploy

# View the rollout history of the deployment
kubectl rollout history deployment nginx-deploy
```

**Outcome:**

*   `kubectl apply -f nginx-deploy.yaml`: This command creates the `nginx-deploy` deployment with 4 pods running `nginx:1.16`.
*   `kubectl set image deployment nginx-deploy nginx=nginx:1.17 --record`: This **imperative command** updates the `nginx` container's image in the `nginx-deploy` deployment to `nginx:1.17`. The
    `--record` flag is crucial as it saves the command in the revision history, making it easier to track changes.
*   `kubectl rollout undo deployment nginx-deploy`: This **imperative command** reverts the deployment to its previous revision (i.e., back to `nginx:1.16`). This is useful for quickly rolling back problematic updates.
*   `kubectl rollout history deployment nginx-deploy`: This **imperative command** displays the revision history of the `nginx-deploy` deployment, showing each change and its associated `CHANGE-CAUSE` if `--record` was used.

* * *

### Task 5: Redis Deployment, Resource Updates, and Rollback

**Task Description:** Create a Redis deployment with 1 replica and a ConfigMap. Then, update its CPU requests multiple times and perform a rollout undo.

**Solution:**

First, create the initial Deployment YAML and ConfigMap.

```
# Imperative command to create a dry-run YAML for a Redis deployment with 1 replica
kubectl create deployment redis --image=redis:alpine --replicas=1 --dry-run=client -o yaml > redis.yaml

# Create a ConfigMap named redis-config with the data CONFIG_VALUE=test
kubectl create configmap redis-config --from-literal=CONFIG_VALUE=test
```

**`redis.yaml`:**

```
# Redis Deployment definition
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: redis
  [cite_start]name: redis # Name of the deployment 
spec:
  [cite_start]replicas: 1 # Desired number of pod replicas 
  selector:
    matchLabels:
      app: redis
  strategy: {} # Default strategy (RollingUpdate)
  template:
    metadata:
      labels:
        app: redis
    spec:
      volumes:
        - name: data
          emptyDir: {} # Volume for Redis data, lasts the lifetime of the pod
        - name: redis-config
          configMap:
            [cite_start]name: redis-config # Mounts the redis-config ConfigMap [cite: 20]
      containers:
      - [cite_start]image: redis:alpine # Redis image 
        name: redis # Name of the container
        volumeMounts:
          - mountPath: /redis-master-data
            name: data # Mounts the data volume
          - mountPath: /redis-master
            [cite_start]name: redis-config # Mounts the redis-config ConfigMap [cite: 20]
        ports :
          - [cite_start]containerPort : 6379 # Exposes port 6379 for Redis [cite: 21]
        resources:
          requests:
            [cite_start]cpu: "0.2" # Initial CPU request [cite: 21]
```

**Explanation:**

The

`redis.yaml` defines a Deployment named `redis` with 1 replica. It includes two volumes: an

`emptyDir` for data and a `configMap` volume that mounts the `redis-config` ConfigMap. The Redis container uses the

`redis:alpine` image and initially requests `0.2` CPU.

**Deployment, Resource Updates, and Rollback Commands (Bash):**

```
# Apply the Redis deployment YAML
kubectl apply -f redis.yaml

# Set CPU requests for the redis deployment to 0.3 and record the change
kubectl set resources deployment redis --requests=cpu=0.3 --record 

# Update the Redis image to redis:alpine3.21 and record the change
kubectl set image deployment redis redis=redis:alpine3.21 --record

# Set CPU requests for the redis deployment to 0.4 and record the change
kubectl set resources deployment redis --requests=cpu=0.4 --record 

# View the rollout history of the redis deployment
kubectl rollout history deployment redis 

# Undo the last rollout (revert to the previous revision)
kubectl rollout undo deployment redis
```

**Outcome:**

*   `kubectl apply -f redis.yaml`: This command deploys the Redis application.
*   `kubectl set resources deployment redis --requests=cpu=0.3 --record`: This **imperative command** updates the CPU resource requests for the `redis` deployment to `0.3`. The
    `--record` flag ensures this change is logged in the revision history.
*   `kubectl set image deployment redis redis=redis:alpine3.21 --record`: This **imperative command** updates the Redis image to `redis:alpine3.21`.
*   `kubectl set resources deployment redis --requests=cpu=0.4 --record`: This **imperative command** further updates the CPU resource requests to `0.4`.
*   `kubectl rollout history deployment redis`: This **imperative command** shows the complete revision history for the `redis` deployment, detailing each change, including the `kubectl set` commands used.
*   `kubectl rollout undo deployment redis`: This **imperative command** rolls back the `redis` deployment to its previous successful revision. In this case, it would revert the CPU request from `0.4` to `0.3` and the image from `redis:alpine3.21` to `redis:alpine`.
    
```
# Example output of kubectl rollout history deployment redis
deployment.apps/redis
REVISION  CHANGE-CAUSE
1         <none>
2         kubectl set resources deployment redis --requests=cpu=0.3 --record=true # First resource update 
3         kubectl set image deployment redis redis=redis:alpine3.21 --record=true # Image update 
4         kubectl set resources deployment redis --requests=cpu=0.4 --record=true # Second resource update 
```

This output clearly illustrates the **revision history** and the **change-cause** for each revision, demonstrating the effectiveness of the `--record` flag for auditing and troubleshooting.

* * *



---
Powered by [Gemini Exporter](https://www.geminiexporter.com)