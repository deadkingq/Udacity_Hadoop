#!/usr/bin/env python
# filename: mapper.py


import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    if len(line) == 19:
        if not line[0].isdigit():
            continue
    
        tags=line[2]
        node_type=line[5]
        
        if node_type == "question":
            tags=tags.strip().split(' ')
            for tag in tags:
                print tag
