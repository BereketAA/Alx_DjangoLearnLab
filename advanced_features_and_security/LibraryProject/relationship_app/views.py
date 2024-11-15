from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm  # Assuming you have a BookForm for creating/editing books

# View for adding a book
@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after adding
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# View for editing a book
@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

# View for deleting a book
@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to book list after deletion
    return render(request, 'relationship_app/delete_book.html', {'book': book})
    
    
    


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



# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after successful registration
            return redirect('book_list')  # Redirect to the book list or another page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# User Login View (Django provides this built-in)
# You don't need to write a custom view for login, just use Django's built-in login URL

# User Logout View (Django provides this built-in)
# You don't need to write a custom view for logout, just use Django's built-in logout URL


from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view - Only accessible by users with Admin role
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view - Only accessible by users with Librarian role
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view - Only accessible by users with Member role
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

