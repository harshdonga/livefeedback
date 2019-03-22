from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index , name = "Loginpage"),
    path('login/' , views.login , name = "login"),
    path('login/submit/' , views.submit , name = "submit")
]
