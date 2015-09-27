import os.path
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from learn.models import DemoPost,Struct
from learn.pageAnalyst import analyse
from django.template.context_processors import request
import os
def archive(request,coursename):
    
    posts = DemoPost.objects.filter(forum_name= coursename)
    print posts[0].forum_name
    print len(posts)
    t = loader.get_template("demo.html")
    
    if os.path.exists(os.getcwd()+"\\temp\\"+coursename+".tmp"):
        print "done!"
        structFile = open(os.getcwd()+"\\temp\\"+coursename+".tmp",'r')
        structs = []
        for line in structFile:
            seg = line.split('+')
            name = seg[0]
            code = seg[1]
            stu = Struct(name = name,code = code)
            structs.append(stu)
            print stu.code
        c = Context({'posts':posts,'structs':structs})
        
    else:
        
        #analyse(coursename)
        structFile = open(os.getcwd()+"\\temp\\"+coursename+".tmp",'r')
        structs = []
        for line in structFile:
            seg = line.split('+')
            name = seg[0]
            code = seg[1]
            stu = Struct(name = name,code = code)
            structs.append(stu)
            print stu.code
        c = Context({'posts':posts,'structs':structs})
        
    return HttpResponse(t.render(c))