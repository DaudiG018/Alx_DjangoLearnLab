from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for the admin interface
    list_filter = ('author', 'publication_year')
    
    # Add search capabilities
    search_fields = ('title', 'author')

    # Optional: Add ordering
    ordering = ('-publication_year',)
