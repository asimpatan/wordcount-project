"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/

"""

# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('count/', views.count, name = "wordcount"),
    path('about/', views.about, name = "about"),
]
