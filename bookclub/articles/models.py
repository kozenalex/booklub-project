from django.db import models
from users.models import MyUser
from books.models import Book, BookRaiting

class Article(models.Model):

    text = models.TextField(verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(MyUser, on_delete=models.PROTECT, null=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, null=True, default=None)

    @property
    def get_author_raiting(self):
        res = BookRaiting.objects.filter(user=self.author).first()
        return res.raiting if res else 0

    def __str__(self) -> str:
        return f'Отзыв на книгу {self.book}'
