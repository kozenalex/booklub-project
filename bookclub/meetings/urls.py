from django.urls import path
from meetings import views

urlpatterns = [
    path('', views.MeetingsListView.as_view(), name='meetings_list'),
    path('create/', views.MeetingCreateView.as_view(), name='meeting_create'),
    path('members/add/', views.AddMeetingMember.as_view(), name='add_meeting_member'),
    path('loginmembers/add/', views.AddMeetingLoginMember.as_view(), name='add_login_meeting_member'),
    #path('<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    #path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]
