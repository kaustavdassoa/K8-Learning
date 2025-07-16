# LAB : Practice Test - Pods

**Important kubeCLT commands**

list pods
```
kubectl get pods
```
Discribe a pod 
```
kubectl describe pod <pod-name>
```
create a pod with ngix image 

```
kubectl run ngix --image=nginx 
kubectl run redis --image=redis123
```



```
kubectl get pods -o wide

NAME            READY   STATUS    RESTARTS   AGE     IP           NODE           NOMINATED NODE   READINESS GATES
newpods-h7b7b   1/1     Running   0          4m15s   10.42.0.10   controlplane   <none>           <none>
newpods-pllpx   1/1     Running   0          4m15s   10.42.0.9    controlplane   <none>           <none>
newpods-w9w4l   1/1     Running   0          4m15s   10.42.0.11   controlplane   <none>           <none>
ngix            1/1     Running   0          2m43s   10.42.0.13   controlplane   <none>           <none>
```

````
kubectl get pods
 
NAME            READY   STATUS             RESTARTS   AGE
newpods-h7b7b   1/1     Running            0          4m54s
newpods-pllpx   1/1     Running            0          4m54s
newpods-w9w4l   1/1     Running            0          4m54s
ngix            1/1     Running            0          3m22s
webapp          1/2     ImagePullBackOff   0          27s
````

```
kubectl describe pod webapp 

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

  
NOTE: Total number of running pods/Total number of pods

```

**Edit Pods**

```
kubectl set image (-f FILENAME | TYPE NAME) CONTAINER_NAME_1=CONTAINER_IMAGE_1 ... CONTAINER_NAME_N=CONTAINER_IMAGE_N
NOTE : TYPE NAME = pod (po), replicationcontroller (rc), deployment (deploy), daemonset (ds), statefulset (sts), cronjob (cj), replicaset (rs)

kubectl set image po redis redis=redis 
```

```
kubectl edit pod <pod-name> 
```

NOTE : Please note that only the properties listed below are editable.
spec.containers[*].image
spec.initContainers[*].image
spec.activeDeadlineSeconds
spec.tolerations
spec.terminationGracePeriodSeconds


# LAB Practice Test - ReplicaSets

```
kubectl describe rs new-replica-set 
```

```yaml
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
  replicas: 4
  selector:
    matchLabels:
      name: busybox-pod
  template:
    metadata:
      creationTimestamp: null
      labels:
        name: busybox-pod
    spec:
      containers:
      - command:
        - sh
        - -c
        - echo Hello Kubernetes! && sleep 3600
        image: busybox777
        imagePullPolicy: Always
        name: busybox-container
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
status:
  fullyLabeledReplicas: 4
  observedGeneration: 1
  replicas: 4
```

```  
kubectl get rs 
NAME              DESIRED   CURRENT   READY   AGE
new-replica-set   4         4         0       3m17s
```

```
kubectl get pods
```

```
NAME                    READY   STATUS             RESTARTS   AGE
new-replica-set-2r2rv   0/1     ImagePullBackOff   0          4m22s
new-replica-set-hgbgm   0/1     ImagePullBackOff   0          4m22s
new-replica-set-lpvsm   0/1     ImagePullBackOff   0          4m22s
new-replica-set-pbrlq   0/1     ImagePullBackOff   0          4m22s
```

```
kubectl get pod new-replica-set-2r2rv 

NAME                    READY   STATUS             RESTARTS   AGE
new-replica-set-2r2rv   0/1     ImagePullBackOff   0          4m34s
```

```
kubectl describe pod new-replica-set-2r2rv 
```

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
    Image:         busybox777
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
  
```  
kubectl delete pods new-replica-set-2r2rv new-replica-set-hgbgm new-replica-set-lpvsm new-replica-set-pbrlq
```



