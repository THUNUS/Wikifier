#code:utf-8
from learn.models import DemoPost
from wikiDemo import settings
import os
import sys

def saveFiles(maindir,coursename,postfilename):

    #read post filename
    f = file(maindir+os.sep+postfilename)
    post_file = ""
    for line in f:  
        post_file += line
    f.close()
    post = DemoPost(forum_name =coursename,title= postfilename,body=post_file)
    post.save()
    return
    
coursename = sys.argv[1]
subforumid = sys.argv[2]

maindir = 'G:\\workplace\\git\\moocwiki\\annotated'+os.sep+coursename + os.sep + subforumid
os.environ['DJANGO_SETTINGS_MODULE'] = 'demo.settings'
postlist = os.listdir(maindir)
for postfile in postlist:
    try:
        saveFiles(maindir,coursename,postfile)
    except Exception,e:
        print e,"Wrong"
            
    