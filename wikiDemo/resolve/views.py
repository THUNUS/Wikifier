from django.shortcuts import render
from learn.urldeode import decode
from django.http import HttpResponseRedirect
from courseInfo.models import courseVideo
import django
import re
import json 
def redirect(request,para):
    print "redirect"
    para = para.split('/')
    post = {}
    if list(para).count('section') != 0:
        print para
        post['course'] = para[0]
        post['object'] = para[1]
        post['chapter'] = para[list(para).index('section')-1]
        post['section'] = para[list(para).index('section')+1]
        lst = []
        lst.append(int(post['chapter'].encode("utf-8")))
        lst.append(int(post['section'].encode("utf-8")))
        post['section']  = lst
        print post['section']
        id = decode(post)
        return HttpResponseRedirect("https://class.coursera.org/"+post['course']+"/"+post['object']+"/"+id)
    elif list(para).count('week') != 0 :
        post['course'] = para[0]
        post['object'] = para[1]
        return HttpResponseRedirect("https://class.coursera.org/"+post['course']+"/"+"lecture")
    elif list(para).count('lecture') != 0 and len(para) == 3:
        post['course'] = para[0]
        post['object'] = para[1]
        post['chapter'] = para[2]
        if post['chapter'].isdigit() is False:
            try:
                link = courseVideo.objects.filter(courseName = post['course'],videoName = post['chapter'])[0].resource_link
                return HttpResponseRedirect(link)
            except:
                pass
        else:
            return HttpResponseRedirect("https://class.coursera.org/"+post['course']+"/"+"lecture")

    elif list(para).count('lecture') != 0 and para.count('slide') !=0:
        post['course'] = para[0]
        post['object'] = para[1]
        post['chapter'] = para[2].encode('utf-8')
        post['subObject'] = para[3]
        post['page'] = para[4].encode('utf-8')
        print post['page']
        return HttpResponseRedirect("https://d396qusza40orc.cloudfront.net/"+post['course']+"/docs/slides/Lecture"+post['chapter']+".pdf#page="+post['page'])