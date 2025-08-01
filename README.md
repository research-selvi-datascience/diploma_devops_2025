***Book Catalog API***

**Project Overview**

This is a Django-based RESTful API for managing a book catalog. It supports full CRUD operations on book records and is containerized using Docker. The application is deployed to a local Kubernetes cluster using Helm and includes a CI/CD pipeline powered by GitHub Actions.


**List All Books**
GET /api/books/

**Add a New Book**

POST /api/books/
Content-Type: application/json

{
  "title": "The Alchemist",
  "author": "Paulo Coelho",
  "isbn": "9780061122415",
  "published_date": "1988-05-01"
}

**Update a Book (PUT)**

PUT /api/books/<id>/

**Delete a Book**

DELETE /api/books/<id>/
