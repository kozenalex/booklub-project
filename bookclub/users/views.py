from django.shortcuts import redirect
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.list import ListView
from django.contrib import messages
from django.db.models import ProtectedError
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import MyUserCreationForm, UserAvaUpdateForm, UserUpdateForm
from users.models import MyUser

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer


class UserView(LoginRequiredMixin, SuccessMessageMixin):

    login_url = 'login'
    model = MyUser


class UsersListView(ListView):

    model = MyUser
    context_object_name = 'users_list'
    template_name = 'users.html'


class UserCreateView(SuccessMessageMixin, CreateView):

    model = MyUser
    form_class = MyUserCreationForm
    template_name = 'edit.html'
    success_message = 'Регистрация прошла успешно!'
    extra_context = {
        'title': 'Регистрация в клубе',
        'button': 'Зарегистрироваться',
        'is_user': False
    }
    success_url = reverse_lazy('login')

class UserUpdateView(UserView, UpdateView):

    form_class = UserUpdateForm
    model = MyUser
    template_name = 'edit.html'
    context_object_name = 'user'
    extra_context = {
        'title': 'Изменение профиля пользователя',
        'button': 'Изменить',
        'is_user': True
    }
    success_message = 'Профиль успешно изменен'
    success_url = reverse_lazy('users_list')


class UserPassChangeView(UserView, PasswordChangeView):

    template_name = 'pass_change.html'
    success_message = 'Password changed'
    success_url = reverse_lazy('users_list')


class UserAvaChangeView(UserView, UpdateView):

    form_class = UserAvaUpdateForm
    context_object_name = 'user'
    template_name = 'ava_change.html'
    success_message = 'Avatar changed'
    
    def get_success_url(self) -> str:
        user_id = self.get_object().id
        return reverse_lazy('user_update', kwargs={'pk': user_id})

class UserDeleteView(UserView, DeleteView):

    template_name = 'confirm_delete.html'
    extra_context = {
        'title': 'Удалить профиль пользователя',
        'is_user': True
    }
    success_message = 'Профиль успешно удален'
    success_url = reverse_lazy('users_list')

    def post(self, request, *args, **kwargs):
        try:
            request.user.delete()
            messages.success(request, self.success_message)
        except ProtectedError:
            messages.error(request, 'You can not delete user who is in use')
        return redirect(self.success_url)

class UserProfileApiView(RetrieveUpdateDestroyAPIView):
    queryset=MyUser.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]