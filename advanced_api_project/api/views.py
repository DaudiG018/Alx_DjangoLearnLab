from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class BookListView(generics.ListCreateAPIView):
    """
    List all books or create a new book.
    GET: Retrieve a list of all books.
    POST: Create a new book.
    """
     
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Read-only access

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific book by ID.
    GET: Retrieve a book by its ID.
    PUT/PATCH: Update a book by its ID.
    DELETE: Delete a book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    """
    List all books or create a new book.
    Supports filtering, searching, and ordering:
    - Filtering by title, author, and publication year.
    - Searching by title and author.
    - Ordering by title and publication year (default: title).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']
