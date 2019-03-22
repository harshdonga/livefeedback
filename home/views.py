from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request , 'home/index.html')

def contact(request):
    return render(request , 'home/contact.html')

def gallery(request):
    return render(request , 'home/gallery.html')

def about(request):
    return render(request , 'home/about.html')
