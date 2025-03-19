# End-to-end-Machine-Learning-Project-with-Mlflow


This repository contains an **end-to-end machine learning project** for predicting **wine quality** using MLflow for experiment tracking, Streamlit for interactive visualization, and AWS ECS/ECR for deployment.

---

 **Project Overview**
This project demonstrates the **full lifecycle of an ML model**, from data ingestion to deployment. The model predicts **wine quality** based on physicochemical attributes.

 **Tech Stack**
- **Machine Learning:** `Scikit-learn`, `ElasticNet`
- **MLOps:** `MLflow`, `DVC`
- **Deployment:** `Streamlit`, `Docker`, `AWS ECS`
- **CI/CD:** `GitHub Actions`, `AWS ECR`

## WorkFlows

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update entity
5. update configuration manager 
6. update components
7. update pipelines
8. update main.py
9. update app.py



# How to run ? 

### STEPS

Clone the repository


***bash

https://github.com/WisdomAnalyst/End-to-end-Machine-Learning-Project-with-Mlflow
...

### STEP 01- Create a conda environment after opening the repository

***bash
conda create -n mlproj python=3.8 -y
***


***bash
conda activate mlproj
***

### STEP 2 - install the requirements 
***bash
pip install -r requirements.txt
***


***bash
#finally run the following command 
python app.py


now, 
***bash
open up your local host and port


#MLflow
[Documentation](https://mlflow.org/docs/latest/index.html)



#### cmd
-mlflow ui



### dagshub
[dagshub](https;//dagshub.com/)


MLFLOW_TRACKING_USERNAME=WisdomAnalyst
MLFLOW_TRACKING_PASSWORD=781aa8b98086477f57088d72da8f137a4686f662
MLFLOW_TRACKING_URI=https://dagshub.com/WisdomAnalyst/End-to-end-Machine-Learning-Project-with-Mlflow.mlflow
python script.py


Run this to export as env variables 

***bash

export MLFLOW_TRACKING_URI=https://dagshub.com/WisdomAnalyst/End-to-end-Machine-Learning-Project-with-Mlflow.mlflow

export MLFLOW_TRACKING_USERNAME=WisdomAnalyst

export MLFLOW_TRACKING_PASSWORD=781aa8b98086477f57088d72da8f137a4686f662



## Deployment Steps

### 1. AWS Configuration
- **ECR (Elastic Container Registry)**
  ```bash
  # Repository Name: wine-quality-prediction
  # URI: 533267162979.dkr.ecr.us-east-1.amazonaws.com/wine-quality-prediction
ECS (Elastic Container Service)
# Cluster Name: wine-quality-cluster
# Task Definition: wine-quality-task
# Service Name: wine-quality-service

2. GitHub Actions CI/CD Setup
Added GitHub Secrets:
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key

3. Project Structure
End-to-end-Machine-Learning-Project-with-Mlflow/
├── .github/
│   └── workflows/
│       └── main.yaml
├── src/
│   └── Mlproject/
│       └── pipeline/
│           └── prediction.py
├── templates/
│   └── index.html
├── static/
│   └── css/
├── app.py
├── Dockerfile
├── requirements.txt
├── setup.py
└── README.md

4. Docker Configuration
# Use Python 3.8 slim-buster as base image
FROM python:3.8-slim-buster

# Update apt and install awscli
RUN apt-get update -y && apt-get install awscli -y

# Set working directory
WORKDIR /app

# Copy the entire application
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Command to run the application
CMD ["python3", "app.py"]

5. Manual Deployment Steps
# Build Docker image locally
docker build -t wine-quality-prediction .

# Login to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 533267162979.dkr.ecr.us-east-1.amazonaws.com

# Tag image
docker tag wine-quality-prediction:latest 533267162979.dkr.ecr.us-east-1.amazonaws.com/wine-quality-prediction:latest

# Push to ECR
docker push 533267162979.dkr.ecr.us-east-1.amazonaws.com/wine-quality-prediction:latest

6. GitHub Actions Workflow
name: ML Model CI/CD

on:
  push:
    branches:
      - main
    paths-ignore:
      - 'README.md'

jobs:
  deployment:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v1

      - name: Build and push Docker image
        env:
          ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
          ECR_REPOSITORY: wine-quality-prediction
          IMAGE_TAG: latest
        run: |
          docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
          docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
7. AWS ECS Configuration
Task Definition:

Family: wine-quality-task
CPU: 0.25 vCPU
Memory: 0.5 GB
Container Image: 533267162979.dkr.ecr.us-east-1.amazonaws.com/wine-quality-prediction:latest
Port Mappings: 8080
Service Configuration:

Cluster: wine-quality-cluster
Service Name: wine-quality-service
Launch Type: FARGATE
Tasks: 1

8. Monitoring
CloudWatch Logs enabled for container insights
Task definition configured with logging

9. Troubleshooting
Check CloudWatch Logs for container output
Verify ECS service events
Check Task Definition status
Monitor GitHub Actions workflow runs

10. Security
AWS credentials stored as GitHub Secrets
ECR repository policies configured
ECS task execution role permissions set
