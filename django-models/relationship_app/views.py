from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book

from django.views.generic import DetailView
from .models import Library

# Function-based view to list all books and their authors
def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'relationship_app/list_books.html', context)  # Use the correct template path


# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

