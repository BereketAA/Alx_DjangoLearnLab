from django.shortcuts import render

# Create your views here.

from django.contrib.auth.views import LoginView, LogoutView

path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
path('logout/', LogoutView.as_view(), name='logout'),



from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})