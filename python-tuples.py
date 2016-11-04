#!/usr/bin/python

import sys

gtuples = []

n = int(raw_input().strip())
t = tuple(map(int, str(raw_input().strip()).split(" ")))
print hash(t)


### Input
#>> 3 1
#>> 1 1 1
### Output
# 1
