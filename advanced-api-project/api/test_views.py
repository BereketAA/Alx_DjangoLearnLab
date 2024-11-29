from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author
from rest_framework.permissions import IsAuthenticated


class BookTests(APITestCase):
    def setUp(self):
        # Create an author
        self.author = Author.objects.create(name="Test Author")
        
        # Create a Book instance
        self.book = Book.objects.create(
            title="Test Book", 
            publication_year=2020, 
            author=self.author
        )
        
        # Set URL paths
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', args=[self.book.id])

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('id').title, 'New Book')

    def test_read_book(self):
        response = self.client.get(self.book_detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)
        self.assertEqual(response.data['publication_year'], self.book.publication_year)

    def test_update_book(self):
        data = {
            'title': 'Updated Book',
            'publication_year': 2025,
            'author': self.author.id
        }
        response = self.client.put(self.book_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()  # Refresh the Book instance from DB
        self.assertEqual(self.book.title, 'Updated Book')
        self.assertEqual(self.book.publication_year, 2025)

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)






class BookSearchFilterOrderingTests(APITestCase):
    def setUp(self):
        # Setup for tests
        self.author1 = Author.objects.create(name="Author 1")
        self.author2 = Author.objects.create(name="Author 2")
        self.book1 = Book.objects.create(title="Book A", publication_year=2020, author=self.author1)
        self.book2 = Book.objects.create(title="Book B", publication_year=2021, author=self.author2)

        # URL for listing books
        self.book_list_url = reverse('book-list')

    def test_filter_by_author(self):
        response = self.client.get(self.book_list_url, {'author': self.author1.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book by Author 1

    def test_search_by_title(self):
        response = self.client.get(self.book_list_url, {'search': 'Book A'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only "Book A"

    def test_order_by_title(self):
        response = self.client.get(self.book_list_url, {'ordering': 'title'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, ['Book A', 'Book B'])

    def test_order_by_publication_year_desc(self):
        response = self.client.get(self.book_list_url, {'ordering': '-publication_year'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, [2021, 2020])  # Order by descending year





class BookPermissionsTests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(title="Test Book", publication_year=2020, author=self.author)
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', args=[self.book.id])

    def test_create_book_permission(self):
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Unauthenticated user

    def test_authenticated_user_create_book(self):
        self.client.login(username='testuser', password='password')  # Login with test user
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Authenticated user can create book