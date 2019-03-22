from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import questionsserializer
from .models import questions , fdata
import time
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def index(request):
    return render(request , 'faculty/login.html')


def login(request):
    name = request.POST['username']
    password = request.POST['password']
    dataset =fdata.objects.all()

    try:
        selected = dataset.get(name = name)
    except Exception as e:
        return render(request , 'faculty/access.html')
    if(password == selected.password):
        print("Faculty Found")
        apiurl = 'http://127.0.0.1:8000/api/student/'
        r = requests.get(apiurl).json()
        q1 = []
        q2= []
        q3= []
        q4 = []
        posv = []
        negv =[]
        neuv =[]
        counter = 0
        c = []
        url = []
        m = 5
        analyzer = SentimentIntensityAnalyzer()
        for x in r:
            q1.append(x['q1'])
            q2.append(x['q2'])
            q3.append(x['q3'])
            q4.append(x['q4'])
            analy = analyzer.polarity_scores(x['q5text'])
            pos = analy['pos']
            neg = analy['neg']
            neu = analy['neu']
            posv.append(pos*m)
            negv.append(neg*m)
            url.append(x['url'])
            counter += 1
            c.append(counter)
        maxstr = max(q4)
        context = {
            'q1': q1,
            'q2': q2,
            'q3': q3,
            'posv':posv,
            'negv':negv,
            'neuv':neuv,
            'c': c,
            'maxstr': maxstr,
            'url' : url
        }
        return render(request , 'faculty/teacher.html' ,context )

def submit(request):
    fq1 = request.POST['fq1']
    fq2 = request.POST['fq2']
    fq3 = request.POST['fq3']
    topic1 = request.POST['topic1']
    topic2 = request.POST['topic2']
    topic3 = request.POST['topic3']
    topic4 = request.POST['topic4']
    topic5 = request.POST['topic5']

    q = questions(fq1 = fq1 , fq2 = fq2 , fq3 = fq3 , topic1 = topic1 , topic2 = topic2 , topic3 = topic3 , topic4 = topic4 , topic5 = topic5)
    ti = time.time()
    q.save()
    return HttpResponse(request ,'')
    # while(time.time() <= ti):
    #     pass
    # q.delete()

#def view(request):



class questionsViewSet(viewsets.ModelViewSet):
    queryset = questions.objects.all()
    serializer_class = questionsserializer
