from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

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

