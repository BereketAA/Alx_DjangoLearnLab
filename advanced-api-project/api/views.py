from django.shortcuts import render


from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookListView(ListAPIView):
    """List all books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
     # Add filter backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Define filtering options
    filterset_fields = ['author__name', 'publication_year', 'title']

    # Define search fields
    search_fields = ['title', 'author__name']

    # Define ordering fields
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']

class BookDetailView(RetrieveAPIView):
    """Retrieve a single book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(CreateAPIView):
    """Create a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(UpdateAPIView):
    """Update an existing book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(DestroyAPIView):
    """Delete a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]




from rest_framework.exceptions import ValidationError

class BookCreateView(generics.CreateAPIView):
    """Customized Create View with validation."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        publication_year = serializer.validated_data['publication_year']
        if publication_year > 3000:
            raise ValidationError("Invalid publication year.")
        serializer.save()
 
 
 
 
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class BookListView(generics.ListAPIView):
    """List View with read-only permissions for unauthenticated users."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]