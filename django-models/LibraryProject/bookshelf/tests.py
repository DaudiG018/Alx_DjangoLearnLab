from django.test import TestCase

# Create your tests here.from bookshelf.models import Book
from bookshelf.models import Book
# Create a new book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()


# Retrieve the book instance
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)


# Update the book title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(updated_book.title)


# Delete the book instance
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)
