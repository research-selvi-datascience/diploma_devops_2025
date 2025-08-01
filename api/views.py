from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book

class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "status": "ok",
                "running": "yes"
            }
        )

health_view = HealthView.as_view()

# Book Resource
# /api/books - All methods (GET, POST)
#


class BookView(APIView):
    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = BookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({"detail": "Method PUT requires 'pk' in URL."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({"detail": "Method DELETE requires 'pk' in URL."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"detail": "Book deleted and no record exists."}, status=status.HTTP_404_NOT_FOUND)
        
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



book_view = BookView.as_view()


