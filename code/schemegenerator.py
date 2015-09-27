#!/usr/bin/python
'''This code is to generate MOOC Xreference URL scheme.
Usage: python schemegenerator.py 
Input: post text and related meta data
Output: my MOOC Xreference URL scheme.
       like www.comp.nus.edu.sg/moocxresolver/globalcourseid/slide/slideid/pagenumber
            www.comp.nus.edu.sg/moocxresolver/globalcourseid/lecture/lectureid
            www.comp.nus.edu.sg/moocxresolver/globalcourseid/quiz/quizid
            www.comp.nus.edu.sg/moocxresolver/globalcourseid/question/questionid
'''

import os
import sys
import re
import argparse

#courselist_filepath = sys.argv[1]
#course2subforums_filepath = sys.argv[2]
#output_filepath = sys.argv[3] #postfilename->url
parser = argparse.ArgumentParser (prog='schemegenerator.py', description='scheme generator')
parser.add_argument('-cl', required=True, help='file path of course list')
parser.add_argument('-c2s', required=True, help='file path of the map between course and subforums')
parser.add_argument('-p', required=True, help='parent directory of all courses')
parser.add_argument('-o', required=True, help='file path of output')

args = parser.parse_args()
courselist_filepath = args.cl
course2subforums_filepath = args.c2s
parent_directory = args.p
output_filepath = args.o

prefix = 'wing.comp.nus.edu.sg/moocxresolver/'
keyword = '(problem|quiz|question|exam|module|lecture|slide|video)'
regex_suf = '( ?)(\d+ ?([\.-]?(?= ?\d+)) ?\d*)'
regex = keyword + regex_suf

courses = []
course2subforums = {}
with open(courselist_filepath) as f:
    for line in f:
        course = line.split()[0]
        courses.append(course)
with open(course2subforums_filepath) as f:
    for line in f:
        line = line.split()
        course2subforums[line[0]] = line[1:]
print course2subforums

url_post = []
for course in courses:
    globalcourseid = 'coursera-'+course
    subforums = course2subforums[course]
    for subforum in subforums:
        posts = os.listdir(parent_directory+os.sep+course+os.sep+subforum)
        posts.sort()
        for post in posts:
            with open(parent_directory+os.sep+course+os.sep+subforum+os.sep+post) as f:
                #read post text
                post_text = ''
                for line in f:
                    post_text += line
            
            #match regex 
            matches = re.findall(regex, post_text.lower())
            for match in matches:
                if match[0] in ['problem','question']:
                    url = prefix+globalcourseid+'/'+'problem'+'/'+match[2]
                elif match[0] in ['quiz','exam']:
                    url = prefix+globalcourseid+'/'+'quiz'+'/'+match[2]
                elif match[0] in ['module','lecture','video']:
                    url = prefix+globalcourseid+'/'+'lecture'+'/'+match[2]
                elif match[0] in ['slide']:
                    url = prefix+globalcourseid+'/'+'slide'+'/'+'slideid'+'/'+match[2]
                url_post.append([url,post])
print url_post
with open(output_filepath, 'w') as f:
    for url, post in url_post:
        f.write(url+' '+post+'\n')
