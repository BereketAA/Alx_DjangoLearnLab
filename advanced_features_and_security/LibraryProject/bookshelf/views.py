from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"




from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Article

@permission_required('app_name.can_view', raise_exception=True)
def view_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail.html', {'article': article})

@permission_required('app_name.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)
        return redirect('article_list')
    return render(request, 'article_form.html')

@permission_required('app_name.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('article_detail', article_id=article.id)
    return render(request, 'article_form.html', {'article': article})

@permission_required('app_name.can_delete', raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'article_confirm_delete.html', {'article': article})






from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# View for displaying a list of books
@permission_required('bookshelf.can_view_book_list', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Additional view (if required)
@permission_required('bookshelf.can_view_books', raise_exception=True)
def books(request):
    return render(request, 'bookshelf/books.html')