apiVersion: v1
kind: Pod
metadata:
  name: nginx-apparmor
  # Note that the Pod does not need to be in the same namespace as the loader.
  labels:
    app: nginx
  annotations:
    # Tell Kubernetes to apply the AppArmor profile "k8s-nginx".
    # Note that this is ignored if the Kubernetes node is not running version 1.4 or greater.
    container.apparmor.security.beta.kubernetes.io/nginx: localhost/k8s-nginx
spec:
  containers:
  - name: nginx
    image: nginx
    ports:
    - containerPort: 80
