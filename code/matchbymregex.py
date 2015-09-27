#!/usr/bin/python

'''This code is to find the posts which contain certain keyword
Usage: python matchbykeyword [coursename] [subforumid] [keyword]
Input: a set of post files
Output: names of files which contain the keyword
'''

import os
import sys
import re

count = 0
def findRef(postfilename):
    global count
    #read post text file
    f = file(postfilename)
    post_text = ""
    for line in f:
        post_text += line
    f.close()
    
    #match regex
    regex = keyword + 		
    match = re.findall(regex,post_text.lower())
    if match:
        print postfilename, match
        count = count + len(match)
    
coursename = sys.argv[1]
subforumid = sys.argv[2]
#keyword = sys.argv[3]
keyword = '(problem|quiz|question|exam|module|lecture|slide|video)'
maindir = "/home/chencan/post_text/"+coursename+os.sep+subforumid
postlist = os.listdir(maindir)
for postfile in postlist:
    try:
        findRef(maindir+os.sep+postfile)
    except Exception,e:
        print e,postfile,"Wrong"
print count
