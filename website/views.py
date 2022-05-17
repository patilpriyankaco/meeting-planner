from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting


# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html",
    {"meetings" : Meeting.objects.all()})

def daterequest(request):
    return HttpResponse("This page is served at :" + str(datetime.now()))

def selfabout(request):
    return HttpResponse("HI..Im Priyanka 28 years old and computer engineer doing job preparation")