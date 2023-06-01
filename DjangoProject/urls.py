"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from alcohols.views import *
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('list_view/', AlcoholsListView.as_view(), name='list-view'),
    path('wines_view/', WinesListView.as_view(), name='wines-view'),
    path('recipe/<int:pk>/', AlcoholDetail.as_view(), name='alcohol-detail'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('recipe/<int:pk>/add_comment/', AddComment.as_view(), name='add-comment'),
    path('recipe/<int:pk>/add_fav/', AddFav.as_view(), name='add-fav'),
    path('ulubione/', FavoriteAlcoholsView.as_view(), name='fav'),
]
