from django.urls import path
from .views import *

urlpatterns = [
    path('register', register, name='register'),
    path('login', logIn, name='login'),
    path('profile', profileView, name='profile'),
    path('logout', logOut, name='logout'),
]