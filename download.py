#!/bin/env python2

import sys
import os
pwd=sys.path[0]

# os.system('cat /proc/cpuinfo')
f=open("account.txt")
errfile = open("err.log","w+")
while True:
    line1 = f.readline().strip()
    line2 = f.readline().strip()
    addr = pwd+"/"+line1
    if not line2: break
    line2 = line2+" "
    mkdir = "mkdir -p " + addr
    wget = "wget --load-cookies cookies.txt "+line2 +"-O "+addr+"/project.zip"
    errfile.write("YORUENKLSDJ")
    unzip = "unzip " + addr + "/project.zip -d "+addr


    res = os.system(mkdir)
    if res:
        exit(0)
    print wget
    res = os.system(wget)
    if res:
        errfile.write("Wget error: "+addr+"\n")
    print unzip
    res = os.system(unzip)
    if res:
        errfile.write("Unzip error: "+addr+"\n")
