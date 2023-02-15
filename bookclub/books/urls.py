from django.urls import path
from books import views

urlpatterns = [
    path('', views.BooksListView.as_view(), name='books_list'),
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    #path('<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    #path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]
