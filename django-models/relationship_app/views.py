f# relationship_app/views.py

from django.shortcuts import render
from django.views.generic.detail import DetailView  # Add this import
from .models import Book, Library

# Function-based view to list all books and their authors
def book_list(request):
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
