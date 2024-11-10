from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book

from django.views.generic import DetailView
from .models import Library

# relationship_app/views.py

# Function-based view to list all books and their authors
def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'relationship_app/list_books.html', context)  # Use the correct template path


# Class-based view to display details of a specific library
class LibraryListView(ListView):
    model = Library
    template_name = 'relationship_app/library_list.html'  # Template for listing libraries
    context_object_name = 'libraries'  # The context name in the template

