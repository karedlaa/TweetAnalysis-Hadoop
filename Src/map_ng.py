#!/usr/bin/python

import sys

for line in sys.stdin:
  line = line.strip()
  if line:
    words = line.split('\t')
    print '%s\t%s' % (words[1],words[0])
