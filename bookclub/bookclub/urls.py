"""bookclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import bookclub.views
from django.conf.urls.static import static
from bookclub import settings
import users

urlpatterns = [
    path('admin/', admin.site.urls),
    #path to djoser end points
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    #path to local apps endpoints
    path('', bookclub.views.HomeView.as_view(), name='index_page'),
    path('users/', include('users.urls')),
    path('books/', include('books.urls')),
    path('meetings/', include('meetings.urls')),
    path('articles/', include('articles.urls')),
    path('login/', bookclub.views.UserAuthView.as_view(), name='login'),
    path('logout/', bookclub.views.UserLogoutView.as_view(), name='logout')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)