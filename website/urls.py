from django.contrib import admin
from django.urls import path, include
from website.views import *

#app_name = "website"

urlpatterns = [
    path('', home, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact')
]