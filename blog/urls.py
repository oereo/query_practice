from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import post_list

urlpatterns = [
        path('', post_list, name='post_list'),
]