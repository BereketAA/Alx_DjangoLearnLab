# Update the Book Title

This command updates the title of the book to "Nineteen Eighty-Four".

```python
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(id=book.id)
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>