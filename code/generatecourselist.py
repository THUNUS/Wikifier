#!/usr/bin/python

'''This code is to generate a list of course names.
Usage: python generatecourselist.py -p parent-directory-of-all-courses -o output
Input: the parent directory of all courses.
Output: a list of course names
'''

import argparse
import os

parser = argparse.ArgumentParser(prog='generatecourselist.py', description='generate a list of course names')
parser.add_argument('-p', required=True, help='the parent directory of all courses')
parser.add_argument('-o', required=True, help='the file path of output')
args = parser.parse_args()
parent_directory = args.p
output_filepath = args.o

courses = os.listdir(parent_directory)
courses.sort()
print courses

with open(output_filepath, 'w') as f:
    for course in courses:
        f.write(course+'\n')
