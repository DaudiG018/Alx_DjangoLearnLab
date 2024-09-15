from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        
        # Create some books for testing
        self.book1 = Book.objects.create(title='Book One', author='Author One', publication_year=2021)
        self.book2 = Book.objects.create(title='Book Two', author='Author Two', publication_year=2022)
        self.book_url = reverse('book-list')
    
    def test_create_book(self):
        url = self.book_url
        data = {'title': 'Book Three', 'author': 'Author Three', 'publication_year': 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.latest('id').title, 'Book Three')

    def test_list_books(self):
        url = self.book_url
        response = self.client.get(url)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        serializer = BookSerializer(self.book1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_update_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        data = {'title': 'Updated Book One', 'author': 'Updated Author One', 'publication_year': 2024}
        response = self.client.put(url, data, format='json')
        self.book1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.book1.title, 'Updated Book One')
    
    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
    
    def test_filter_books(self):
        url = f"{self.book_url}?title=Book Two"
        response = self.client.get(url)
        serializer = BookSerializer([self.book2], many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_search_books(self):
        url = f"{self.book_url}?search=Author One"
        response = self.client.get(url)
        serializer = BookSerializer([self.book1], many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_order_books(self):
        url = f"{self.book_url}?ordering=publication_year"
        response = self.client.get(url)
        serializer = BookSerializer([self.book1, self.book2], many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_unauthorized_access(self):
        self.client.logout()
        url = self.book_url
        response = self.client.post(url, {'title': 'Unauthorized Book'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

