"""socialbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from logbook import views
from django.urls import path

from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout', views.logout,name='logout'), 
    path('signin', views.signin,name='signin'),   
    path('profile/', views.edit_profile, name='edit_profile'),
    path('post/', views.insta_post1),
    path('insta_post/', views.insta_post),
    path('', views.home),
    path('p/', views.p),
    path('user_other/<username>/',views.user),
    path('follow/<username>/',views.follow),
    path('unfollow/<username>/',views.unfollow),
    path('liked<pk>/',views.liked,name='liked'),
    path('unliked<pk>/',views.unliked,name='liked'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    ]

