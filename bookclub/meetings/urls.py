from django.urls import path
from meetings import views

urlpatterns = [
    path('', views.MeetingsListView.as_view(), name='meetings_list'),
    path('create/', views.MeetingCreateView.as_view(), name='meeting_create'),
    #path('<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    #path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]