```
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: replicaset-1
spec:
  replicas: 2
  selector:
    matchLabels:
      tier: frontend
  template:
    metadata:
      labels:
        tier: frontend
    spec:
      containers:
      - name: nginx
        image: nginx
```        
```        
kubectl delete rs replicaset-1 replicaset-2 


replicaset.apps "replicaset-1" deleted
replicaset.apps "replicaset-2" deleted        
```

```
kubectl set image rs new-replica-set busybox-container=busybox  

NOTE : After updating the rs image, one needs to delete the pods to get the pods recreated with new image  
```

```
kubectl scale rs new-replica-set --replicas=5
```

```
kubectl edit replicaset new-replica-set 
```


### Difference between ReplicaSet and Deployment

Purpose and Functionality: ReplicaSet ensures a specified number of pod replicas are running at any given time
Deployment manages ReplicaSets and provides declarative updates to applications, along with additional features for managing application lifecycle

Update Strategy: ReplicaSet doesn't handle updates to pod templates - if you want to update the pod template, you need to create a new ReplicaSet
Deployment automatically handles updates by creating new ReplicaSets and gradually transitioning pods from old to new versions (rolling updates)

Version History: ReplicaSet maintains no history of previous versions
Deployment maintains a revision history and allows easy rollback to previous versions


#### ReplicaSet example
```
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: frontend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: php-redis
        image: gcr.io/google_samples/gb-frontend:v1
```        
        
#### Deployment example
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: php-redis
        image: gcr.io/google_samples/gb-frontend:v1
        
       
# LAB Practice Test - Deployments
 
``` 
kubectl get pods
```

```
kubectl get rs
```

```
kubectl get deploy
```

```
kubectl create deployment httpd-frontend --image httpd:2.4-alpine --replicas 3
```


# LAB Practice Test - Docker Images

```
kubectl run redis --image=redis:alpine --labels=tier=db
```
```
kubectl expose pod redis --port=6379 --name=redis-service --type=ClusterIP
```

```
kubectl create deploy webapp --image=kodekloud/webapp-color --replicas=3
```


Create a new pod called custom-nginx using the nginx image and run it on container port 8080.

```
kubectl create ns dev-ns
kubectl create deploy redis-deploy --image=redis --replicas=2 --namespace=dev-ns
```

validation 
```
kubectl get deploy --namespace=dev-ns
kubectl get pods --namespace=dev-ns
```

Create a pod called httpd using the image httpd:alpine in the default namespace. Next, create a service of type ClusterIP by the same name (httpd). The target port for the service should be 80.

```
kubectl run httpd --image=httpd:alpine --port=8081
kubectl expose pod httpd --port=8081 --target-port=80 --type=ClusterIP --name=httpd
```


# LAB Practice Test - Commands and Arguments
```
kubectl describe pod ubuntu-sleeper 
```

``` bash
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
    Command:
      sleep
      4800
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




```yaml
apiVersion: v1
kind: Pod
metadata:
  name: vi 
  namespace: default
spec:
  containers:
  - name : ubuntu-container 
    image: ubuntu
    command:
    - "sleep"
    - "5000" 
```
NOTE : The commands should be in string array

```yaml
apiVersion: v1
kind: Pod 
metadata:
  name: ubuntu-sleeper-3
spec:
  containers:
  - name: ubuntu
    image: ubuntu
    command: ["sleep","1200"]
```
NOTE : The commands should be in string array , here is another way to represent string array

```
k edit pod ubuntu-sleeper-3
k replace --force -f /tmp/kubectl-edit-95038272.yaml
```


```Docker
FROM python:3.6-alpine
RUN pip install flask
COPY . /opt/
EXPOSE 8080
WORKDIR /opt
ENTRYPOINT ["python", "app.py"]
```

```Docker
FROM python:3.6-alpine
RUN pip install flask
COPY . /opt/
EXPOSE 8080
WORKDIR /opt
ENTRYPOINT ["python", "app.py"]
CMD ["--color", "red"]
```
```yaml
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
    command: ["python", "app.py"]
    args: ["--color", "pink"]
