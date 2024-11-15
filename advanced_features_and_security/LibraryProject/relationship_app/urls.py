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

# relationship_app/urls.py

from django.urls import path
from . import views  # Import all views from views.py
from .views import list_books, LibraryDetailView

urlpatterns = [
    # URL for function-based view to list all books
    path('books/', views.list_books, name='book_list'),  # Function-based view for books list

    # URL for class-based view to display a library's details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details

    # Optional ListView for all libraries (if you want to list all libraries)
    path('libraries/', views.LibraryListView.as_view(), name='library_list'),  # Optional ListView for all libraries
]

# relationship_app/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Import Django's built-in auth views

urlpatterns = [
    path('register/', views.register, name='register'),  # Custom registration view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Built-in login view
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),  # Built-in logout view
    path('logged_out/', views.logged_out, name='logged_out'),  # Optional logged-out page
    path('books/', views.book_list, name='book_list'),  # Other URL patterns...
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]