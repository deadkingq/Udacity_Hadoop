#!/usr/bin/env python
# filename: mapper.py


import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    if len(line) == 19:
        if not line[0].isdigit():
            continue
    
        node_id=line[0]
        author_id=line[3]
        node_type=line[5]
        abs_parent_id=line[7]
        
        if node_type == "answer":
            identifier = abs_parent_id
        elif node_type == "question":
            identifier = node_id
        
        print "{0}\t{1}".format(identifier, author_id)