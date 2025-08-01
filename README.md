
# 1. Project Overview - Book Catalog API

This is a Django-based Book Catalog API that allows users to manage books with operations such as listing, adding, updating, and deleting book entries. The project is containerized with Docker, supports automated deployment via a CI/CD pipeline using GitHub Actions, and is deployed to Kubernetes using Helm charts.

# 2. API Endpoints

- **GET** `/api/books/` - List all books
- **POST** `/api/books/` - Add a new book
- **PUT** `/api/books/<id>/` - Update a book by ID
- **DELETE** `/api/books/<id>/` - Delete a book by ID

#### POST (Sample): 

```bash
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "description": "This is a test",
  "isbn": "1234567890123",
  "published_date": "2021-09-15"
}
```
# 3. Local Build and Run Instructions

#### Prerequisites
- Python 3.10+
- Docker & Docker Compose
- PostgreSQL

#### Run Locally with Docker Compose
```bash
docker-compose up --build

# Docker Build (Manual)
docker build -t book-catalog-api:latest .
docker run -p 8000:8000 book-catalog-api:latest
 # Environment variables are defined in docker-compose.yml

```
The app will be available at http://localhost:8000/

# 4. CI/CD Pipeline (GitHub Actions)

A CI/CD workflow is configured to:
- Install dependencies
- Run tests and check for migrations
- Build and push Docker images to GitHub Container Registry
- Deploy the app to a Kubernetes cluster using Helm

Trigger: Workflow runs on every push to the `main` branch.

# 5. Kubernetes and Helm Setup

#### Helm Chart Includes:
- `deployment.yaml`
- `service.yaml`
- `ingress.yaml`
- `values.yaml`
- `configmap.yaml`

### Deploy to Kubernetes:

```bash
helm install book-catalog ./k8s/helm-chart
```

#### View Services and Pods:
```bash
kubectl get svc
kubectl get pods
kubectl get ingress
```

## Semantic Release

This project supports semantic versioning using Git tags (e.g. `v1.0.0`). When a release is tagged, the GitHub Actions workflow builds a versioned Docker image and pushes it to GHCR.

# 6. Git Version Control

- Git is used for source control
- All code is hosted in [GitHub Repo](https://github.com/research-selvi-datascience/diploma_devops_2025)



