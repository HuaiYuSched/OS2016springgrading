#!/bin/env python2

output=open("output.txt")
account = open("account.txt")
stulab = open("studentlab")
accountinfo = {}
finallist = {}
for line in account:
    acc = line.split()
    accountinfo[acc[0]] = acc[1]

for line in output:
    stuinfo = line.split()
    if stuinfo[2] in accountinfo:
        finallist[stuinfo[0]] = stuinfo[0] + " " + stuinfo[1] +" "+ accountinfo[stuinfo[2]]

    # else:
    #     print stuinfo[2]

for line in stulab:
    stu = line.split()
    if len(stu) == 3:
        if stu[1] not in finallist:
            index = stu[2].find("172.16.13.236")
            if index != -1:
                spstu = stu[2].split("/")
                if spstu[0]=="http:":
                    # print
                    finallist[stu[1]] = stu[1] + " " + stu[0] + " " + spstu[3]
                else :
                    # print stu[1],stu[0],spstu[0][18:]
                    finallist[stu[1]] = stu[1] + " " + stu[0] + " " + spstu[0][18:]

for key in finallist:
    print finallist[key]
