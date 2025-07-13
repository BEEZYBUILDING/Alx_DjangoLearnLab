from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields shown in list view
    search_fields = ('title', 'author')                     # Enables search
    list_filter = ('publication_year',)                     # Adds a filter sidebar
