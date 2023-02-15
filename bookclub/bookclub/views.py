from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from users.models import User

class HomeView(TemplateView):

    template_name = 'home.html'


class UserAuthView(SuccessMessageMixin, LoginView):

    model = User
    template_name = 'login.html'
    success_message = 'Вы вошли успешно!'


class UserLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'Вы вышли из профиля!')
        return super().dispatch(request, *args, **kwargs)