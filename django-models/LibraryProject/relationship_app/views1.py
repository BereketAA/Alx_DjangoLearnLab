
# Create your views here.
from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import ListView, DetailView
from django.views.generic.detail import DetailView 

# relationship_app/views.py

# Function-based view to list all books and their authors
def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'relationship_app/list_books.html', context)


# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

