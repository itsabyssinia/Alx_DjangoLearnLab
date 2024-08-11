from django.contrib import admin

from django.contrib import admin
from .models import Book

# Register the Book model with the Django admin interface
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

# Register your models here.
