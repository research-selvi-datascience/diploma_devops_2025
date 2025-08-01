1. Project Overview

# Book Catalog API

This is a Django-based Book Catalog API that allows users to manage books with operations such as listing, adding, updating, and deleting book entries. The project is containerized with Docker, supports automated deployment via a CI/CD pipeline using GitHub Actions, and is deployed to Kubernetes using Helm charts.

2. API Usage Examples

## API Endpoints

- **GET** `/api/books/` - List all books
- **POST** `/api/books/` - Add a new book
- **PUT** `/api/books/<id>/` - Update a book by ID
- **DELETE** `/api/books/<id>/` - Delete a book by ID

### Sample POST Payload
```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "description": "This is a test",
  "isbn": "1234567890123",
  "published_date": "2021-09-15"
}


---

##### **3. Local Build and Run Instructions**
```markdown
##  Local Development Setup

### Prerequisites
- Python 3.10+
- Docker & Docker Compose
- PostgreSQL

### Run Locally with Docker Compose
```bash
docker-compose up --build

The app will be available at http://localhost:8000/


---

##### **4. CI/CD Pipeline Explanation**
```markdown
## CI/CD Pipeline (GitHub Actions)

A CI/CD workflow is configured to:
- Install dependencies
- Run tests and check for migrations
- Build and push Docker images to GitHub Container Registry
- Deploy the app to a Kubernetes cluster using Helm

Trigger: Workflow runs on every push to the `main` branch.



5. Kubernetes and Helm Setup

## Kubernetes & Helm Setup

### Helm Chart Includes:
- `deployment.yaml`
- `service.yaml`
- `ingress.yaml`
- `values.yaml`
- `configmap.yaml`

### Deploy to Kubernetes:
```bash
helm install book-catalog ./k8s/helm-chart


The services and pods can be viewed using:

kubectl get svc
kubectl get pods
kubectl get ingress



---

##### **6. Optional: Git Version Control Notes**
```markdown
## Version Control

- Git is used for source control
- All code is hosted in [GitHub](https://github.com)


