from django.shortcuts import render
from .models import *
from .serializers import Noticeserializers
from .serializers import Eventserializers
from django.http import HttpResponse
from rest_framework.decorators import api_view

from rest_framework.renderers import JSONRenderer

# Create your views here.
def noticeall(request):
    nall = Notice.objects.all() #complex data - data quertyset 
    serializerdata = Noticeserializers(nall,many = True)# convert into python data type
    json_data = JSONRenderer().render(serializerdata.data)
    return HttpResponse(json_data,content_type="application/json")

def eventall(request):
    eall = Event.objects.all() #complex data - data quertyset 
    serializerdata = Eventserializers(eall,many = True)# convert into python data type
    json_data = JSONRenderer().render(serializerdata.data)
    return HttpResponse(json_data,content_type="application/json")