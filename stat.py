#!/bin/env python2

studlist = open("finallist")
scorefile = open("summary.txt")
score = {}
miss =[]
for line in scorefile:
    scoreline = line.split()
    score[scoreline[0]] = scoreline[2]


for line in studlist:
    stud = line.split()
    if stud[2] in score:
        print line.strip() + " " + score[stud[2]]
    else :
        miss.append(line.strip())
for stud in miss:
    print stud + " not in score file"
