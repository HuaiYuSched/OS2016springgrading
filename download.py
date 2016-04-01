#!/bin/env python2

import sys
import os
pwd=sys.path[0]

# os.system('cat /proc/cpuinfo')
f=open("download.txt")
errfile = open("err.log","w+")
while True:
    line1 = f.readline().strip()
    line2 = f.readline().strip()
    addr = pwd+"/"+line1
    if not line2: break
    line2 = line2+" "
    mkdir = "mkdir -p " + addr
    wget = "wget --load-cookies cookies.txt "+line2 +"-O "+addr+"/project.zip"
    # errfile.write("YORUENKLSDJ")
    unzip = "unzip " + addr + "/project.zip -d "+ addr

    gitclone = "git clone "+line2 +" " + addr
    res = os.system(mkdir)
    if res:
        exit(0)
    print gitclone
    res = os.system(gitclone)
    if res:
        errfile.write("gitclone error: "+addr+"\n")
