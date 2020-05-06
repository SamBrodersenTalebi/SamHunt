from django.urls import path, include
#import all functions from views.py
from . import views

urlpatterns = [
  path('create', views.create, name='create'),
]