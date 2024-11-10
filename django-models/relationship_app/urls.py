# relationship_app/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Import Django's built-in auth views

urlpatterns = [
    path('register/', views.register, name='register'),  # Custom registration view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Built-in login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Built-in logout view
    path('logged_out/', views.logged_out, name='logged_out'),  # Optional logged-out page
    path('books/', views.book_list, name='book_list'),  # Other URL patterns...
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]