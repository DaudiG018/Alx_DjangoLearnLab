import datetime
from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

# The BookSerializer serializes all fields of the Book model and validates that the publication year is not in the future.
# The AuthorSerializer serializes the Author model and includes a nested BookSerializer to dynamically include related books.
