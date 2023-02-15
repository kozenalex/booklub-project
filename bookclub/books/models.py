from django.db import models

class Book(models.Model):

    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='static/', blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