```


```
k run webapp-green --image=kodekloud/webapp-color -o yaml --dry-run=client > webapp-green.yaml
```

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
    args: ["--color=green"] # ["--color", "green"] even this is correct 
```


#  LAB Practice Test - ConfigMaps


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
  - env:
    - name: APP_COLOR
      value: green
	name: webapp-color
	image: kodekloud/webapp-color  
```  
NOTE TO MYSELF : check why the sequence of -env matters here 



```
k create configmap webapp-config-map --from-literal=APP_COLOR=darkblue --from-literal=APP_OTHER=disregard 
```

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: webapp-config-map
  namespace: default
data:
  APP_COLOR: darkblue
  APP_OTHER: disregard
``` 

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
  - env:
    - name: APP_COLOR
      valueFrom:
       configMapKeyRef:
         name: webapp-config-map
         key: APP_COLOR
    image: kodekloud/webapp-color
    name: webapp-color
```


# LAB Practice Test - Security Contexts

Quick Note : Security context can be set at the container level OR at the pod level 
```yaml

	spec:
		securityContext:
			runAsUser: 1000
			runAsGroup: 3000
			fsGroup: 2000
			supplementalGroups: [4000]
```

Multi pod container, with security context set at both pod and at container level. 

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-pod
spec:
  securityContext:
    runAsUser: 1001
  containers:
  -  image: ubuntu
     name: web
     command: ["sleep", "5000"]
     securityContext:
      runAsUser: 1002

  -  image: ubuntu
     name: sidecar
     command: ["sleep", "5000"]
```


Update pod ubuntu-sleeper to run as Root user and with the SYS_TIME capability.
NOTE : Default the containers are run by root 
```yaml
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
	securityContext:
	  capabilities:
	    add: ["SYS_TIME"]
```

# LAB Practice Test - Service Acccount


Describe Service Account 
```bash
k describe sa default

Name:                default
Namespace:           default
Labels:              <none>
Annotations:         <none>
Image pull secrets:  <none>
Mountable secrets:   <none>
Tokens:              <none>
Events:              <none>
```

```bash

k get serviceaccount default -o yaml

apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: "2025-01-09T00:34:17Z"
  name: default
  namespace: default
  resourceVersion: "327"
  uid: 99f5125c-4edd-4318-8858-e426754293d5
```


tokens are created here : /var/run/secrets/kubernetes.io/serviceaccount/token 


Role Binding binds a role to a service account 

```yaml
---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: read-pods
  namespace: default
subjects:
- kind: ServiceAccount
  name: dashboard-sa # Name is case sensitive
  namespace: default
roleRef:
  kind: Role #this must be Role or ClusterRole
  name: pod-reader # this must match the name of the Role or ClusterRole you wish to bind to
  apiGroup: rbac.authorization.k8s.io
---
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups:
  - ''
  resources:
  - pods
  verbs:
  - get
  - watch
  - list
```


the below command generate a token for a created service account 

```bash
kubectl create token dashboard-sa
```
service account should be 




# LAB Practice Test - Secrets

Command to get all secrets
```
kubectl get secrets
```
Command to describe a secret
```
kubectl describe secret dashboard-token
```

Imperative command to create generic secret 

```bash
kubectl create secret generic db-secret --from-literal=DB_Host=sql01 \
--from-literal=DB_User=root --from-literal=DB_Password=password123 
```

Secret generated from the above Imperative command
```
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: db-secret
data:
  DB_Host: c3FsMDE=   # automatically base64Encoded when created with imperative command
  DB_Password: cGFzc3dvcmQxMjM=
  DB_User: cm9vdA==
```

How to use secret inside a pod ?

```yaml
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
    env:
    - name: DB_User
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: DB_User
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

Alternative solution : While both implementations will work when properly formatted, Implementation 2 is recommended because:

1. It's more maintainable
2. Less prone to syntax errors
3. Automatically includes all keys from the secret
4. Requires less code
5. Easier to update when new secret keys are added

```yaml
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
    envFrom:
    - secretRef:
        name: db-secret
