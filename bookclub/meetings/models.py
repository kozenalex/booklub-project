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
    temp_users = models.ForeignKey(TempUser, on_delete=models.CASCADE, null=True)

    @property
    def get_people(self):
        members = self.particepents.all() if self.particepents else self.particepents
        others = self.temp_users.all() if self.temp_users else self.temp_users
        return members + others

class MeetingToUser(models.Model):

    user = models.ForeignKey(MyUser, on_delete=models.PROTECT, null=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.PROTECT, null=True)
