# relationship_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # URL for function-based view to list all books
    path('books/', views.book_list, name='book_list'),

    # URL for class-based view to display a library's details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]