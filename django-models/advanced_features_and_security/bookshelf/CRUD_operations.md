

## Create

Command:

```python
from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()


book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)


book.title = "Nineteen Eighty-Four"
book.save()


book.delete()

books = Book.objects.all()
print(books)


### Summary

1. **Model Creation**: Defined the `Book` model in `bookshelf/models.py`.
2. **Migration**: Created and applied migrations.
3. **CRUD Operations**: Executed create, retrieve, update, and delete operations in Django shell.
4. **Documentation**: Created Markdown files for each CRUD operation and a summary file.

You now have a fully functional Django project with a `bookshelf` app and well-documented CRUD operations.
