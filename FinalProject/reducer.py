#!/usr/bin/env python
# filename:reducer.py

import sys

totallength = 0
count = 0
question_length = 0
currentid = None

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 3:
        continue

    question_id, node_type, body_length = data
    body_length = float(body_length)

    if currentid != None and currentid != question_id:
        if count > 0:
            average_answer_length = totallength / count
        else:
            average_answer_length = 0

        print "{0}\t{1}\t{2}".format(currentid, question_length, average_answer_length)
        
        totallength = 0
        count = 0
        question_length = 0

    if node_type == "answer":
        totallength += body_length
        count += 1
    elif node_type == "question":
        question_length += body_length

    currentid = question_id

if currentid != None:
    if count > 0:
        average_answer_length = totallength / count
    else:
        average_answer_length = 0
    
    print "{0}\t{1}\t{2}".format(currentid, question_length, average_answer_length)




