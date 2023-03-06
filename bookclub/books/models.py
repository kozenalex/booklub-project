from django.db import models

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
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
