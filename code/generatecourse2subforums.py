#!/usr/bin/python

'''This code is to generate a map betweem courses and subforums.
Usage: python generatecourse2subforums.py -p parent-directory-of-all-courses -o output
Input: the parent directory of all courses.
Output: a map from a course to a list of subforums that belong to this course.
'''

import argparse
import os

parser = argparse.ArgumentParser(prog='generatecourse2subforums.py', description='generate a map between courses and subforums')
parser.add_argument('-p', required=True, help='the parent directory of all courses')
parser.add_argument('-o', required=True, help='the file path of output')
args = parser.parse_args()
parent_directory = args.p
output_filepath = args.o

courses = os.listdir(parent_directory)
courses.sort()
print courses

course2subforums = {}
for course in courses:
    subforums = os.listdir(parent_directory+os.sep+course)
    subforums.sort()
    course2subforums[course] = subforums

with open(output_filepath, 'w') as f:
    for course in courses:
        subforums = course2subforums[course]
        f.write(course+' '+ ' '.join(subforums)+'\n')
