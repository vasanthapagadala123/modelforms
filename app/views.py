from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from app.forms import *
def insert_topic(request):
    form=Topicform()
    d={'form':form}
    if request.method=='POST':
       form_data=Topicform(request.POST)
       if form_data.is_valid():
          form_data.save()
          return HttpResponse('toipc model data insert')
    return render(request,'insert_topic.html',d)
def insert_webpage(request):
    form=webpageform()
    d={'form':form}
    if request.method=='POST':
       form_data=webpageform(request.POST)
       if form_data.is_valid():
          form_data.save()
          return HttpResponse('webpage model data insert')
    return render(request,'insert_webpage.html',d)
def insert_access(request):
    form=accessform()
    d={'form':form}
    if request.method=='POST':
       form_data=accessform(request.POST)
       if form_data.is_valid():
          form_data.save()
          return HttpResponse('access model data insert')
    return render(request,'insert_access.html',d)