from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.project, name='home'),
    path('profile/', views.profile, name='profile')
]