from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic import ListView, FormView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from articles.models import Article
from meetings.forms import MeetingCreateForm
from users.forms import TempUserForm
from users.models import MyUser, TempUser
from meetings.models import Meeting
from bookclub.mixins import HomeContextMixin

class MeetingsListView(ListView, LoginRequiredMixin):

    model = Meeting
    template_name = 'meetings.html'
    context_object_name = 'meetings_list'
    

class MeetingCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):

    model = Meeting
    template_name = 'edit.html'
    success_message = 'Встреча запланирована'
    success_url = reverse_lazy('meetings_list')
    form_class = MeetingCreateForm
    extra_context = {
        'button': 'Запланировать'
    }

class AddMeetingLoginMember(HomeContextMixin, LoginRequiredMixin, FormView):
     
     next_meeting = HomeContextMixin.get_next_meeting()
     template_name = 'home.html'
     extra_context = {
         'meeting': next_meeting,
         'article': HomeContextMixin.get_last_article()
     }

     def post(self, request, *args: str, **kwargs):
        curr_user = request.user.id
        if self.next_meeting.particepents.filter(id=curr_user):
            messages.warning(request, 'Вы уже зарегистрированы на встречу!')
        else:
            self.next_meeting.particepents.add(
                curr_user
            )
            self.next_meeting.save()
            self.next_meeting.send_meet_mail([request.user.email])
            messages.success(request, 'Вы успешно зарегистрированы на встречу!')
        return render(request, self.template_name, context=self.extra_context)


class AddMeetingMember(HomeContextMixin, FormView):

    next_meeting = HomeContextMixin.get_next_meeting()
    form_class = TempUserForm
    success_url = reverse_lazy('index_page')
    success_message = 'Вы успешно записаны на следующую встречу!'
    template_name = 'home.html'
    extra_context = {
         'meeting': next_meeting
    }


    def form_valid(self, form):
        data = form.cleaned_data
        if self.next_meeting.temp_users.filter(telegram=data['telegram']) or \
            self.next_meeting.temp_users.filter(email=data['email']):
                self.success_message = 'Вы уже зарегистрированы на встречу!'
        else:
            t = TempUser.objects.create(
                name=data['name'],
                email=data['email'],
                telegram=data['telegram']
            )
            t.save()
            self.next_meeting.temp_users.add(t)
            self.next_meeting.save()
            self.next_meeting.send_meet_mail([t.email])
        messages.success(self.request, self.success_message)    
        return super().form_valid(form)

class MeetingUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Meeting
    fields = ['date', 'time', 'place', 'book', 'particepents', 'temp_users']
    success_url = reverse_lazy('meetings_list')
    success_message = 'Встреча обновлена успешно!'
    template_name = 'edit.html'
    extra_context = {
        'title': 'Изменение встречи',
        'button': 'Изменить'
    }
