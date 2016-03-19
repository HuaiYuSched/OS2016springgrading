#!/bin/env python2
from bs4 import BeautifulSoup
import sys

def has_class_project_row(tag):
    if tag.has_attr('class'):
        return 'project-row' in tag.get("class")
    return False

def has_class_project_name(tag):
    if tag.has_attr('class'):
        return 'project-name' in tag.get("class")
    return False

def has_class_namespace_name(tag):
    if tag.has_attr('class'):
        return 'namespace-name' in tag.get("class")
    return False

reload(sys)
sys.setdefaultencoding('utf-8')

soup = BeautifulSoup(open("html.txt"),"lxml")

# print(soup.prettify())
result = soup.find_all(has_class_project_row)

for tags in result:
    for tag in tags.find_all(has_class_namespace_name):
        user = tag.string[:-2].strip()
    for tag in tags.find_all(has_class_project_name):
        print user+"/"+tag.string.strip()
    print "http://172.16.13.236"+tags.a.get('href').lstrip()+"/repository/archive.zip"
    # print "\n"
