from django.db import models
from users.models import User
from books.models import Book

class Article(models.Model):

    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, null=True, default=None)
