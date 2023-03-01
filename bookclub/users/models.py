from django.contrib.auth.models import User
from django.db import models
import django.core.validators as validators
from django.utils.deconstruct import deconstructible


@deconstructible
class UnicodeTelegramValidator(validators.RegexValidator):
    regex = r"^@[\w]{1,254}"
    message = """"
        "Введите правильный ник телеграм, он начинается с @."
    """
    flags = 0


class MyUser(User):

    telegram = models.CharField(
        max_length=255,
        blank=True,
        validators=[UnicodeTelegramValidator()],
        help_text="Обязательное поле. Начинается с @"
    )
    avatar = models.ImageField(
        upload_to='avatars/%Y-%m-%d',
        null=True,
        blank=True
    )
    def __str__(self):
        return self.get_full_name()


class TempUser(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    telegram = models.CharField(
        max_length=255,
        validators=[UnicodeTelegramValidator()],
        help_text="Обязательное поле. Начинается с @",
    )

    def __str__(self) -> str:
        return self.name