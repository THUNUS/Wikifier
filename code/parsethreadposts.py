#!/usr/bin/python

'''This code is to extract post text from json files.
Usage: python parsethreadposts.py [coursename] [subforumid]
Input:  a set of json files
Output: a set of post files 
'''

import json
import os
import sys

def extractText(jsonfilename):
    #read json file
    f = file(jsonfilename)
    thread = json.load(f)
    f.close

    #extract text
    threadid = thread['id']
    print threadid
    postlist = []
    for post in thread['posts']:
        if 'post_text' not in post or post['post_text'] == "":
            print 'no post text', post['id']
            continue
        postid, posttext = post['id'], post['post_text']
        postlist.append([postid, posttext])

    #store in files, one post in one file
    s = jsonfilename.split('.')
    postnameprefix = s[1]+'.'+s[2]+'.'+s[3]+'.'
    postnamesuffix = '.post'
    resultdir = "/home/chencan/post_text/"+coursename+os.sep+subforumid+os.sep
    for postid, posttext in postlist:
        f = open(resultdir + postnameprefix + str(postid) + postnamesuffix,'w')
        f.write(posttext.encode('utf-8'))
        f.close()

coursename = sys.argv[1]
subforumid = sys.argv[2]
maindir = "/home/chencan/Data/"+coursename+os.sep+subforumid+"/posts"
jsonfilelist = os.listdir(maindir)
for jsonfile in jsonfilelist:
    if jsonfile[-5:] != ".json":
        continue
    try:
        extractText(maindir+os.sep+jsonfile)
    except:
        print jsonfile, "wrong!"
