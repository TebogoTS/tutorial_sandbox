
---

# Python API and MySQL Database Kubernetes Application

This project demonstrates a simple setup where a Python Flask API connects to a MySQL database, both deployed as separate containers within a Kubernetes cluster. The API provides a list of people stored in the MySQL database.

## Prerequisites

Before you start, make sure you have the following installed:
- Docker
- Kubernetes
- kubectl
- Optional: MySQL client tools for testing database connectivity locally

## Project Structure

```
/project-root
|-- application
|   |-- Dockerfile
|   |-- app.py
|   |-- requirements.txt
|-- database
|   |-- Dockerfile
|   |-- schema.sql
|-- kubernetes
    |-- application-deployment.yaml
    |-- application-service.yaml
    |-- mysql-deployment.yaml
    |-- mysql-service.yaml
|-- README.md
```

## Setup Instructions

### Building Docker Images

1. **Build the Python API Container**

   Navigate to the `application` directory and build the Docker image:

   ```bash
   cd application
   docker build -t python-api:latest .
   ```

2. **Build the MySQL Database Container**

   Navigate to the `database` directory and build the Docker image:

   ```bash
   cd ../database
   docker build -t mysql-custom:latest .
   ```

### Deploying to Kubernetes

1. **Create the MySQL Deployment and Service**

   ```bash
   kubectl apply -f ../kubernetes/mysql-deployment.yaml
   kubectl apply -f ../kubernetes/mysql-service.yaml
   ```

2. **Create the Python API Deployment and Service**

   ```bash
   kubectl apply -f ../kubernetes/application-deployment.yaml
   kubectl apply -f ../kubernetes/application-service.yaml
   ```

### Accessing the Services

1. **Forward Ports to Access the API Locally**

   ```bash
   kubectl port-forward service/python-api-service 5000:5000
   ```

   Now, access the API at `http://localhost:5000/`.

2. **Forward Ports to Access the MySQL Database Locally**

   ```bash
   kubectl port-forward service/mysql-service 3306:3306
   ```

   You can now connect to MySQL at `localhost:3306` using your preferred MySQL client with the root password provided in the MySQL `Dockerfile`.

## Usage

- The API endpoint at `http://localhost:5000/` will return a JSON list of all people in the database.
- To add more people to the database, insert them directly via MySQL commands or adapt the API to accept POST requests.

## Additional Information

- Make sure to change the default passwords and user information in your production environment.
- The `kubectl port-forward` command is intended for development and testing environments only.

---

## Build and Start Services:

### Directory Structure
Ensure your directory structure looks like this:

```arduino
tutorial_sandbox/
├── application/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
├── database/
│   ├── Dockerfile
│   ├── schema.sql
├── fluent-bit.conf
└── docker-compose.yml
```

```bash
docker-compose up --build
```