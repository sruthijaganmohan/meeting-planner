from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meetings

# Create your views here.

def welcome(request):
    return render(request, "website/welcome.html", 
                  {'meetings': Meetings.objects.all()})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("My name is Sruthi, I am 21 years old")