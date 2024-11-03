# Delete the Book Instance

This command deletes the book instance and confirms the deletion by retrieving all books.

```python
book.delete()
Book.objects.all()
# Output: <QuerySet []>