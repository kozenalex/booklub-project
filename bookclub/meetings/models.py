from django.db import models
from books.models import Book
from users.models import MyUser, TempUser

class Meeting(models.Model):

    date = models.DateTimeField()
    place = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    particepents = models.ManyToManyField(
        MyUser,
        through='MeetingToUser'
    )
    temp_users = models.ManyToManyField(TempUser, blank=True)

    @property
    def get_people(self):
        others = self.temp_users.all() if self.temp_users else self.temp_users
        return others

class MeetingToUser(models.Model):

    user = models.ForeignKey(MyUser, on_delete=models.PROTECT, null=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.PROTECT, null=True)
