#!/usr/bin/env python
# filename:reducer.py

import sys

count=0
totalsale=0
currentweekday=None
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    weekday,cost=data
    cost=float(cost)
    if currentweekday and currentweekday!=weekday:
        print"{0}\t{1}".format(weekday,totalsale/count)
        count=0
        totalsale=0
    currentweekday=weekday
    count+=1
    totalsale+=cost
if currentweekday!=None:
    print"{0}\t{1}".format(weekday,totalsale/count)




