from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import TempUserForm
from users.models import MyUser, TempUser

from meetings.models import Meeting

class MeetingsListView(ListView, LoginRequiredMixin):

    model = Meeting
    template_name = 'meetings.html'
    context_object_name = 'meetings_list'
    

class MeetingCreateView(CreateView, LoginRequiredMixin, SuccessMessageMixin):

    model = Meeting
    template_name = 'edit.html'
    success_message = ('Встреча запланирована')
    success_url = reverse_lazy('index_page')
    fields = ['date', 'book', 'place']
    extra_context = {
        'button': 'Запланировать'
    }

class AddMeetingMember(FormView, SuccessMessageMixin):

    form_class = TempUserForm
    success_url = reverse_lazy('index_page')
    success_message = 'Вы успешно записаны на следующую встречу!'

    def form_valid(self, form):
        data = form.cleaned_data
        t = TempUser.objects.create(
            name=data['name'],
            email=data['email'],
            telegram=data['telegram']
        )
        t.save()
        m = Meeting.objects.all().last()
        m.temp_users.add(t)
        m.save()
        return super().form_valid(form)
