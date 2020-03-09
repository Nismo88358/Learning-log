"""Определяет схемы URL для пользователей"""
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'
urlpatterns = [
    # Страница входа
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register')
]
