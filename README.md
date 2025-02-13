### Deploy to Kubernetes
---
```
kubectl apply -f k8s/apps/mysql-master-deployment.yaml
kubectl apply -f k8s/apps/celery-worker-deployment.yaml
kubectl apply -f k8s/apps/celery-beat-deployment.yaml
kubectl apply -f k8s/apps/rabbitmq-deployment.yaml
kubectl apply -f k8s/apps/lottery.yaml
kubectl apply -f k8s/apps/nginx-deployment.yaml
```

### Combine IAM service-account to kubernetes service-account
- Enable Workload Identity on your GKE cluster
```
gcloud container clusters update YOUR_CLUSTER_NAME \
  --workload-pool=YOUR_PROJECT_ID.svc.id.goog
```
- Create an IAM service account
```
gcloud iam service-accounts create ann-service \
  --display-name "Ann Service Account"
```
- Grant it the necessary roles, e.g., roles/secretmanager.secretAccessor:
```
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
  --member="serviceAccount:ann-service@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```
- Create a GKE service account
```
kubectl create serviceaccount ann-service
```
- Bind the IAM service account to the Kubernetes service account
```
gcloud iam service-accounts add-iam-policy-binding ann-service@YOUR_PROJECT_ID.iam.gserviceaccount.com \
  --member="serviceAccount:YOUR_PROJECT_ID.svc.id.goog[default/ann-service-account]" \
  --role="roles/iam.workloadIdentityUser"
```
- Modify the deployment to use the Kubernetes service account
```
serviceAccountName: ann-service
```

### CI/CD
---
* GitHub
* Cloud Build
    * deploy main django app to gke each time push

### Asynchronous Tasks
---
* Celery
    * Start Celery Worker
    ```
        celery -A lottery worker -Q lonquery_pq --loglevel=info
    ```
    * Start Celery Beat
    ```
        celery -A lottery beat --loglevel=info
    ```
* RabbitMQ
