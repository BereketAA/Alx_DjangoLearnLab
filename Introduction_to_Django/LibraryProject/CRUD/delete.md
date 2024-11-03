# Delete the Book Instance

This command deletes the book instance and confirms the deletion by retrieving all books.

```python
from bookshelf.models import Book  # Importing the Book model

# Deleting the book instance
book.delete()

# Confirming deletion by retrieving all books
Book.objects.all()
# Output: <QuerySet []>