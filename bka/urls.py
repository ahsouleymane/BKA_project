from django.contrib import admin
from django.urls import path, include
from bka import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
]
