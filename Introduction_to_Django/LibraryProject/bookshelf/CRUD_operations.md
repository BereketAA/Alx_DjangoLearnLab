### Consolidated Documentation File (`CRUD_operations.md`)

You can also create a consolidated file that includes all commands and expected outputs in one place. Here’s how you can format it:

**Documentation in `CRUD_operations.md`**:
```markdown
# CRUD Operations for Book Model

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>

Book.objects.get(id=book.id)
# Output: <Book: 1984 by George Orwell (1949)>

book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(id=book.id)
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

book.delete()
Book.objects.all()
# Output: <QuerySet []>