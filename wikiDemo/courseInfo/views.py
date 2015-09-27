#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse
from courseInfo.models import courseVideo
import django
# Create your views here.
def sendInfo(request,para):
    django.setup()
    print para
    videos = courseVideo.objects.filter(courseName = para)
    response = "{\"course\":["
    for video in videos:
        try:
            response += "{\"video\":\""+video.videoName + "\",\"link\":\""+video.resource_link+"\"}"
            response += ",\n"
        except Exception:
            pass
    response = response[:-2]
    response += "]}"
    #print response
    return HttpResponse(response)
