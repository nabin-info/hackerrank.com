#!/usr/bin/python

import sys

glist = []

n = int(raw_input().strip())
for i in range(n):
    a = str(raw_input().strip()).split(" ")
    cmd,args = a[0], a[1:]
    if cmd == 'print':
        print glist
    else:
        eval('glist.'+cmd+'('+",".join(args)+')')


### Input
#>> 3 1
#>> 1 1 1
### Output
# 1
