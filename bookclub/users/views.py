from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.list import ListView
from django.contrib import messages
from django.db.models import ProtectedError
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from users.forms import MyUserCreationForm, ProfileForm
from users.models import Profile


class UserView(LoginRequiredMixin, SuccessMessageMixin):

    login_url = 'login'
    model = Profile


class UsersListView(ListView):

    model = Profile
    context_object_name = 'users_list'
    template_name = 'users.html'


class UserCreateView(SuccessMessageMixin, CreateView):

    model = Profile
    form_class = MyUserCreationForm
    template_name = 'edit.html'
    success_message = 'Регистрация прошла успешно!'
    extra_context = {
        'tele_form': ProfileForm,
        'title': 'Регистрация в клубе',
        'button': 'Зарегистрироваться'
    }
    success_url = reverse_lazy('login')


class UserUpdateView(UserView, UpdateView):

    form_class = MyUserCreationForm
    model = User
    template_name = 'edit.html'
    extra_context = {
        'tele_form': ProfileForm,
        'title': _('Update user profile'),
        'button': _('Update')
    }
    success_message = _('Profile updated')
    success_url = reverse_lazy('users_list')


class UserPassChangeView(UserView, PasswordChangeView):

    template_name = 'pass_change.html'
    success_message = _('Password changed')
    success_url = reverse_lazy('users_list')


class UserDeleteView(UserView, DeleteView):

    template_name = 'confirm_delete.html'
    extra_context = {
        'title': _('Delete user'),
        'is_user': True
    }
    success_message = _('User profile deleted')
    success_url = reverse_lazy('users_list')

    def post(self, request, *args, **kwargs):
        try:
            request.user.delete()
            messages.success(request, self.success_message)
        except ProtectedError:
            messages.error(request, _('You can not delete user who is in use'))
        return redirect(self.success_url)