```




# LAB Practice Test - Resource Requirements


### Quick notes 



```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: cpu-resource-constraint
spec:
  limits:
  - default: # this section defines default limits
      cpu: 500m
    defaultRequest: # this section defines default requests
      cpu: 500m
    max: # max and min define the limit range
      cpu: "1"
    min:
      cpu: 100m
    type: Container
```
fileName : cpu-constraints-pod.yaml

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: memory-resource-constraint
spec:
  limits:
  - default: # this section defines default limits
      memeory: 1Gi
    defaultRequest: # this section defines default requests
      memeory: 1Gi
    max: # max and min define the limit range
      memeory: 1G1i
    min:
      memeory: 500Mi
    type: Container
```
fileName : memory-constraints-pod.yaml


Applying LimitRange to a sepcific namespace 
```bash

kubectl apply -f constraint-define-yaml-fileName --namespace=<namespace-name>

Example:

kubectl create namespace constraints-cpu-example
kubectl apply -f cpu-constraints-pod.yaml --namespace=constraints-cpu-example
```


A LimitRange does not check the consistency of the default values it applies. This means that a default value for the limit that is set by LimitRange may be less than the request value specified for the container in the spec that a client submits to the API server. If that happens, the final Pod will not be schedulable.

then that Pod will not be scheduled, failing with an error similar to:

```bash
Pod "example-conflict-with-limitrange-cpu" is invalid: spec.containers[0].resources.requests: Invalid value: "700m": must be less than or equal to cpu limit
```




# LAB Practice Test - Taints and Toleration

Taints and Tolerations :

Node affinity is a property of Pods that attracts them to a set of nodes (either as a preference or a hard requirement). Taints are the opposite -- they allow a node to repel a set of pods.

Taints and tolerations work together to ensure that pods are not scheduled onto inappropriate nodes. One or more taints are applied to a node; this marks that the node should not accept any pods that do not tolerate the taints.

to apply taint 
```bash
kubectl taint nodes node1 key1=value1:NoSchedule
```
to remove taint 
```bash
kubectl taint nodes node1 key1=value1:NoSchedule-
```

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
  tolerations:
    - key : "spray"
      operator : "Equal"
      value: "mortein"
      effect : NoSchedule

```



```
k get nodes --all-namespaces
```
```
kubectl get service 
```

```
kubectl taint nodes node01 spray=mortein:NoSchedule
```

```
k run mosquito --image=nginx
```

```bash 
Events:
  Type     Reason            Age   From               Message
  ----     ------            ----  ----               -------
  Warning  FailedScheduling  56s   default-scheduler  0/2 nodes are available: 1 node(s) had untolerated taint {node-role.kubernetes.io/control-plane: }, 1 node(s) had untolerated taint {spray: mortein}. preemption: 0/2 nodes are available: 2 Preemption is not helpful for scheduling.
```  




# LAB Practice Test - Node Affinity
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd            
  containers:
  - name: nginx
    image: nginx
```

Apply a label color=blue to node node01

```bash
k label node node01 color=blue
```

Create a new deployment named blue with the nginx image and 3 replicas.

```bash
k create deploy blue --image=nginx --replicas=3 -o json 
```

```yaml
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
              - key: color
                operator: In
                values:
                - blue
      containers:
      - name: blue
        image: nginx
```


```yaml
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
              - key: node-role.kubernetes.io/control-plane
                operator: Exists
      containers:
      - name: blue
        image: nginx
```

# LAB Practice Test - Multi-Container Pods

Create a multi-container pod with 2 containers.


Use the spec given below:

If the pod goes into the crashloopbackoff then add the command sleep 1000 in the lemon container.

```yaml
	
  	
```


View logs on pod 
```bash
kubectl -n elastic-stack exec -it app -- cat /log/app.log
```

