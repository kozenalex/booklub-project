from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from books.models import Book



class BooksView(SuccessMessageMixin):
    login_url = 'login'
    model = Book


class BooksListView(BooksView, ListView):

    context_object_name = 'books_list'
    template_name = 'books.html'
    extra_context = {'title': 'Книги клуба:'}


class BookCreateView(LoginRequiredMixin, BooksView, CreateView):

    fields = ['title', 'description', 'img']
    template_name = 'edit.html'
    success_message = 'Book created successfuly'
    success_url = reverse_lazy('books_list')
    extra_context = {
        'title': 'Добавить кнгу',
        'button': 'Добавить',
    }


class StatusUpdateView(BooksView, UpdateView):

    fields = ['name']
    template_name = 'edit.html'
    extra_context = {
        'title': 'Update status',
        'button': 'Update'
    }
    success_message = 'Status updated successfuly'
    success_url = reverse_lazy('statuses_list')


class StatusDeleteView(BooksView, DeleteView):

    template_name = 'confirm_delete.html'
    extra_context = {
        'title': 'Delete status'
    }
    success_message = 'Status deleted'
    success_url = reverse_lazy('statuses_list')
