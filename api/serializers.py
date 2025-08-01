from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):


    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'isbn', 'published_date', 'created_at']
    
