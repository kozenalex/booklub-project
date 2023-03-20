from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from books.models import Book, BookRaiting
from books.serializers import BookDetailSerializer
from articles.models import Article



class BooksView(SuccessMessageMixin):
    login_url = 'login'
    model = Book


class BooksListView(BooksView, ListView):

    context_object_name = 'books_list'
    template_name = 'books.html'
    extra_context = {'title': 'Книги клуба:'}


class BookCreateView(LoginRequiredMixin, BooksView, CreateView):

    fields = ['title', 'author', 'description', 'img']
    template_name = 'edit.html'
    success_message = 'Книга успешно добавлена!'
    success_url = reverse_lazy('books_list')
    extra_context = {
        'title': 'Добавить кнгу',
        'button': 'Добавить',
    }

class BookView(BooksView, TemplateView):

    template_name = 'book.html'
    def get_context_data(self, **kwargs):
        book = Book.objects.get(pk=kwargs['pk'])
        articles = Article.objects.filter(book=book.id).order_by('created_at').reverse()
        user_article = Article.objects.filter(author=self.request.user.id).filter(book=book.id)

        return {
            'book': book,
            'articles': articles,
            'user_article_exist': user_article.first().id if user_article else None,
            'raiting': book.get_raiting,
            'y_stars': book.get_yellow_stars,
            'b_stars': book.get_blank_stars
        }

class BookApiDetail(RetrieveAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()

class BookApiCreate(CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()

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
