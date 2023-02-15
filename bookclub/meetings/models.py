from django.db import models
from books.models import Book
from users.models import User

class Meeting(models.Model):

    date = models.DateTimeField()
    place = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    particepents = models.ManyToManyField(
        User,
        through='MeetingToUser'
    )

class MeetingToUser(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.PROTECT, null=True)
