from django.urls import path
from . import views

urlpatterns = [
    path('book-list/', views.book_list, name='book_list'),  # Map to the book_list view
    path('books/', views.books, name='books'),  # Map to the books view
]