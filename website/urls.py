from django.contrib import admin
from django.urls import path, include
from website.views import *

urlpatterns = [
    path('', home),
    path('about', about),
    path('contact', contact)
]