#!/usr/bin/env python
# filename:reducer.py

import sys
import re
import collections

index = collections.defaultdict(list)
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    word = data[1]
    index[word].append(int(data[0]))

for word in index:
    print "{0}\t{1}\t{2}".format(word, len(index[word]), sorted(index[word]))


