#!/usr/bin/env python
# filename:reducer.py

import sys

last_tag = None
tag_count = 0
toptag=[0]*10
topcount=[0]*10

for tag in sys.stdin:

    if last_tag!= None and last_tag!= tag:
        min_count=min(topcount)
        min_index=topcount.index(min_count)
        if int(tag_count)>= min_count:
            topcount[min_index]=int(tag_count)
            toptag[min_index]=last_tag
        tag_count=0

    last_tag = tag
    tag_count+=1


sort = sorted(range(10), key=lambda k: topcount[k], reverse=True)
for i in range(0,10):
    print  "{0}\t{1}".format(toptag[sort[i]],topcount[sort[i]])