```yaml
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
    volumeMounts:
    - mountPath: /log
      name: log-volume

  - name: sidecar
    image: kodekloud/filebeat-configured
    volumeMounts:
    - mountPath: /var/log/event-simulator/
      name: log-volume

  volumes:
  - name: log-volume
    hostPath:
      # directory location on host
      path: /var/log/webapp
      # this field is optional
      type: DirectoryOrCreate
```



# LAB Practice Test – Init Containers


```yaml
apiVersion: v1
kind: Pod
metadata:
  name: red
  namespace: default
spec:
  initContainers:
  - image : busybox
    name : busybox
    command: ["sleep","20"]

  containers:
  - command:
    - sh
    - -c
    - echo The app is running! && sleep 3600
    image: busybox:1.28
    imagePullPolicy: IfNotPresent
    name: red-container
```



# LAB Practice Test - Readiness and Liveness Probes

```yaml

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
```



```yaml
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
--
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

```
kubectl expose pod simple-webapp-1 --port=8080 --name=webapp-service-1 --type=LoadBalancer
kubectl expose pod simple-webapp-1 --port=8080 --name=webapp-service-1 --type=LoadBalancer
```



# LAB Practice Test - Container Logging

```
kubectl logs <pod-name>
```

```
kubectl logs <pod-name> | grep 'serach string'
```

```
kubectl logs -f <pod-name>
```


# LAB Practice Test - Monitoring


Deploying Metrics Server 

```yaml 
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

```bash
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




Get Node Metrics 
```
kubectl top node
```
```
NAME           CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
controlplane   282m         1%     907Mi           1%        
node01         27m          0%     185Mi           0%   
```

```
kubectl top pod
```

```
NAME       CPU(cores)   MEMORY(bytes)   
elephant   21m          30Mi            
lion       1m           16Mi            
rabbit     147m         250Mi     
```

# LAB Practice Test - Labels, Selectors and Annotations

Command to get all the pods with label env=dev.

```
kubectl get pods -l env=dev
```

Command to get all the pods with label env=prod.
```
kubectl get all -l env=prod
```

Command to get all the pods with label [env=prod,bu=finance,tier=frontend] mutiple labels.

```
kubectl get pod -l env=prod,bu=finance,tier=frontend
```

ReplicaSet defination , replica-set pod teamplate label should match with match ith slector label.

```json 
apiVersion: apps/v1
kind: ReplicaSet
metadata:
   name: replicaset-1
spec:
   replicas: 2
   selector:
      matchLabels:
        tier: front-end
   template:
     metadata:
       labels:
        tier: front-end
     spec:
       containers:
       - name: nginx
         image: nginx
```



# LAB Practice Test - Rolling Updates & Rollbacks

```
kubectl set image deployment/frontend simple-webapp=kodekloud/webapp-color:v2 --record=true 
```
NOTE : record flag is getting deplicated 

```
kubectl rollout status deployment/frontend
```

```
kubectl rollout history deployment/frontend
```

```
kubectl describe deployment frontend
```

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
  ----    ------             ----   ----                   -------
  Normal  ScalingReplicaSet  10m    deployment-controller  Scaled up replica set frontend-6765b99794 from 0 to 4
  Normal  ScalingReplicaSet  3m17s  deployment-controller  Scaled up replica set frontend-854b57fbbf from 0 to 1
  Normal  ScalingReplicaSet  3m17s  deployment-controller  Scaled down replica set frontend-6765b99794 from 4 to 3
  Normal  ScalingReplicaSet  3m17s  deployment-controller  Scaled up replica set frontend-854b57fbbf from 1 to 2
  Normal  ScalingReplicaSet  2m56s  deployment-controller  Scaled down replica set frontend-6765b99794 from 3 to 1
  Normal  ScalingReplicaSet  2m56s  deployment-controller  Scaled up replica set frontend-854b57fbbf from 2 to 4
  Normal  ScalingReplicaSet  2m34s  deployment-controller  Scaled down replica set frontend-6765b99794 from 1 to 0
```

