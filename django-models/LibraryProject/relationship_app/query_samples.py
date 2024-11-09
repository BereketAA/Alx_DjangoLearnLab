import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        # Retrieve the author by name
        author = Author.objects.get(name=author_name)
        
        # Query all books by this author
        books = Book.objects.filter(author=author)
        
        # Print the titles of the books
        if books.exists():
            print(f"Books by {author_name}:")
            for book in books:
                print(f"- {book.title}")
        else:
            print(f"No books found for author: {author_name}")

    except Author.DoesNotExist:
        print(f"Author named '{author_name}' does not exist in the database.")

# Example usage
get_books_by_author('Author Name')  # Replace 'Author Name' with an actual author's name
