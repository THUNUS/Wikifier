import sys
import os
import re
from sys import argv
from compiler.pycodegen import EXCEPT
def findFilesContainKeyWords(maindir,postfilename,keyword,tempdir):

    #read post filename
    f = file(maindir+os.sep+postfilename)
    post_file = ""
    for line in f:
        post_file += line
    f.close()
    
    #match using regex
    regex = keyword +'( *\d+ *?[\.-]? *?\d*)'
    match = re.findall(regex, post_file.lower())
    if match:
        print postfilename
        nf = open(tempdir+os.sep+postfilename,'w')
        nf.write(post_file)
        nf.close()
    
coursename = sys.argv[1]
subforumid = sys.argv[2]
keyword = '(problem|quiz|question|exams|module|lecture|slide|video|homework|[Ww]eek)'
maindir = 'D:\\Java\\workplace\\research\\moocwiki\\post_text'+os.sep+coursename + os.sep + subforumid
tempdir = 'D:\\Java\\workplace\\research\\moocwiki\\temp'+os.sep+coursename + os.sep + subforumid
os.makedirs(tempdir)
postlist = os.listdir(maindir)
for postfile in postlist:
	try:
		findFilesContainKeyWords(maindir,postfile,keyword,tempdir)
	except Exception,e:
		print e,"Wrong"
            
    