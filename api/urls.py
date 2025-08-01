from django.urls import re_path
from django.urls import path

from .views import book_view
from .views import health_view
app_name = 'api'



urlpatterns = [
    path('health/', health_view, name='health'),                 
    path('books/', book_view, name='books'),                     # GET list, POST create
    path('books/<int:pk>/', book_view, name='book-detail'),      # PUT, DELETE, PATCH on one book
]





#urlpatterns = [
#    re_path(r"^health/", health_view, name='health'),
#    re_path(r"^books/", book_view, name='books'),
#    re_path(r"^books/<int:pk>/", book_view, name="books")]
 