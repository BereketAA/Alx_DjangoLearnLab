from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import generics.ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Fetch all book records
    serializer_class = BookSerializer  # Use the BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()  # Fetches all records from the Book model
    serializer_class = BookSerializer  # Uses the BookSerializer for all operations