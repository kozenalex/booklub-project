from django.urls import path, include
from books import views

urlpatterns = [
    path('', views.BooksListView.as_view(), name='books_list'),
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    path('<int:pk>', views.BookView.as_view(), name='book_detail'),
    path('<int:pk>/articles/', include('articles.urls')),
    path('api/<int:pk>', views.BookApiDetail.as_view()),
    path('api/create/', views.BookApiCreate.as_view()),
    #path('<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    #path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]
