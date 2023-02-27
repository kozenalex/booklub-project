from django.db import models

class Book(models.Model):

    title = models.CharField(max_length=255)
    img = models.ImageField(
        upload_to='books/%Y-%m-%d/',
        blank=True,
        height_field=None,
        width_field=None,
        max_length=100
    )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
