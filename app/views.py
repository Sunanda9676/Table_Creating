from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topics(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)


def display_webpage(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)