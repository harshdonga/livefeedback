from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index , name = "Login"),
    path('redirect/signup/' , views.signup , name = "Signup"),
    path('login/' , views.login , name = "Login"),
    path('redirect/' , views.redirect , name = "redirect"),
    path('login/response/' , views.response , name = "thanks")

    #path('feedback' , views.feedback , name = 'feedback')
]
