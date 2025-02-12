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
