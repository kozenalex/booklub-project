from django.contrib import admin
from books.models import Book, BookRaiting

# Register your models here.
admin.site.register(Book)
admin.site.register(BookRaiting)