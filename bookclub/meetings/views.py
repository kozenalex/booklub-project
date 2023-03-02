from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, FormView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from meetings.forms import MeetingCreateForm
from users.forms import TempUserForm
from users.models import MyUser, TempUser

from meetings.models import Meeting

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

class AddMeetingLoginMember(LoginRequiredMixin, FormView):
     
     meeting = Meeting.objects.all().last()
     template_name = 'home.html'
     extra_context = {
         'meeting': meeting
     }

     def post(self, request, *args: str, **kwargs):
        curr_user = request.user.id
        if self.meeting.particepents.filter(id=curr_user):
            messages.warning(request, 'Вы уже зарегистрированы на встречу!')
        else:
            self.meeting.particepents.add(
                curr_user
            )
            self.meeting.save()
            messages.success(request, 'Вы успешно зарегистрированы на встречу!')
        return render(request, self.template_name, context=self.extra_context)


class AddMeetingMember(FormView):

    meeting = Meeting.objects.last()
    form_class = TempUserForm
    success_url = reverse_lazy('index_page')
    success_message = 'Вы успешно записаны на следующую встречу!'
    template_name = 'home.html'
    extra_context = {
         'meeting': meeting
    }


    def form_valid(self, form):
        data = form.cleaned_data
        if self.meeting.temp_users.filter(telegram=data['telegram']) or \
            self.meeting.temp_users.filter(email=data['email']):
                self.success_message = 'Вы уже зарегистрированы на встречу!'
        else:
            t = TempUser.objects.create(
                name=data['name'],
                email=data['email'],
                telegram=data['telegram']
            )
            t.save()
            m = Meeting.objects.all().last()
            m.temp_users.add(t)
            m.save()
        messages.success(self.request, self.success_message)    
        return super().form_valid(form)
