from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from articles.models import Article
from books.models import Book, BookRaiting
from users.models import MyUser

class ArticleCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):

    login_url = reverse_lazy('login')
    model = Article
    template_name = 'edit.html'
    fields = ['text']
    success_message = 'Отзыв успешно оуликован!'
    extra_context = {
        'title': 'Отзыв на книгу',
        'button': 'Опубликовать',
        'is_article': True
    }

    def get(self, request, *args, **kwargs):
        book = Book.objects.get(pk=kwargs['pk'])
        self.extra_context['book'] = book
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        book = Book.objects.get(pk=kwargs['pk'])
        author = MyUser.objects.get(pk=request.user.id)
        raiting = request.POST.get('rating')
        curr_author_raiting = BookRaiting.objects.filter(user=author).filter(book=book)
        if curr_author_raiting:
            curr_author_raiting.update(raiting=raiting)
        else:
            BookRaiting.objects.create(
                book=book,
                user=author,
                raiting=raiting
            )
        Article.objects.create(
            book=book,
            author=author,
            text=request.POST.get('text')
        )
        return redirect(reverse_lazy(
            'book_detail',
            kwargs={'pk':book.id}
        ))

class ArticleUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):

    login_url = reverse_lazy('login')
    model = Article
    fields = ['text']
    template_name = 'edit.html'
    extra_context = {
        'title': 'Отзыв на книгу',
        'button': 'Опубликовать',
        'is_article': True
    }

    def get_success_url(self) -> str:
        book = self.get_object().book
        return reverse_lazy(
            'book_detail',
            kwargs= {'pk': book.id}
        )
    
    def get(self, request, *args: str, **kwargs):
        self.extra_context['book'] = self.get_object().book
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        author = MyUser.objects.get(pk=request.user.id)
        book = Book.objects.get(pk=self.get_object().book.id)
        raiting = request.POST.get('rating')
        curr_author_raiting = BookRaiting.objects.filter(user=author).filter(book=book)
        if curr_author_raiting and raiting:
            curr_author_raiting.update(raiting=raiting)
        elif not curr_author_raiting and raiting:
            BookRaiting.objects.create(
                book=book,
                user=author,
                raiting=raiting
            )
        return super().post(request, *args, **kwargs)