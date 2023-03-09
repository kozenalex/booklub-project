from django.db import models
from users.models import MyUser
from books.models import Book

class Article(models.Model):

    text = models.TextField(verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(MyUser, on_delete=models.PROTECT, null=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, null=True, default=None)

    def __str__(self) -> str:
        return f'Отзыв на книгу {self.book}'
