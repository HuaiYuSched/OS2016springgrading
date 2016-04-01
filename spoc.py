#!/bin/env python2

import os

f = open("spoc.html")
student_list = open("c")
log = open("spoc.log","w+")
storagy ={}
for line in f:
    lo = line.find("2009")
    if lo != -1:
        # print lo
        storagy[line[lo:lo+10]] = True

    lo = line.find("2011")
    if lo != -1:
        # print line[lo:lo+10]
        storagy[line[lo:lo+10]] = True
    lo = line.find("2012")
    if lo != -1:
        # print line[lo:lo+10]
        storagy[line[lo:lo+10]] = True
    lo = line.find("2013")
    if lo != -1:
        # print line[lo:lo+10]
        storagy[line[lo:lo+10]] = True
    lo = line.find("2014")
    if lo != -1:
        # print line[lo:lo+10]
        storagy[line[lo:lo+10]] = True

for line in student_list:
    number = line.split()[0]
    name = line.split()[1]
    if number not in storagy:
        print number, name
