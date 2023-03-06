from django.db import models
from books.models import Book
from users.models import MyUser, TempUser
from django.core.mail import send_mail

class Meeting(models.Model):

    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(null=True)
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
        members = self.particepents.all() if self.particepents else self.particepents
        return list(others) + list(members)
    
    def send_meet_mail(self, recipients):

        send_mail(
                subject=f'Книжный клую "Фантастика"',
                message=f'''Вы зарегистрированы на встречу книжного клуба,
                  которая состоится {self.date} в {self.time}.
                  Место встречи: {self.place}''',
                from_email='akosin@udm.ru',
                recipient_list=recipients
            )

    def __str__(self) -> str:
        return f'Встреча {self.date}'

class MeetingToUser(models.Model):

    user = models.ForeignKey(MyUser, on_delete=models.PROTECT, null=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.PROTECT, null=True)
