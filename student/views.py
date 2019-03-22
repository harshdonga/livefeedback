from django.shortcuts import render
from .models import sdata , submissiondata
import requests
import json
import time as t
from .serializers import answersserializer
from rest_framework import viewsets
from textblob import TextBlob


def thanks(request):
    return render(request , 'student/thanks.html')
def index(request):
    return render(request , 'student/student.html')

def redirect(request):
    return render(request , 'student/signup.html')

def signup(request):
    name   = request.POST["username"]
    password = request.POST["password"]
    rid    = request.POST["id"]
    dept = request.POST["dept"]
    phone = request.POST["phone"]
    email = request.POST["email"]

    studentdata = sdata(name = name , rid = rid, phone = phone , dept = dept , email = email , password = password)
    studentdata.save()

    return render(request ,'student/thanks.html', { 'name' : name })

def response(request):
    q1 = request.POST['fq1']
    q2 = request.POST['fq2']
    q3 = request.POST['fq3']
    q4 = request.POST['dropdown']
    text = request.POST['textinput']

    test = TextBlob(text)
    q5 = test.sentiment.polarity

    resp = submissiondata(q1 = q1 , q2 = q2 , q3 = q3 , q4 = q4 , q5 = q5 , q5text = text)
    resp.save()

    return render(request ,'student/thanks.html')

class answerViewSet(viewsets.ModelViewSet):
    queryset = submissiondata.objects.all()
    serializer_class = answersserializer


def login(request):
    username = request.POST['lname']
    password = request.POST['lpass']
    dataset =sdata.objects.all()

    try:
        selected = dataset.get(name = username)
        print("student Found")
    except Exception as e:
        return render(request , 'student/access.html' )

    if(password == selected.password):
        apiurl = 'http://127.0.0.1:8000/api/faculty/'
        r = requests.get(apiurl).json()
        ti = t.time()
        t3600 = ti+3600
        return render(request , 'student/response.html' , {'dataset' : dataset , 'r':r , 't3600' : t3600})
    else:
        return render(request , 'student/access.html' )
