#!/usr/bin/python

import sys
import re

validcc = re.compile('^[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$')
repeat4 = re.compile('([0-9])-?\\1-?\\1-?\\1')

def is_valid_cc(cc):
    if validcc.search(cc):
        if repeat4.search(cc):
            return False
        return True
    return False

for n in range(int(raw_input())):
    if is_valid_cc(str(raw_input())):
        print "Valid"
    else:
        print "Invalid"

#for i in [ '42536258796157867'\
#         , '4424444424442444'\
#         , '5424644424442444'\
#         , '5122-2368-7954 - 3214'\
#         , '44244x4424442444'\
#         , '0525362587961578']:
#    print i, ":\t", is_valid_cc(i)
    

