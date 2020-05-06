from django.urls import path, include
#import all functions from views.py
from . import views

urlpatterns = [
  path('signup', views.signup, name="signup"),
  path('login', views.login, name="login"),
   path('logout', views.logout, name="logout"),
]