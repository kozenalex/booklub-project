from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from users.forms import TempUserForm
from users.models import MyUser
from meetings.models import Meeting

class HomeView(TemplateView):

    template_name = 'home.html'
    extra_context = {
        'm': Meeting.objects.all().first(),
        'form': TempUserForm
    }


class UserAuthView(SuccessMessageMixin, LoginView):

    model = MyUser
    template_name = 'login.html'
    success_message = 'Вы вошли успешно!'


class UserLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'Вы вышли из профиля!')
        return super().dispatch(request, *args, **kwargs)