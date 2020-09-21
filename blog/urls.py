from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import post_list, status_check

urlpatterns = [
    path('', post_list, name='post_list'),
    path('status/', status_check, name='status_check'),
]