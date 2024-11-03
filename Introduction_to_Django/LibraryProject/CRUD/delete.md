# Delete the Book Instance
# Delete the Book Instance

This command deletes the book instance and confirms the deletion by retrieving all books.

```python

from bookshelf.models import Book  # Importing the Book model

# Assuming the book instance was created previously
book.delete()  # Deleting the book instance

# Confirming deletion by retrieving all books
Book.objects.all()
# Output: <QuerySet []>