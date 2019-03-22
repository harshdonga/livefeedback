from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index, name = "homepage"),
    path('faculty/' , include('faculty.urls')),
    path('student/' , include('student.urls')),
    path('api/' , include('faculty.api_urls')),
    path('api/' , include('student.api_urls'))

]
