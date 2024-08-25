from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
    
    
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


