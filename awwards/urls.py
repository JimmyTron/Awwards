from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),

]