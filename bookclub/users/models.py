from django.contrib.auth.models import User
from django.db import models
import django.core.validators as validators
from django.utils.deconstruct import deconstructible


@deconstructible
class UnicodeTelegramValidator(validators.RegexValidator):
    regex = r"[\w]{5,254}"
    message = """"
        "Введите правильный ник телеграм, в нем не менее 5 символов. допущены буквы, цифры и подчеркивание"
    """
    flags = 0


class MyUser(User):

    telegram = models.CharField(
        max_length=255,
        blank=True,
        validators=[UnicodeTelegramValidator()],
        help_text="Ваш правильный ник в телерам, если он есть"
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
        help_text="Ваш правильный ник в телерам, если он есть",
    )

    def __str__(self) -> str:
        return self.name