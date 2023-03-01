from django.db import models
from books.models import Book
from users.models import MyUser, TempUser

class Meeting(models.Model):

    date = models.DateField(verbose_name='Дата')
    place = models.CharField(max_length=255, verbose_name='Место встречи')
    book = models.ForeignKey(Book, on_delete=models.PROTECT, verbose_name='Книга')
    particepents = models.ManyToManyField(
        MyUser,
        through='MeetingToUser',
        blank=True
    )
    temp_users = models.ManyToManyField(TempUser, blank=True)

    @property
    def get_people(self):
        others = self.temp_users.all() if self.temp_users else self.temp_users
        return others
    
    def __str__(self) -> str:
        return f'Встреча {self.date}'

class MeetingToUser(models.Model):

    user = models.ForeignKey(MyUser, on_delete=models.PROTECT, null=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.PROTECT, null=True)
