from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index, name = "homepage"),
    path('faculty/' , include('faculty.urls')),
    path('student/' , include('student.urls')),
    path('api/' , include('faculty.api_urls')),
    path('api/' , include('student.api_urls')),
    path('gallery/' , views.gallery , name = "gallery"),
    path('index/' , views.index , name = "index"),
    path('contact/' , views.contact , name = "contact"),
    path('about/' , views.about , name = "about")

]
