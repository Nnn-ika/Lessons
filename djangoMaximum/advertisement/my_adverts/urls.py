from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main_page'),
    path('top-sellers', topSellers, name='top_sellers'),
    path('advertisement-post', advertisementPost, name='advertisement_post'),
    path('advertisement', advertisement),
]