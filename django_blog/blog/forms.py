from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        

from django import forms
from taggit.forms import TagField
from .models import Post

class PostForm(forms.ModelForm):
    tags = TagField(required=False)  # Add tags field

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        
        
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
        }