from django.urls import path
from . import views

urlpatterns = [
    # URL for adding a book
    path('add_book/', views.add_book, name='add_book'),

    # URL for editing a book (requires book_id as a parameter)
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),

    # URL for deleting a book (requires book_id as a parameter)
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

    # Other URL patterns for listing books, library views, etc.
    path('books/', views.book_list, name='book_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('libraries/', views.LibraryListView.as_view(), name='library_list'),  # Optional ListView for all libraries
]