from .views import *
from django.urls import path

urlpatterns = [
    path('home/', home, name= 'home')
]