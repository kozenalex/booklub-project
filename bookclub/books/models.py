from django.db import models
from django.db.models import Avg
import requests
import json

from users.models import MyUser

class Book(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название книги')
    img = models.ImageField(
        upload_to='books/%Y-%m-%d/',
        blank=True,
        height_field=None,
        width_field=None,
        max_length=100,
        verbose_name='Обложка'
    )
    author = models.CharField(max_length=255, blank=True, verbose_name='Автор')
    google_img = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_google_thumbnail(self):
        if not self.google_img:
            response = requests.get(
                            url='https://www.googleapis.com/books/v1/volumes',
                            params={
                                'q': self.title + '+' + self.author,
                                'printType': 'books',
                                'projection':'lite'
                            })
            r_j = json.loads(response.text)
            thumbs = [
                x['volumeInfo']['imageLinks']['thumbnail'] for \
                    x in r_j['items'] if x['volumeInfo'].get('imageLinks')
            ]
            self.google_img = thumbs[0] if thumbs else None
            self.save()
        return self.google_img

    @property
    def get_raiting(self):

        avg_r = BookRaiting.objects.filter(book=self).aggregate(Avg('raiting'))
        num = avg_r['raiting__avg'] if avg_r else 0
        if num:
            return int(
                num + (0.5 if num > 0 else -0.5)
            )
        else:
            return 0
    
    @property
    def get_yellow_stars(self):
        return range(self.get_raiting)

    @property
    def get_blank_stars(self):
        return range(5 - self.get_raiting)      

    def __str__(self) -> str:
        return self.title

class BookRaiting(models.Model):

    RAITING_CHOICES = tuple(
        zip(
            range(0, 6), range(0, 6)
        )
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    raiting = models.IntegerField(choices=RAITING_CHOICES)

    def __str__(self):
        return f'Оценка книги {self.book} от {self.user}'