Note : 
StrategyType = RollingUpdate | Replicas=**4(total)** | **4(desired)**
RollingUpdateStrategy= 25% max unavailable | 25% max surge (**25% of 4 i.e 1 pod**)

```
kubectl set image deployment/frontend simple-webapp=kodekloud/webapp-color:v3
```


# LAB Practice Test - Deployment strategies

```
kubectl get service -o wide
NAME               TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE     SELECTOR
frontend-service   NodePort    172.20.154.102   <none>        8080:30080/TCP   78s     app=frontend
kubernetes         ClusterIP   172.20.0.1       <none>        443/TCP          8m57s   <none>
```

**Blue-Green Deployment Strategy**



** Canary  Deployment Strategy**

Have service to send request to both deployment , once the new deployment is tested successfully scale out the deployment and scale down the old deploument.


Scale down 
```
kubectl scale --current-replicas=5 --replicas=4 deployment/frontend
kubectl scale --current-replicas=2 --replicas=1 deployment/frontend-v2
```

```
kubectl get deploy
NAME          READY   UP-TO-DATE   AVAILABLE   AGE
frontend      4/4     4            4           10m
frontend-v2   1/1     1            1           8m7s
```

```
controlplane ~ ➜  k get deploy
NAME          READY   UP-TO-DATE   AVAILABLE   AGE
frontend      0/0     0            0           12m
frontend-v2   5/5     5            5           10m
```

# LAB Practice Test - Jobs & CronJobs
Job 

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: throw-dice-job
spec:
  completions: 1     # exits when 1 container is sucessful 
  template:
    spec:
      containers:
      - name: throw-dice-job
        image: kodekloud/throw-dice
      restartPolicy: Never
```  

Job Defination 

```yaml  
apiVersion: batch/v1
kind: Job
metadata:
  name: throw-dice-job
spec:
  completions: 2   # exits when 2 container is sucessful 
  template:
    spec:
      containers:
      - name: throw-dice-job
        image: kodekloud/throw-dice
      restartPolicy: Never
```  
	  
Job Defination  - 3
	  
```yaml 
apiVersion: batch/v1
kind: Job
metadata:
  name: throw-dice-job
spec:
  completions: 3       # exits when 3 container is sucessful 
  parallelism: 3       # runs 3 container in parallel  
  template:
    spec:
      containers:
      - name: throw-dice-job
        image: kodekloud/throw-dice
      restartPolicy: Never


```  

Command to force recreate the jobs from a file 

```bash

k replace --force -f throw-dice-job.yaml

```


CronJob - job that gets trigger in specific time

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: throw-dice-cron-job
spec:
  schedule: "30 21 * * *"
  jobTemplate:
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


# LAB Practice Test - Services

Create base service defination using Imperative Command Reference

Cluster IP Service are not exposed to the outside world.
Loadbalancer Services are exposed to the outside world. 
Node port 


```
kubectl create service nodeport webapp-service --tcp=8080:30080 --node-port=30080 -o yaml > service-definition-2.yaml
```

edit service-definition-2.yaml
```yaml 
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: "2025-01-08T03:46:05Z"
  labels:
    app: webapp-service
  name: webapp-service
  namespace: default
spec:
  type: NodePort
  ports:
  - name: webapp-service-port
    nodePort: 30080
    port: 8080
    targetPort: 8080
  selector:
    name : simple-webapp
```  



# LAB Practice Test - Ingress Networking - 1

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
  status:
    loadBalancer:
      ingress:
      - ip: 172.20.71.208
kind: List
metadata:
  resourceVersion: ""
```


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
        - backend:
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
critical-space/Pay App

```
apiVersion: v1
kind: List
items:
- apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    annotations:
      nginx.ingress.kubernetes.io/rewrite-target: /
      nginx.ingress.kubernetes.io/ssl-redirect: "false"
    name: critical-ingress
    namespace: critical-space
  spec:
    rules:
    - http:
        paths:
        - backend:
            service:
              name: pay-service
              port:
                number: 8282
          path: /pay
          pathType: Prefix
```

