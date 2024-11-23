from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps '/api/books/' to BookList view
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Retain the existing BookList view for listing books
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router-generated URLs for BookViewSet
    path('', include(router.urls)),
]
