#!/usr/bin/python

'''This code is to find the posts which contain annotated
reference in the annotated post text and output the filename,
the content of referent and the position of the reference.
Usage: python findannotatedref.py [coursename] [subforumid]
Input: a set of annotated post files
Output: names of files which contain reference, content of
reference, position of reference. 
'''

import os
import sys
import re

def findAnnotatedRef(postfilename):
    #read post text file
    f = file(postfilename)
    post_text = ""
    for line in f:
        post_text += line
    f.close()
    
    #match regex
    regex ='<ref'+'.*?'+'</ref>'
    matches = re.findall(regex,post_text.lower())
    if matches:
        pre_ref_len = 0
        print postfilename,
        for match in matches:
            start =  post_text.lower().index(match)
            end = start + len(match) - 1
            sub_match = re.search(r'(<ref.*>)(.*)</ref>',match)
            ref_len = len(sub_match.group(1)) 
            content_len = len(sub_match.group(2))
            print match,'['+ str(start-pre_ref_len)+','+str(end-ref_len-len(r'</ref>')-pre_ref_len)+']',
            print content_len,content_len == (end-ref_len-len(r'</ref>')-pre_ref_len)-(start-pre_ref_len)+1,
            pre_ref_len += len(match)
        print
    
coursename = sys.argv[1]
subforumid = sys.argv[2]
#keyword = sys.argv[3]
maindir = "/home/chencan/moocwiki/annotated/"+coursename+os.sep+subforumid
postlist = os.listdir(maindir)
for postfile in postlist:
    try:
        findAnnotatedRef(maindir+os.sep+postfile)
    except:
        print postfile,"Wrong"
