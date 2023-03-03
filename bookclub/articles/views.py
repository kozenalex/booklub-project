from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from articles.models import Article
from books.models import Book
from users.models import MyUser

class ArticleCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):

    model = Article
    template_name = 'edit.html'
    fields = ['text']
    success_message = 'Отзыв успешно оуликован!'
    success_url = reverse_lazy('books_list')
    extra_context = {
        'title': 'Отзыв на книгу',
        'button': 'Опубликовать'
    }

    def get(self, request, *args, **kwargs):
        book = Book.objects.get(pk=kwargs['pk'])
        self.extra_context['book'] = book
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        book = Book.objects.get(pk=kwargs['pk'])
        author = MyUser.objects.get(pk=request.user.id)
        Article.objects.create(
            book=book,
            author=author,
            text=request.POST.get('text')
        )
        return redirect(self.success_url)