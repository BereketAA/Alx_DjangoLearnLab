ersion of your query_samples.py script with the missing filter query:

python
Copy code
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# Import models
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    # Get the author object based on the author's name
    author = Author.objects.get(name=author_name)
    
    # Use filter to get all books written by the author
    books = Book.objects.filter(author=author)
    
    # Print out the books
    for book in books:
        print(book.title)

# Example call to the function (replace 'Author Name' with an actual author's name)
get_books_by_author('Author Name')