```bash
kubctl create ingress ingress-pay -n critical-space --rule="/pay=pay-service:8282"
```


Without the rewrite-target option, this is what would happen:

http://<ingress-service>:<ingress-port>/watch --> http://<watch-service>:<port>/watch

http://<ingress-service>:<ingress-port>/wear --> http://<wear-service>:<port>/wear

To fix that we want to "ReWrite" the URL when the request is passed on to the watch or wear applications. 

annotations:
      nginx.ingress.kubernetes.io/rewrite-target: /  # this will rewrite the backend URL and remove the /pay when forwarding the request.
	  
With the rewrite-target

http://<ingress-service>:<ingress-port>/watch --> http://<watch-service>:<port>
http://<ingress-service>:<ingress-port>/pay --> http://<pay-service>:<port>
	  
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
piVersion: apps/v1
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
        - --default-backend-service=app-space/default-http-backend
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
    nodePort: 30080
  selector:
    app.kubernetes.io/component: controller
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/name: ingress-nginx
  type: NodePort
                                                                                                                  142,1         Bot
```

```bash
k create ingress ingress-wear-watch -n app-space --rule="/wear=wear-service:8080" --rule="/watch=video-service:8080"
```


# LAB Practice Test - Network Policies

k get networkpolicy -A


kubectl get pods -l key=value

```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: internal-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      name: internal
  policyTypes:
  - Egress
  egress:
  - to:
    - podSelector:
        matchLabels:
          name: mysql
    ports:
    - port: 3306
      protocol: TCP
  - to:
    - podSelector:
        matchLabels:
          name: payroll
    ports:
    - port: 8080
      protocol: TCP
  - ports:
     - port: 53
       protocol: UDP
     - port: 53
       protocol: TCP
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
  

# LAB Practice Test - Persistent Volumes
  
kubectl exec webapp -- cat /log/app.log


```
apiVersion: v1
kind: Pod
metadata:
  name: webapp
spec:
  containers:
    - name: webapp
      image: kodekloud/event-simulator
      volumeMounts:
        - name: vol-1
          mountPath: /log
  volumes:
    - name: vol-1
      hostPath:
        path: /var/log/webapp
			
```			

```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-log
spec:
  capacity:
    storage: 100Mi
  accessModes:
    - ReadWriteMany
  volumeMode: Filesystem
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: /pv/log
```

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: claim-log-1
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 50Mi
```

```
apiVersion: v1
kind: Pod
metadata:
  name: webapp
spec:
  containers:
  - name: webapp
    image: kodekloud/event-simulator
	volumeMounts:
	 - mountPath: /usr
	   name : pv-storage
  volumes:
    - name: pv-storage
      persistentVolumeClaim:
        claimName: claim-log-1
	
	
```


# LAB Practice Test - Storage Class


```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-pvc
spec:
  storageClassName : local-storage
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
```

NOTE : The Storage Class called local-storage makes use of VolumeBindingMode set to WaitForFirstConsumer. This will delay the binding and provisioning of a PersistentVolume until a Pod using the PersistentVolumeClaim is created.

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx 
spec:
  containers:
  - name: nginx 
    image: nginx:alpine
	volumeMounts:
	 - mountPath: /var/www/html
	   name : pv-storage
  volumes:
    - name: pv-storage
      persistentVolumeClaim:
        claimName: local-pvc
```

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: low-latency
  annotations:
    storageclass.kubernetes.io/is-default-class: "false"
provisioner: kubernetes.io/no-provisioner
reclaimPolicy: Retain # default value is Delete
allowVolumeExpansion: true
mountOptions:
  - discard # this might enable UNMAP / TRIM at the block storage layer
