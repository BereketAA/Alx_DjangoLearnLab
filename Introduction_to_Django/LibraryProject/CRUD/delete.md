# Delete the Book Instance

This command deletes the book instance and confirms the deletion by retrieving all books.

```python
from bookshelf.models import Book
# Assuming the book instance was created previously
# Create a book instance first (if not already created)
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Deleting the book instance
book.delete()  # This deletes the book instance

# Confirming deletion by attempting to retrieve all books
Book.objects.all()
# Output: <QuerySet []>  # This indicates that no books exist