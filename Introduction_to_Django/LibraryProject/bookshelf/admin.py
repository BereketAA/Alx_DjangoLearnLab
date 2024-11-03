from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    search_fields = ('title', 'author')  # Fields to search
    list_filter = ('publication_year',)  # Add filter by publication year

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
