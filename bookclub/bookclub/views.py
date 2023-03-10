from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import TempUserForm
from users.models import MyUser
from meetings.models import Meeting
from articles.models import Article
from bookclub.mixins import HomeContextMixin

class HomeView(HomeContextMixin, TemplateView):

    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        return {
        'meeting': HomeContextMixin.get_next_meeting(),
        'form': TempUserForm,
        'article': HomeContextMixin.get_last_article()
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