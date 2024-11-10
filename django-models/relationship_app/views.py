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
