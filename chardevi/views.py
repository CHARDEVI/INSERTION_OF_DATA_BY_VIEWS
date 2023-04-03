from django.shortcuts import render
from chardevi.models import *
from django.http import HttpResponse

# Create your views here.

def insert_topic(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic_name is inserted')
def insert_webpage(request):
    tn=input('enter topic_name')
    n=input('enter name')
    url=input('enter url')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    return HttpResponse('insert_webpage is inserted')
def insert_accessrecord(request):
    tn=input('enter topic_name')
    n=input('enter name')
    url=input('enter url')
    a=input('enter author')
    d=input('enter date')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    AR=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    AR.save()
    return HttpResponse('insert_accessrecord is inserted')