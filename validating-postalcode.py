#!/usr/bin/python

import sys
import re

altrep = re.compile('([0-9])(?=[0-9]\\1)')
valpc = re.compile('\A[1-9][0-9]{5}\Z')

def is_valid_pc2(i):
    return not (valpc.search(i) == None) and (len(altrep.findall(i)) < 2)

def is_valid_pc(i):
    try:
        if int(i) < 100000 or int(i) > 999999:
            return False
    except:
        return False
    if len(altrep.findall(str(i))) > 1:
        return False
    return True

for i in [ '101100'\
         , '525201'\
         , '120101'\
         , '12ab01'\
         , '20201'\
         , '990011']:
    print i, ":\t", is_valid_pc(i), is_valid_pc2(i)

#for n in range(int(raw_input())):
#    if is_valid_cc(str(raw_input())):
#        print "Valid"
#    else:
#        print "Invalid"

