# relationship_app/urls.py

from django.urls import path
from . import views  # Import all views from views.py

urlpatterns = [
    # URL for function-based view to list all books
    path('books/', views.list_books, name='book_list'),  # Function-based view for books list

    # URL for class-based view to display a library's details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details

    # Optional ListView for all libraries (if you want to list all libraries)
    path('libraries/', views.LibraryListView.as_view(), name='library_list'),  # Optional ListView for all libraries
]