volumeBindingMode: WaitForFirstConsumer
parameters:
  guaranteedReadWriteLatency: "true" # provider-specific
```


# LAB Practice Test - KubeConfig

 vi /root/.kube/config
 
 kubectl config --kubeconfig=/root/my-kube-config use-context research
 
 
vi ~/.bashrc
alias k=kubectl


 kubectl get pods --client-certificate=/etc/kubernetes/pki/users/dev-user/dev-user.crt --client-key=/etc/kubernetes/pki/users/dev-user/dev-user.key --certificate-authority=/etc/kubernetes/pki/users/dev-user/dev-user.csr
 
 kubectl config --kubeconfig=/root/.kube/config
 
 kubectl config set-credentials dev-user \
  --client-certificate=/etc/kubernetes/pki/users/dev-user/dev-user.csr \
  --client-key=/etc/kubernetes/pki/users/dev-user/dev-user.key \
  --kubeconfig=/root/.kube/config
  
  k config view --kubeconfig=/root/.kube/config
  
  
# LAB Practice Test Role Based Access Controls

ps aux | grep kube-apiserver



kubectl create role developer --verb=list --verb=create --verb=delete --resource=pods
kubectl create rolebinding dev-user-binding --role=developer --user=dev-user


k auth can-i --as dev-user pod describe -n blue


controlplane ~ ✦ ✖ k describe role developer -n blue
Name:         developer
Labels:       <none>
Annotations:  <none>
PolicyRule:
  Resources  Non-Resource URLs  Resource Names  Verbs
  ---------  -----------------  --------------  -----
  pods       []                 [blue-app]      [get watch create delete]

k replace --force -f developer-role.yaml 


controlplane ~ ✦ ➜  k describe role developer -n blue
Name:         developer
Labels:       <none>
Annotations:  <none>
PolicyRule:
  Resources  Non-Resource URLs  Resource Names   Verbs
  ---------  -----------------  --------------   -----
  pods       []                 [dark-blue-app]  [get watch create delete]
  
  
  
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
  - ""
  resourceNames:
  - dark-blue-app
  resources:
  - pods
  verbs:
  - get
  - watch
  - create
  - delete
- apiGroups:
  - "apps"
  resources:
  - deployments
  verbs:
  - create
  - list
"developer




```

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: NodeAccessClusterRoles
rules:
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["*"]
```

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: NodeAccessClusterRoles-michelle
subjects:
- kind: User
  name: michelle
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: NodeAccessClusterRoles
  apiGroup: rbac.authorization.k8s.io
```

This is requried for getting the api groupName of any Resource
```
kubectl api-resources

controlplane ~ ➜  kubectl api-resources | grep storage 
csidrivers                                       storage.k8s.io/v1                 false        CSIDriver
csinodes                                         storage.k8s.io/v1                 false        CSINode
csistoragecapacities                             storage.k8s.io/v1                 true         CSIStorageCapacity
storageclasses                      sc           storage.k8s.io/v1                 false        StorageClass
volumeattachments                                storage.k8s.io/v1                 false        VolumeAttachment
persistentvolumes                   pv           v1                                false        PersistentVolume
```



```

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: storage-admin
rules:
- apiGroups: [""]
  resources: ["persistentvolumes"]
  verbs: ["*"]
- apiGroups: ["storage.k8s.io"]
  resources: ["storageclasses"]
  verbs: ["*"]
  
```

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

kubectl auth can-i get pv

kubectl auth can-i get sc

cat /etc/kubernetes/manifests/kube-apiserver.yaml | grep admission

ps -ef | grep kube-apiserver | grep admission-plugins

kubectl get pods -n kube-system






ps -ef | grep kube-apiserver | grep mutating 


kubectl create secret tls webhook-server-tls --cert=/root/keys/webhook-server-tls.crt --key=/root/keys/webhook-server-tls.key -n webhook-demo


kubectl api-resources | grep storage 


kubectl convert -f ingress-old.yaml --local -o json > ingress-new.yaml