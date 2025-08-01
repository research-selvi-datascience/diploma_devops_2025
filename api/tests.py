from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book
from datetime import date


class BookViewTest(APITestCase):
    
    def test_response_is_correct(self):
        book = Book.objects.create(
            title="Demo",
            description="Description",
            author ="Author",
            isbn="1234567890123",
            published_date=date(2025, 7, 31)
            
        )
        url = reverse('api:books')
        response = self.client.get(url, format = 'json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        returned_book = body[0]
        assert returned_book["title"] == book.title
        assert returned_book["description"] == book.description
        assert returned_book["author"] == book.author
        assert returned_book["isbn"] == book.isbn
        assert returned_book["published_date"] == str(book.published_date)


class BookUpdateAndDeleteTest(APITestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Initial Title",
            description="Initial Description",
            author="Initial Author",
            isbn="9876543210123",
            published_date=date(2020, 1, 1)
        )
        self.detail_url = reverse('api:book-detail', args=[self.book.pk])

    def test_update_book(self):
        data = {
            "title": "Updated Title",
            "description": "Updated Description",
            "author": "Updated Author",
            "isbn": self.book.isbn,
            "published_date": str(self.book.published_date)
        }
        response = self.client.put(self.detail_url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        updated = response.json()
        assert updated["title"] == "Updated Title"
        assert updated["description"] == "Updated Description"

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        # Confirm it's deleted
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())

        
        
class HealthViewTest(APITestCase):
    
    def test_response_is_correct(self):
        url = reverse('api:health')
        response = self.client.get(url, format = 'json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body['status'] == 'ok'
        