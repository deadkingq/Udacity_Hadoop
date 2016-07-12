#!/usr/bin/env python
# filename: mapper.py

import sys
import re
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
delimiters = ['.',',','$',';','!','?',':','"','(',')','[',']','<','>','#','=','-','/',' ']
regex = '|'.join(map(re.escape, delimiters))
for data in reader:
    if len(data) == 19:
        ID=data[0]
        if ID== "id":
            continue
        body=data[4]
        cleanbody=re.split(regex,body)
        for words in cleanbody:
            print"{0}\t{1}".format(ID,words.lower())

