# Retrieve the Book Instance

This command retrieves the book instance that was just created.

```python
Book.objects.get(id=book.id)
# Output: <Book: 1984 by George Orwell (1949)>