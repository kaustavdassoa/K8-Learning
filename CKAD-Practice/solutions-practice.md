# LAB : Practice Test - Pods

```
kubectl get pods
```

```
kubectl run ngix --image=nginx 
```

```
kubectl describe pod newpods-h7b7b 
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


kubectl describe pod webapp 

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
kubectl run redis --image=redis123
```

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
```

```
NAME                    READY   STATUS             RESTARTS   AGE
new-replica-set-2r2rv   0/1     ImagePullBackOff   0          4m34s
```

```
kubectl describe pod new-replica-set-2r2rv 
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
  
  
k delete pods new-replica-set-2r2rv new-replica-set-hgbgm new-replica-set-lpvsm new-replica-set-pbrlq





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
        
        
k delete rs replicaset-1 replicaset-2 
replicaset.apps "replicaset-1" deleted
replicaset.apps "replicaset-2" deleted        



kubectl set image rs new-replica-set busybox-container=busybox  

NOTE : After updating the rs image, one needs to delete the pods to get the pods recreated with new image  




kubectl scale rs new-replica-set --replicas=5



kubectl edit replicaset new-replica-set 



### Difference between ReplicaSet and Deployment

Purpose and Functionality: ReplicaSet ensures a specified number of pod replicas are running at any given time
Deployment manages ReplicaSets and provides declarative updates to applications, along with additional features for managing application lifecycle

Update Strategy: ReplicaSet doesn't handle updates to pod templates - if you want to update the pod template, you need to create a new ReplicaSet
Deployment automatically handles updates by creating new ReplicaSets and gradually transitioning pods from old to new versions (rolling updates)

Version History: ReplicaSet maintains no history of previous versions
Deployment maintains a revision history and allows easy rollback to previous versions


#### ReplicaSet example
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
