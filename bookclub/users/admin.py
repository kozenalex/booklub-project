from django.contrib import admin
from users.models import MyUser, TempUser
# Register your models here.

admin.site.register(MyUser)
admin.site.register(TempUser)